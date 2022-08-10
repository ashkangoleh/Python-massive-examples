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

# import functools
# import time
# import sys
# import gc
# # print(sys.getrecursionlimit())
# print(sys.setrecursionlimit(5000000))

# # def fib_without_cache(n):
# #     if n < 2:
# #         return n
# #     return fib_without_cache(n-1) + fib_without_cache(n-2)

# # # Execution start time
# # begin = time.time()
# # # fib_without_cache(50)
# # print('fib_without_cache(30): ', fib_without_cache(30))
# # end = time.time()
# # print("Time taken to execute the\
# # function without lru_cache is", f"{end-begin:0.9f}")

# @functools.lru_cache(maxsize = None)
# def fib_with_cache(n):
#     if n < 2:
#         return n
#     return fib_with_cache(n-1) + fib_with_cache(n-2)


# begin = time.time()
# print('fib(1500): ', fib_with_cache(1500))
# end = time.time()
# print("Time taken to execute: ", f"{end-begin:0.9f}")


# # # @functools.lru_cache()
# def fib2(n):
#     if n == 1:
#         return [1]
#     if n == 2:
#         return [1, 1]
#     fibs = [1, 1]
#     for _ in range(2, n):
#         fibs.append(fibs[-1] + fibs[-2])
#     return bin(fibs[-1] + fibs[-2])


# def fib(n):
#     v1, v2, v3 = 1, 1, 0    # initialise a matrix [[1,1],[1,0]]
#     # perform fast exponentiation of the matrix (quickly raise it to the nth power)
#     for rec in bin(n)[3:]:
#         calc = v2*v2
#         v1, v2, v3 = v1*v1+calc, (v1+v3)*v2, calc+v3*v3
#         if rec == '1':
#             v1, v2, v3 = v1+v2, v1, v2
#     return v2


# begin = time.time()
# print('fib(1500): ', fib(1500))
# end = time.time()
# print("Time taken to execute1: ", f"{end-begin:0.9f}")
# begin = time.time()
# print('fib2(1500): ', int(fib2(1500),2))
# end = time.time()
# print("Time taken to execute2: ", f"{end-begin:0.9f}")

# print('garbage collect: ', gc.collect())


# x = False
# tries = 6
#
#
# def drawgrid():
#     global tries
#     #  the variable is local so it will give a error by calling it in a function so by making it global it works as long as you add "global variable"
#     if tries == 6:
#         print("   _____ \n"
#               "  |      \n"
#               "  |      \n"
#               "  |      \n"
#               "  |      \n"
#               "  |      \n"
#               "  |      \n"
#               "__|__\n")
#
#     elif tries == 5:
#         print("   _____ \n"
#               "  |    0 \n"
#               "  |      \n"
#               "  |      \n"
#               "  |      \n"
#               "  |      \n"
#               "  |      \n"
#               "__|__\n")
#
#     elif tries == 4:
#         print("   _____ \n"
#               "  |    0 \n"
#               "  |    | \n"
#               "  |      \n"
#               "  |      \n"
#               "  |      \n"
#               "  |      \n"
#               "__|__\n")
#     elif tries == 3:
#         print("   _____ \n"
#               "  |    0 \n"
#               "  |    |- \n"
#               "  |      \n"
#               "  |      \n"
#               "  |      \n"
#               "  |      \n"
#               "__|__\n")
#
#     elif tries == 2:
#         print("   _____ \n"
#               "  |    0 \n"
#               "  |   -|-\n"
#               "  |      \n"
#               "  |      \n"
#               "  |      \n"
#               "  |      \n"
#               "__|__\n")
#
#     elif tries == 1:
#         print("   _____ \n"
#               "  |    0 \n"
#               "  |   -|-\n"
#               "  |   / \n"
#               "  |      \n"
#               "  |      \n"
#               "  |      \n"
#               "__|__\n")
#
#     elif tries == 0:
#         print("   _____ \n"
#               "  |    0 \n"
#               "  |   -|-\n"
#               "  |   / \ \n"
#               "  |      \n"
#               "  |      \n"
#               "  |      \n"
#               "__|__\n")
#
#
# def mainLoop():
#     global tries
#
#     print('Hello, please choose a word')
#     hangWord = input('')
#     operation4 = len(hangWord)
#     lettersOfWords = list(hangWord)
#     while not x:
#         print('enter a letter')
#         letter = input('')
#         if operation4 == 4:
#             if letter != lettersOfWords[0] and letter != lettersOfWords[1] and letter != lettersOfWords[2] and letter != \
#                     lettersOfWords[3]:
#                 print('Try again ')
#                 print('?', '?', '?', '?')
#                 tries -= 1
#                 drawgrid()
#                 print(f'{tries} life are left')
#             elif letter == lettersOfWords[0]:
#                 print(letter, '?', '?', '?')
#                 print('First letter found')
#
#             elif letter == lettersOfWords[1]:
#
#                 print('?', letter, '?', '?')
#                 print('second letter found')
#
#             elif letter == lettersOfWords[2]:
#                 print('?', '?', letter, '?')
#                 print('Third letter found')
#
#             elif letter == lettersOfWords[3]:
#                 print('?', '?', '?', letter)
#                 print('Fourth letter found')
#
#
# drawgrid()
# mainLoop()
# l = {
#   "fee_per_kwu": "0",
#   "witness_count": "0",
#   "guessed_miner": "Unknown",
#   "output_total_usd": "0.5",
#   "transaction_count": "1",
#   "version_bits": "000000000000000000000000000001",
#   "output_count": "1",
#   "input_count": "1",
#   "id": "0",
#   "input_total_usd": "0",
#   "fee_per_kb_usd": "0",
#   "generation": "5000000000",
#   "reward": "5000000000",
#   "version_hex": "1",
#   "generation_usd": "0.5",
#   "reward_usd": "0.5",
#   "cdd_total": "0",
#   "fee_total": "0",
#   "bits": "486604799",
#   "weight": "1140",
#   "merkle_root": "4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b",
#   "nonce": "2083236893",
#   "version": "1",
#   "difficulty": "1",
#   "fee_total_usd": "0",
#   "median_time": "2009-01-03 18:15:05",
#   "fee_per_kwu_usd": "0",
#   "chainwork": "0000000000000000000000000000000000000000000000000000000100010001",
#   "input_total": "0",
#   "size": "285",
#   "output_total": "5000000000",
#   "coinbase_data_hex": "04ffff001d0104455468652054696d65732030332f4a616e2f32303039204368616e63656c6c6f72206f6e206272696e6b206f66207365636f6e64206261696c6f757420666f722062616e6b73",
#   "stripped_size": "285",
#   "time": "2009-01-03 18:15:05",
#   "fee_per_kb": "0",
#   "hash": "000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f"
# }
# print([k for k,v in l.items()].index("id"))

