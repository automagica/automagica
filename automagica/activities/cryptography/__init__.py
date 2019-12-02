@activity
def generate_random_key():
	"""
	Generates a random Fernet key. 
	Fernet guarantees that a message encrypted using it cannot be manipulated or read without the key. Fernet is an implementation of symmetric (also known as “secret key”) authenticated cryptography
	"""
	import os
	from cryptography.fernet import Fernet
	key = Fernet.generate_key()

	return key

@activity
def encrypt_text_with_key(text, key):
	"""
	Encrypts string with (Fernet) key, returns bytes-like object.

	:param text: Text to be encrypted.
	:param path: Path where key is stored.
	"""
	from cryptography.fernet import Fernet
	f = Fernet(key)

	return f.encrypt(text.encode('utf-8'))

@activity
def decrypt_text_with_key(encrypted_text, key):
	"""
	Decrypts bytes-like object to string with (Fernet) key
	
	:param encrypted_text: Text to be encrypted.
	:param path: Path where key is stored.
	"""
	from cryptography.fernet import Fernet
	f = Fernet(key)

	return f.decrypt(encrypted_text).decode("utf-8") 

@activity
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

@activity
def decrypt_file_with_key(input_file, output_file, key):
	"""
	Decrypts file with (Fernet) key
	
	:param input_file: Bytes-like file to be decrypted.
	:param output_file: Outputfile, make sure to give this the same extension as basefile before encryption.
	"""
	from cryptography.fernet import Fernet

	with open(input_file, 'rb') as f:
		data = f.read()

	fernet = Fernet(key)
	encrypted = fernet.decrypt(data)

	with open(output_file, 'wb') as f:
		f.write(encrypted)

@activity
def generate_key_from_password(password, salt=None):
	"""
	Generates (Fernet) key based on password and salt.
	
	:param text: text to be encrypted.
	:param salt: Salt to generate key in combination with password. Default value is the hostname. Take in to account that hostname is necessary to generate key, e.g. when files are encrypted with salt 'A' and password 'B', both elements are necessary to decrypt files.
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

@activity
def generate_hash_from_file(file, method='md5', buffer_size = 65536):
	"""
	Generate hash from file. Can be used to create unique identifier for file validation or comparison.

	:param file: File to hash
	:param method: Method for hashing, choose between 'md5', 'sha256' and 'blake2b'. Note that different methods generate different hashes.
	:param buffer_size: Buffer size for reading file in chunks, default value is 64kb
	"""
	import sys
	import hashlib

	# Arbitrary buffer size. 64kb for compatibility with most systems
	buffer_size = 65536  

	if method == 'md5':
		hash_list = hashlib.md5()
	if method == 'sha256':
		hash_list = hashlib.sha1()
	if method == 'blake2b':
		hash_list = hashlib.blake2b()

	with open(file, 'rb') as f:
		while True:
			data = f.read(buffer_size)
			if data:
				hash_list.update(data)
			else:
				return hash_list.hexdigest()

@activity			
def generate_hash_from_text(text, method='md5'):
	"""
	Generate hash from text.
	
	:param file: Text to hash
	:param method: Method for hashing, choose between 'md5', 'sha256' and 'blake2b'. Note that different methods generate different hashes.
	"""
	import sys
	import hashlib

	encoded_text = text.encode('utf-8')

	if method == 'md5':
		return hashlib.md5(encoded_text).hexdigest()
	if method == 'sha256':
		return hashlib.sha256(encoded_text).hexdigest()
	if method == 'blake2b':
		return hashlib.balke2b(encoded_text).hexdigest()