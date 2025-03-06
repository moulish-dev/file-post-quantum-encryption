import oqs
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

def generate_kyber_keys():
    """Generate post-quantum Kyber key pair."""
    with oqs.KeyEncapsulation('Kyber1024') as kem:
        public_key = kem.generate_keypair()
        secret_key = kem.export_secret_key()
        return kem, public_key, secret_key

def encapsulate_key(kem, public_key):
    """Generate a shared secret using Kyber key encapsulation."""
    ciphertext, shared_secret = kem.encap_secret(public_key)
    return ciphertext, shared_secret

def decapsulate_key(kem, ciphertext):
    """Recover the shared secret using the private key."""
    shared_secret = kem.decap_secret(ciphertext)
    return shared_secret

def encrypt_file(input_file, output_file, key):
    """Encrypt a file using AES-GCM with the Kyber-shared key."""
    iv = os.urandom(16)  # Random initialization vector
    cipher = AES.new(key[:32], AES.MODE_GCM, nonce=iv)
    
    with open(input_file, 'rb') as f:
        plaintext = f.read()
    
    ciphertext, tag = cipher.encrypt_and_digest(plaintext)
    
    with open(output_file, 'wb') as f:
        f.write(iv + tag + ciphertext)
    print(f"Encrypted file saved as: {output_file}")

def decrypt_file(input_file, output_file, key):
    """Decrypt a file using AES-GCM with the Kyber-shared key."""
    with open(input_file, 'rb') as f:
        iv = f.read(16)
        tag = f.read(16)
        ciphertext = f.read()
    
    cipher = AES.new(key[:32], AES.MODE_GCM, nonce=iv)
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)
    
    with open(output_file, 'wb') as f:
        f.write(plaintext)
    print(f"Decrypted file saved as: {output_file}")


def main():
    kem, public_key, secret_key = generate_kyber_keys()
    ciphertext, shared_secret = encapsulate_key(kem, public_key)
    recovered_secret = decapsulate_key(kem, ciphertext)
    
    print("Shared Secret Matches:", shared_secret == recovered_secret)
    
    # Encrypt and Decrypt a test file
    input_file = "sample.txt"
    encrypted_file = "encrypted.bin"
    decrypted_file = "decrypted.txt"
    
    # Create a sample file
    with open(input_file, "w") as f:
        f.write("Hello, this is a test message secured with post-quantum encryption!")
    
    encrypt_file(input_file, encrypted_file, shared_secret)
    decrypt_file(encrypted_file, decrypted_file, recovered_secret)

if __name__ == "__main__":
    main()
