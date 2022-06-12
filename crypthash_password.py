from passlib.context import CryptContext



pwt_context = CryptContext(schemes=['pbkdf2_sha256'],deprecated='auto')


class Hasher:
    @staticmethod
    def verify_password(plaintext,hashed_password):
        return pwt_context.verify(plaintext,hashed_password)
    
    
    @staticmethod
    def get_password_hash(plaintext):
        return pwt_context.hash(plaintext)
    
    