# import grequests
# from threading import Thread

# class Test:
#     def __init__(self):
#         self.urls = [
#             'http://ploto.arz.team:7878/api/v1/strategies/ichimoku/price-above-kumo?resolution=1h&exchange=binance&category=spot',
#             'http://ploto.arz.team:7878/api/v1/strategies/ichimoku/price-below-kumo?resolution=1h&exchange=binance&category=spot',
#             'http://ploto.arz.team:7878/api/v1/strategies/ichimoku/price-crossed-up-kumo?resolution=1h&exchange=binance&category=spot',
#             'http://ploto.arz.team:7878/api/v1/strategies/ichimoku/price-crossed-down-kumo?resolution=1h&exchange=binance&category=spot',
#             'http://ploto.arz.team:7878/api/v1/strategies/ichimoku/price-crossed-up-base?resolution=1h&exchange=binance&category=spot',
#             'http://ploto.arz.team:7878/api/v1/strategies/ichimoku/price-crossed-down-base?resolution=1h&exchange=binance&category=spot',
#             'http://ploto.arz.team:7878/api/v1/strategies/ichimoku/price-below-base?resolution=1h&exchange=binance&category=spot',
#             'http://ploto.arz.team:7878/api/v1/strategies/ichimoku/price-above-base?resolution=1h&exchange=binance&category=spot',
#             'http://ploto.arz.team:7878/api/v1/strategies/ichimoku/price-below-conversion?resolution=1h&exchange=binance&category=spot',
#             'http://ploto.arz.team:7878/api/v1/strategies/ichimoku/price-above-conversion?resolution=1h&exchange=binance&category=spot',
#             'http://ploto.arz.team:7878/api/v1/strategies/ichimoku/price-crosses-down-conversion?resolution=1h&exchange=binance&category=spot',
#             'http://ploto.arz.team:7878/api/v1/strategies/ichimoku/price-crosses-up-conversion?resolution=1h&exchange=binance&category=spot',
#         ]

#     def exception(self, request, exception):
#         print("Problem: {}: {}".format(request.url, exception))

#     def async_(self):
#         results = grequests.map((grequests.get(u) for u in self.urls), exception_handler=self.exception, size=100)
#         print(results)

# test = Test()
# test.async_()


# concurrent = 1000

# for i in range(concurrent):
#     t = Thread(target=test.async_)
#     t.start()
#     print(t.getName())


# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import *
# from sqlalchemy.types import Integer, Text, DateTime
# from sqlalchemy import Column, create_engine
# Base = declarative_base()
# engine = create_engine("sqlite:///user.db?check_same_thread=False", echo=True)
# session = sessionmaker(bind=engine, autocommit=False, autoflush=False)
# db = session()
# Base = declarative_base()
# def init_db():
#     Base.metadata.create_all(bind=engine)

# class User(Base):
#     __tablename__ = "Users"


#     email = Column(Text ,primary_key = True)
#     password = Column(Text)

#     def __repr__(self):
#            return '{0}(email={1})'.format(self.__class__.__name__, self.email)

# def addUser(username, password):
#     user = User()
#     user.email = username
#     user.password = password
#     db.add(user)
#     db.commit()

# init_db()
# addUser("a", "b")

# import time

# time_to_wait = 30

# while time_to_wait:
#    seconds = time_to_wait % 60
#    mins = time_to_wait // 60
#    hours = mins * 60
#    timer = '{:02d}:{:02d}:{:02d}'.format(hours, mins, seconds)
#    print("\r", timer, end="")
#    time.sleep(1)
#    time_to_wait -= 1
   
   
import pandas as pd
import time
import requests
stockslist = ['f','goog', 'aapl']
for s in stockslist:
    url = f'https://finance.yahoo.com/quote/{s}/?guccounter=1'
    html = requests.get(url).content
    tablelist = pd.read_html(html, flavor='html5lib')
    df = pd.concat(tablelist[:2])
    print(df)