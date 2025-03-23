# AI-Powered Cyber Threat Detection

## Overview
This project is an AI-powered cyber threat detection system that leverages machine learning models and blockchain technology to detect phishing, malware, and deepfake threats. It integrates:
- **Google Gemini AI** for phishing detection
- **TensorFlow models** for malware and deepfake detection
- **Ethereum blockchain** for logging threats

## Features
- **Phishing Detection:** Uses Google Gemini AI to analyze text and detect phishing attempts.
- **Malware Detection:** Uses a TensorFlow-based deep learning model to scan images for malware indicators.
- **Deepfake Detection:** Uses a deep learning model to assess images for deepfake manipulation.
- **Blockchain Logging:** Logs cyber threats onto an Ethereum-based blockchain for transparency and security.
- **Web Interface:** Provides an easy-to-use UI for users to check phishing risk, scan malware, and analyze deepfake content.

## Technologies Used
- **Flask** (Backend API)
- **TensorFlow** (Machine Learning Models)
- **Google Gemini AI** (Phishing Detection)
- **Web3.py** (Blockchain Integration)
- **Ethereum Blockchain** (Threat Logging)
- **HTML, CSS, JavaScript (Bootstrap)** (Frontend UI)

## Installation
1. **Clone the repository**
    ```sh
    git clone https://github.com/your-repo/cyber-threat-detection.git
    cd cyber-threat-detection
    ```
2. **Create a virtual environment and install dependencies**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    pip install -r requirements.txt
    ```
3. **Set up environment variables**
    - `GEMINI_API_KEY`: API key for Google Gemini AI
    - `PROJECT_ID`: Infura project ID for Ethereum blockchain
    - `PRIVATE_KEY`: Private key for Ethereum transactions
4. **Run the Flask server**
    ```sh
    python app.py
    ```
5. **Access the Web UI**
    - Open `http://127.0.0.1:5000` in your browser.

## API Endpoints
### 1. Phishing Detection
- **Endpoint:** `/detect/phishing`
- **Method:** `POST`
- **Request Body:**
    ```json
    {
        "text": "Suspicious email or message text"
    }
    ```
- **Response:**
    ```json
    {
        "phishing_risk": 0.85,
        "tx_hash": "0x123456789..."
    }
    ```

### 2. Malware Detection
- **Endpoint:** `/detect/malware`
- **Method:** `POST`
- **Request Body:**
    ```json
    {
        "image": "base64_encoded_image"
    }
    ```
- **Response:**
    ```json
    {
        "malware_risk": 0.92,
        "tx_hash": "0xabcdef123..."
    }
    ```

### 3. Deepfake Detection
- **Endpoint:** `/detect/deepfake`
- **Method:** `POST`
- **Request Body:**
    ```json
    {
        "image": "base64_encoded_image"
    }
    ```
- **Response:**
    ```json
    {
        "deepfake_risk": 0.78,
        "tx_hash": "0x987654321..."
    }
    ```

## Blockchain Integration
- The system logs detected threats onto the **Ethereum blockchain** using Web3.py.
- Smart contract functions are utilized for logging threats securely.

## Contributing
1. **Fork the repository**
2. **Create a new branch**
    ```sh
    git checkout -b feature-branch
    ```
3. **Commit changes and push**
    ```sh
    git commit -m "Added new feature"
    git push origin feature-branch
    ```
4. **Submit a pull request**

## License
This project is licensed under the MIT License.

## Contact
For any issues or inquiries, please contact: **ritesh.kumar.cs28@iilm.edu**

