# User Guide: LOCKING 1.0

LOCKING 1.0 is a simple file encryption and decryption tool that uses symmetric encryption (Fernet) to protect file contents. This program is compatible with Windows, macOS, and Linux operating systems. Below is a detailed guide on how to use the program.

## Features

1. **Encrypt Files**: Encrypt a specified file and generate a new encrypted file.
2. **Decrypt Files**: Decrypt a specified encrypted file back to its original form.
3. **Exit the Program**: End the program's execution.

## Requirements

- Python 3.x
- `cryptography` library (can be installed via `pip install cryptography`)

## Steps to Use

### 1. Install Python

- **Windows**:
  - Download Python from the [official Python website](https://www.python.org/downloads/).
  - During installation, make sure to check the box that says "Add Python to PATH".

- **macOS**:
  - You can install Python via [Homebrew](https://brew.sh/). Open the terminal and run:
    ```bash
    brew install python
    ```

- **Linux**:
  - Most Linux distributions can install Python via the package manager. For example, on Ubuntu, you can run:
    ```bash
    sudo apt update
    sudo apt install python3
    ```

### 2. Install the `cryptography` Library

Open the command prompt (Windows) or terminal (macOS and Linux), and enter the following command to install the `cryptography` library:
```bash
pip install cryptography
```
Alternatively, if you are using Python 3, you may need to use:
```bash
pip3 install cryptography
```

### 3. Download LOCKING 1.0

Download the `locking.py` file to your computer and remember the location where it is saved.

### 4. Run the Program

In the terminal or command prompt, navigate to the directory containing the `locking.py` file and run the following command:
```bash
python locking.py
```
If you are using Python 3, you may need to use:
```bash
python3 locking.py
```

### 5. Choose an Action

Once the program starts, you will see a welcome message and action prompts. Enter one of the following options:
- `1`: Encrypt a file
- `2`: Decrypt a file
- `3`: Exit the program

### 6. Input File Path

Depending on your chosen action, the program will prompt you to enter the file path. Ensure that the path you enter is valid and that the file exists.

### 7. Input Password

The program will ask you to enter a password. Remember this password, as it will be used for both encryption and decryption. The characters will not be displayed on the screen for security reasons.

### 8. View Results

- If you choose the encryption action, the program will generate a new file with a `.enc` extension, indicating that the file has been encrypted.
- If you choose the decryption action, the program will generate a file with the same name as the original file but without the `.enc` suffix, indicating that the file has been decrypted.

### 9. Exit the Program

Enter `3` to exit the program.

## Important Notes

- Ensure that the password you enter is consistent during both encryption and decryption; otherwise, decryption will fail.
- The original file will remain after encryption; you can delete it if needed.
- Keep your password secure, as losing it will result in an inability to decrypt the file.
- If the original file has a `.zip` or other format extension, the decrypted file will not have an extension; please manually add the correct extension corresponding to the original file.
- If you feel concerned about security, you can use different keys for secondary or multiple encryptions to enhance the file's security.

## Example

1. **Encrypting a File**:
   ```
   [*] Please choose an action (1: Encrypt, 2: Decrypt, 3: Exit): 1
   [*] Please enter the file path: example.txt
   [*] Please enter the password: ********
   File example.txt has been encrypted to example.txt.enc
   ```

2. **Decrypting a File**:
   ```
   [*] Please choose an action (1: Encrypt, 2: Decrypt, 3: Exit): 2
   [*] Please enter the file path: example.txt.enc
   [*] Please enter the password: ********
   File example.txt.enc has been decrypted to example.txt
   ```

3. **Exiting the Program**:
   ```
   [*] Please choose an action (1: Encrypt, 2: Decrypt, 3: Exit): 3
   Exiting the program.
   ```

By following these steps, you can easily use LOCKING 1.0 for file encryption and decryption.
