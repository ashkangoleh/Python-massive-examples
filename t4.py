# import psycopg
# import psycopg2
# import datetime
# from psycopg_pool import ConnectionPool
# import asyncio

# connection = {
#     'host': 'venus.arz.team',
#     'user': 'data_scientist',
#     'password': 'ds_secret',
#     'port': 5435,
#     'dbname': 'blocks'
# }
# conninfo = "postgresql://{user}:{password}@{host}:{port}/{dbname}".format(**connection)
# begin_time = datetime.datetime.now()
# # # ps_conn = psycopg2.connect(**connection)
# # # ps_conn = psycopg.connect(**connection)
# # pool = ConnectionPool(conninfo)
# # # ps_cursor = ps_conn.cursor()
# # # ps_cursor.execute('SELECT * FROM block_stats ORDER BY id {0};'.format('desc',))
# # # ps_cursor.execute('SELECT * FROM block_stats;')
# # with pool.connection() as conn:
# #     conn.execute('SELECT * FROM block_stats;')
# # ps = pool.fetchall()
# # pool.close()
# # ps_conn.close()
# async def main():
#     aconn = await psycopg.AsyncConnection.connect(conninfo=conninfo)
#     async with aconn:
#         async with aconn.cursor() as cur:
#             await cur.execute('SELECT * FROM block_stats limit %s;',(10,))
#     aconn.close()
# asyncio.run(main())
# print(datetime.datetime.now() - begin_time)


# math example

# import math
# from decimal import Decimal
# numbers = [2400.2, 4800.3, 3000, 1.1 + 2.2, 0.000000000000006, -1.418686791445350, 1.418686791445356666666, 2400.418686791445350]

# def orderOfMagnitude(number):
#   return math.floor(math.log(abs(number), 10))

# for num in numbers:
#   places = 15 - orderOfMagnitude(num)
#   dec = Decimal(num).quantize(Decimal(f'1.{"0"*places}'))
#   print(dec)import math
# from decimal import Decimal
# numbers = [2400.2, 4800.3, 3000, 1.1 + 2.2, 0.000000000000006, -1.418686791445350, 1.418686791445356666666, 2400.418686791445350]

# def orderOfMagnitude(number):
#   return math.floor(math.log(abs(number), 10))

# for num in numbers:
#   places = 15 - orderOfMagnitude(num)
#   dec = Decimal(num).quantize(Decimal(f'1.{"0"*places}'))
#   print(dec)


# webscraping with pandas

# import pandas as pd
# import requests
# import time
# stockslist = ['f','goog', 'aapl']
# for s in stockslist:
#     print(s)
#     if s == 'aapl':
#       url = f'https://finance.yahoo.com/quote/{s}/?guccounter=1'
#     else:
#       url = f'https://finance.yahoo.com/quote/{s}/'
#     html = requests.get(url).text
#     print('html: ', html)
#     tablelist = pd.read_html(html, flavor='html5lib')
#     print('tablelist: ', tablelist)
#     # df = pd.concat(tablelist[:2])
#     # print(df)


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#         else:
#             tail = self.head
#             while tail.next:
#                 tail = tail.next
#             tail.next = new_node

#     def create_two_ll(self, lists):
#         ll_dict = {}
#         for i in range(len(lists)):
#             for data in lists[i]:
#                 self.append(data)
#             ll_dict[f"ll{i}"] = data
#         print(ll_dict)
#         return ll_dict


# if __name__ == "__main__":
#     ll = LinkedList()
#     ll.create_two_ll([[1,[3,2]]])
#     # ll.create_two_ll([[1,3,5], [2,4,6],[7,9,11],[8,10,12]])

# d = {"a":0,"b":1,"c":2}

# print(dict([list(d.items())[1]]))

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# variable_data = 300
# values = [*map(int, input(f'Enter two numbers {variable_data}: ').split())] # Enter two numbers 300:
# a = values[0] if len(values) > 0 else 100
# print('a: ', a)
# b = values[0] if len(values) > 0 else 200
# print('b: ', b)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# test = {"Default": {"test_data": {"data": "test"}},
#         "Test": {"abc_data": {"data": "test"}},
#         "Master": {"zxy_data": {"data": "test"}},
#         }

# print(test.keys())

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# fa_num = '۰١٢٣٤٥٦٧٨٩'
# en_num = '0123456789'

# table = str.maketrans(en_num, fa_num)
# normalized = "09912140491".translate(table)
# print(normalized)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# _SecondClass__name = "ashkan"
# class SecondClass():

#     def __init__(self):
#         super().__init__()
#         self.a = "overridden a"
#         self._b = "overridden b"
#         self.__c = "overridden c"
#     def return_name(self):
#           return __name

# obj2 = SecondClass()
# print(obj2._SecondClass__c)
# w = obj2._SecondClass__c = 12
# print(obj2.a)
# print(obj2._b)
# print(w)
# print(obj2.return_name())

# print(dict(("py","th","on")))

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

import functools
import time
import sys
import gc
# print(sys.getrecursionlimit())
print(sys.setrecursionlimit(5000000))

# def fib_without_cache(n):
#     if n < 2:
#         return n
#     return fib_without_cache(n-1) + fib_without_cache(n-2)

# # Execution start time
# begin = time.time()
# # fib_without_cache(50)
# print('fib_without_cache(30): ', fib_without_cache(30))
# end = time.time()
# print("Time taken to execute the\
# function without lru_cache is", f"{end-begin:0.9f}")

@functools.lru_cache(maxsize = None)
def fib_with_cache(n):
    if n < 2:
        return n
    return fib_with_cache(n-1) + fib_with_cache(n-2)


begin = time.time()
print('fib(1500): ', fib_with_cache(1500))
end = time.time()
print("Time taken to execute: ", f"{end-begin:0.9f}")


# # @functools.lru_cache()
def fib2(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    fibs = [1, 1]
    for _ in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return bin(fibs[-1] + fibs[-2])


def fib(n):
    v1, v2, v3 = 1, 1, 0    # initialise a matrix [[1,1],[1,0]]
    # perform fast exponentiation of the matrix (quickly raise it to the nth power)
    for rec in bin(n)[3:]:
        calc = v2*v2
        v1, v2, v3 = v1*v1+calc, (v1+v3)*v2, calc+v3*v3
        if rec == '1':
            v1, v2, v3 = v1+v2, v1, v2
    return v2


begin = time.time()
print('fib(1500): ', fib(1500))
end = time.time()
print("Time taken to execute1: ", f"{end-begin:0.9f}")
begin = time.time()
print('fib2(1500): ', int(fib2(1500),2))
end = time.time()
print("Time taken to execute2: ", f"{end-begin:0.9f}")

print('garbage collect: ', gc.collect())
