#pip install pycryptodome

from Crypto.PublicKey import RSA


key = RSA.generate(2048)
private_key = key.export_key()
file_out = open('./python_extra/rsa/private_key.pem','wb')
file_out.write(private_key)
file_out.close()

public_key = key.publickey().export_key()
file_out = open('./python_extra/rsa/public_key.pem','wb')
file_out.write(public_key)
file_out.close()