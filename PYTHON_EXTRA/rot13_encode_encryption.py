import codecs

def rot13_encode(message:str):
    return codecs.encode(message,'rot13')




print(rot13_encode("test"))
print(rot13_encode("test"))
print(rot13_encode("aA bB zZ 1234 *!?%"))