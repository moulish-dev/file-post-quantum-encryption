# Post-Quantum File Encryption

## 🚀 Overview
This project demonstrates **post-quantum secure file encryption** using **Kyber key exchange** (from the Open Quantum Safe `liboqs` library) and **AES-GCM encryption** (from `pycryptodome`).

It ensures secure file storage and transmission using post-quantum cryptography to protect against attacks from quantum computers.

## 🔑 Features
- **Generates Post-Quantum Key Pairs** using Kyber.
- **Encapsulates a shared secret** for secure key exchange.
- **Encrypts a file** using AES-GCM and the Kyber-shared key.
- **Decrypts the file** back using the encapsulated key.
- **Demonstrates encryption & decryption** on a test file.

## 🛠️ Setup & Installation

Presently this works on linux only.

### **1️⃣ Install Dependencies**
Activate your **Python virtual environment** and install required libraries:
```bash
python3 -m venv pqc_env
source pqc_env/bin/activate
pip install liboqs-python pycryptodome
```

### **2️⃣ Clone the Repository**
```bash
git clone https://github.com/moulish-dev/file-post-quantum-encryption.git
cd file-post-quantum-encryption
```

### **3️⃣ Run the Encryption Script**
```bash
python pq_encryption.py
```

## 📌 How It Works
1. **Generates a Kyber key pair**.
2. **Encapsulates a shared secret** using the Kyber public key.
3. **Encrypts a file (`sample.txt`) using AES-GCM** with the shared secret.
4. **Decrypts the file back (`decrypted.txt`)** using the recovered key.

## 📂 Files in This Repo
```
post-quantum-encryption/
│── pq_encryption.py       # Main encryption script
│── sample.txt             # Sample file to encrypt
│── encrypted.bin          # Encrypted output file
│── decrypted.txt          # Decrypted output file
│── requirements.txt       # Python dependencies
│── README.md              # Documentation
```

## ✅ Expected Output
After running the script, you should see:
- **Encrypted file**: `encrypted.bin`
- **Decrypted file**: `decrypted.txt` (same content as `sample.txt`)

## ⚡ Next Steps
- Integrate **post-quantum secure TLS handshake**
- Apply to **VPN encryption** using Kyber key exchange

## 📜 License
This project is licensed under the **MIT License**.

---
**🔒 Secure your data with Post-Quantum Cryptography! 🔒**

