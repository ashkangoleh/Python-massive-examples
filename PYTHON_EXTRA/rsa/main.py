from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)
public_key = private_key.public_key()


private_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption(),
)
print("==>> private_pem: ", private_pem)

# with open('private_key1.pem', 'wb') as f:
#     f.write(pem)

public_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)
print("==>> public_pem: ", public_pem)
# with open('public_key.pem', 'wb') as f:
#     f.write(pem)




from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

# with open("private_key.pem", "rb") as key_file:
private_key_read = serialization.load_pem_private_key(
    # key_file.read(),
    private_pem,
    password=None,
    backend=default_backend()
)
print("==>> private_key_read: ", private_key_read)