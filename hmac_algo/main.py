import hmac
import hashlib
import random
import string


def api_secret_key_generator():
    api_key = ''.join(random.choice(string.ascii_uppercase + string.digits +
                      string.ascii_lowercase
                                    #   +string.punctuation
                                    ) for _ in range(32)).__str__()
    return api_key


def user_specific_message(*, db_username: str, db_password: str):
    concat_username_and_password = f"{db_username}{db_password}"
    return concat_username_and_password


def hmac_renewal(*, key, message, algorithms: hashlib = hashlib.sha512):
    _key = str.encode(key)
    _message = message.encode('UTF-8')
    _hmac = hmac.new(_key, _message, algorithms)
    return _hmac.hexdigest()


api_key_1 = api_secret_key_generator()
print("==>> api_key_1: ", api_key_1)
message_1 = user_specific_message(db_username="ashkan", db_password="123456")
_hmac = hmac_renewal(key=api_key_1, message=message_1)

# API_KEY = "1234"
# message = "ashkan12"
# encodedkey = str.encode(API_KEY)
# hmac1 = hmac.new(encodedkey, message.encode('UTF-8'), hashlib.sha512)
# digestvalue = hmac1.digest()
# # print("==>> digestvalue: ", digestvalue)
# digestvalue2 = hmac1.hexdigest()
# print("==>> digestvalue2: ", digestvalue2)
# # print("==>> size of MAC value : ", 8*hmac1.digest_size)


_API_KEY = str(input("insert API KEY: "))
_username = str(input("username: "))
_password = str(input("password: "))

_API_KEY_encoded = str.encode(_API_KEY)
_message = f"{_username}{_password}".encode("UTF-8")
hmac2 = hmac.new(_API_KEY_encoded, _message, digestmod=hashlib.sha512)

if hmac2.hexdigest() == _hmac:
    print("ok")
else:
    print("your request failed!")
