def generate_random_key(target_folder_path=None):
    """
    Generates a random Fernet key. 
    Fernet guarantees that a message encrypted using it cannot be manipulated or read without the key. Fernet is an implementation of symmetric (also known as “secret key”) authenticated cryptography
    """
    import os
    from cryptography.fernet import Fernet
    key = Fernet.generate_key()

    return key

def encrypt_message_with_key(message, key):
    """
    Encrypts string with (Fernet) key, returns bytes-like object.

    :param message: Message to be encrypted.
    :param path: Path where key is stored.
    """
    from cryptography.fernet import Fernet
    
    f = Fernet(key)
    return f.encrypt(message.encode('utf-8'))

def decrypt_message_with_key(encrypted_message, key):
    """
    Decrypts bytes-like object to string with (Fernet) key
    
    :param encrypted_message: Message to be encrypted.
    :param path: Path where key is stored.
    """
    from cryptography.fernet import Fernet
    
    f = Fernet(key)
    return f.decrypt(encrypted_message).decode("utf-8") 

def encrypt_file_with_key(input_file, output_file, key):
    """
    Encrypts file with (Fernet) key
    
    :param input_file: File to be encrypted.
    :param output_file: Outputfile, returns a bytes-like can be an arbitrary .
    """
    from cryptography.fernet import Fernet

    with open(input_file, 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)

    with open(output_file, 'wb') as f:
        f.write(encrypted)

def decrypt_file_with_key(input_file, output_file, key):
    """
    Decrypts file with (Fernet) key
    
    :param input_file: Bytes-like file to be decrypted.
    :param output_file: Outputfile, make sure to give this the same extension as basefile before encryption.
    """
    with open(input_file, 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    encrypted = fernet.decrypt(data)

    with open(output_file, 'wb') as f:
        f.write(encrypted)


def generate_key_from_password(password, salt=None):
    """
    Encrypts string with (Fernet) key, returns bytes-like object.

    :param message: Message to be encrypted.
    :param path: Path where key is stored.
    """

    import base64
    from cryptography.hazmat.backends import default_backend
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
    import socket

    # If no salt is set, use hostname as salt
    if not salt:
        salt = socket.gethostname().encode('utf-8')
    
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),length=32,salt=salt,iterations=500000,backend=default_backend())
    key = base64.urlsafe_b64encode(kdf.derive(password.encode('utf-8'))) 
    
    return key
    
decrypt_message_with_key(encrypt_message_with_key('Encryption with Automagica', key_from_password('very secure password 123')),key_from_password('very secure password 123')) 