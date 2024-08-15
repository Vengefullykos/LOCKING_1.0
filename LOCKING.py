import os
from cryptography.fernet import Fernet
from getpass import getpass
import base64
import hashlib

LIGHT_GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BLUE = "\033[94m"
RESET = "\033[0m"

def generate_key(password: str) -> bytes:
    key = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(key)

def encrypt_file(file_path: str, password: str):
    key = generate_key(password)
    fernet = Fernet(key)

    with open(file_path, 'rb') as file:
        original = file.read()

    encrypted = fernet.encrypt(original)

    with open(file_path + '.enc', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

    print(f"{YELLOW}File {file_path} has been encrypted to {file_path}.enc{RESET}")

def decrypt_file(file_path: str, password: str):
    key = generate_key(password)
    fernet = Fernet(key)

    with open(file_path, 'rb') as encrypted_file:
        encrypted = encrypted_file.read()

    try:
        decrypted = fernet.decrypt(encrypted)
    except Exception as e:
        print(f"{RED}[ATTENTION] Decryption failed, the password may be incorrect.{RESET}")
        return

    with open(file_path[:-4], 'wb') as decrypted_file:
        decrypted_file.write(decrypted)

    print(f"{YELLOW}File {file_path} has been decrypted to {file_path[:-4]}{RESET}")

def main():
    print(f"{LIGHT_GREEN}Welcome to LOCKING 1.0!{RESET}")
    while True:
        action = input(f"[{BLUE}*{RESET}] Please choose an action (1: Encrypt, 2: Decrypt, 3: Exit): ")
        
        if action == '3':
            print(f"{LIGHT_GREEN}Exiting the program.{RESET}")
            break
        
        file_path = input(f"[{BLUE}*{RESET}] Please enter the file path: ")
        password = getpass(f"[{BLUE}*{RESET}] Please enter the password: ")

        if action == '1':
            encrypt_file(file_path, password)
        elif action == '2':
            decrypt_file(file_path, password)
        else:
            print(f"{RED}Invalid operation.{RESET}")

if __name__ == "__main__":
    main()
