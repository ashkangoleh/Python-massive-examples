# variable_data = 300
# values = [*map(int, input(f'Enter two numbers {variable_data}: ').split())]
# print('values: ', type(values))
# a = values[0] if len(values) > 0 else 100
# print('a: ', a)
# b = values[0] if len(values) > 0 else 200
# print('b: ', b)


# x,y = input("enter the numbers:").split()
# print(x,y)
import re

text = "Extract from debit card account"
test2 = re.search(r'Extract from (debit card|account)',string=text,flags=re.IGNORECASE).groups()
print("==>> test2: ", test2)