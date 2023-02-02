from Crypto.PublicKey import RSA


f = open('./PYTHON_EXTRA/rsa/private_key.pem','r')
f2 = open('./PYTHON_EXTRA/rsa/public_key.pem','r')

key1 = RSA.import_key(f.read())

key2 = RSA.import_key(f2.read())

# print("==>> key2: ", key2.export_key('PEM'))

# print("==>> key1: ", key1.export_key('PEM'))


test = open('./PYTHON_EXTRA/rsa/public_key.pem','r')
if test.read() == key2.export_key('PEM').decode('utf-8'):
    print("ok")
    
    
