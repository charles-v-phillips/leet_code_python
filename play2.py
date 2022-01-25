import re

from collections import Counter


# class BankAccount :
#     def __init__(self,name = None, balance = 0):
#         self.__name = name
#         self.__balance = balance
#
#     def withdraw(self,n):
#         if n > self.__balance:
#             raise ValueError("NOT ENOUGH MONEY")
#         self.__balance -= n
#     def deposit(self,n):
#         self.__balance +=n
#     def check_balance(self):
#         print("Remaining Balance : {}".format(self.__balance))


# def s(*args):
#     for c in args:
#         print(c)
# s(1,2,3)


def play(f):
    def inner():
        print('Inside inner')
        return f()
    return inner

@play
def huh():
    print('in here too')


if __name__ == '__main__':
    huh()


# hexid = lambda val: print(hex(id(val)))
#
# L = [1,2,3]
# hexid(L)
# L +=  [4]
# hexid(L)
#
# lis1 + lis2
# lis1.__add__(lis2)
#
# class list:
#     def __add__(self, other):
#         return
