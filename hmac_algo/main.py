import hmac
import hashlib
import random
import string
from dataclasses import dataclass
from typing import Optional


@dataclass
class Authorization:
    username: str
    password: str
    api_key: str = ''

    @classmethod
    def encoded_api_key(cls):
        return str.encode(cls.api_key)

    @property
    def api_secret_key_generator(self):
        api_key = ''.join(random.choice(string.ascii_letters+string.digits+"!,@,#,$,%,^,&,*,+=-"
                                        ) for _ in range(32))
        return str.encode(api_key)

    @property
    def user_specific_message(self):
        concat_username_and_password = f"{self.username}{self.password}"
        return concat_username_and_password.encode('UTF-8')

    @property
    def hmac_renewal(self):
        _hmac = hmac.new(key=Authorization.encoded_api_key(),
                         msg=self.user_specific_message, digestmod=hashlib.sha512)
        return _hmac.hexdigest()


@dataclass
class ValidationAuth(Authorization):
    apiKey: str = ''
    token: Optional[str] = ''

    @classmethod
    def encoded_api_key(cls):
        return str.encode(cls.apiKey)

    @property
    def validation(self):
        check_validity_hmac = hmac.new(
            ValidationAuth.encoded_api_key(), self.user_specific_message, digestmod=hashlib.sha512).hexdigest()
        print(check_validity_hmac)
        print(self.hmac_renewal)
        return check_validity_hmac == self.hmac_renewal


# auth = Authorization("ashkan", "123456","+I-8Z49BJe@glpBH,6bADbIg&x#nROH&")
# print(auth.api_secret_key_generator)
# print(auth.hmac_renewal)

auth_validation = ValidationAuth(
    'ashkan', '123456', apiKey=",,XK&x,mIKC7,q#0J,#ah-ynq+l,,lfJ").validation
print("==>> auth_validation: ", auth_validation)


# message_1 = user_specific_message(db_username="ashkan", db_password="123456")
# _hmac = hmac_renewal(key=api_key_1, message=message_1)

# API_KEY = "1234"
# message = "ashkan12"
# encodedkey = str.encode(API_KEY)
# hmac1 = hmac.new(encodedkey, message.encode('UTF-8'), hashlib.sha512)
# digestvalue = hmac1.digest()
# # print("==>> digestvalue: ", digestvalue)
# digestvalue2 = hmac1.hexdigest()
# print("==>> digestvalue2: ", digestvalue2)
# # print("==>> size of MAC value : ", 8*hmac1.digest_size)


# _API_KEY = str(input("insert API KEY: "))
# _username = str(input("username: "))
# _password = str(input("password: "))

# _API_KEY_encoded = str.encode(_API_KEY)
# _message = f"{_username}{_password}".encode("UTF-8")
# hmac2 = hmac.new(_API_KEY_encoded, _message, digestmod=hashlib.sha512)

# if hmac2.hexdigest() == _hmac:
#     print("ok")
# else:
#     print("your request failed!")
