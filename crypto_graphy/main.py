#first import package 'pip install cryptography'
from cryptography.fernet import Fernet


# we need to define the encryption key
# Fert can handle this with using generate_key() method

encryption_key = Fernet.generate_key()
print("==>> encryption_key: ", encryption_key)

#no we create out fernet object
cipher_suite = Fernet(encryption_key)
print("==>> cipher_suite: ", cipher_suite)

# to convert plain text to cipher text
# value = b'gAAAAABjjDISH-vTNbjN_n8FKL3xlB59A5cZbbKNE79QhyoJkoOIwG1zcbLEENg0AwqSIEWHtUpoti8dtSjWR9jbBmNhC3ZT3w=='
encrypted_value = cipher_suite.encrypt(b'whello') # gAAAAABjj first 8 or 9 characters are stable
print("==>> encrypted_value: ", encrypted_value.decode())


decrypted_value = cipher_suite.decrypt(encrypted_value)
print("==>> decrypted_value: ", decrypted_value.decode())
