from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
import google.generativeai as genai
import base64
from io import BytesIO
from PIL import Image
from web3 import Web3
import json

app = Flask(__name__)

# 🔹 Configure Google Gemini AI
genai.configure(api_key="GEMINI_API_KEY")

# 🔹 Load AI Models
phishing_model = tf.keras.models.load_model("phishing_model")
malware_model = tf.keras.models.load_model("malware_model")
deepfake_model = tf.keras.models.load_model("deepfake_model")

# 🔹 Blockchain Integration
w3 = Web3(Web3.HTTPProvider("https://rinkeby.infura.io/v3/PROJECT_ID"))
with open("contract_abi.json") as f:
    ABI = json.load(f)
cyber_contract = w3.eth.contract(address="0xYourSmartContractAddress", abi=ABI)

# 🔹 AI-Based Phishing Detection (Gemini API)
def detect_phishing_gemini(text):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(f"Analyze this text for phishing risk: {text}")
    return float(response.text)

# 🔹 Blockchain Logging
def log_threat(threat_type, risk_score):
    txn = cyber_contract.functions.logThreat(threat_type, int(risk_score * 100)).buildTransaction({
        "gas": 100000,
        "gasPrice": w3.toWei('20', 'gwei'),
        "nonce": w3.eth.getTransactionCount(w3.eth.defaultAccount),
    })
    signed_txn = w3.eth.account.sign_transaction(txn, private_key="PRIVATE_KEY")
    tx_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
    return w3.toHex(tx_hash)

@app.route('/detect/phishing', methods=['POST'])
def detect_phishing():
    data = request.get_json()
    prediction = detect_phishing_gemini(data['text'])
    tx_hash = log_threat("Phishing", prediction)
    return jsonify({"phishing_risk": prediction, "tx_hash": tx_hash})

@app.route('/detect/malware', methods=['POST'])
def detect_malware():
    data = request.get_json()
    image_data = base64.b64decode(data['image'])
    image = Image.open(BytesIO(image_data)).convert('L').resize((64, 64))
    image_array = np.array(image) / 255.0
    image_array = np.expand_dims(image_array, axis=[0, -1])
    prediction = malware_model.predict(image_array)[0][0]
    tx_hash = log_threat("Malware", prediction)
    return jsonify({"malware_risk": prediction, "tx_hash": tx_hash})

if __name__ == '__main__':
    app.run(debug=True)
