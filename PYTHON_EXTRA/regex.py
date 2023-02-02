import re



text = "اشکان"
text2 = 'مرتضي'


encoded_text =  text.encode('utf8')
utf8stdout = open(text, 'w', encoding='utf-8')
print("==>> encoded_text: ", utf8stdout)

regex = re.match(r"\xd8\xa7\xd8\xb4\xda\xa9\xd8\xa7\xd9\x86",text)
regex2 = re.match(r"^[\u0645\u0631\u062A\u0636\u064A]+$",text2)
print("==>> regex: ", regex)
print("==>> regex2: ", regex2)