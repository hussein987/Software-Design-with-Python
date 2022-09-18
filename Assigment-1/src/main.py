import random
from task1 import decorator_1
# from task2 import decorator_2

@decorator_1
def func():
    # print("I am ready to Start")
    result = 0
    n =  random.randint(10,751)
    for i in range(n):
        result += (i**2)
        
@decorator_1
def funx(n=2, m=5):
    # print("I am ready to do serious stuff")
    max_val = float('-inf')
    n =  random.randint(10,751)
    res = [pow(i,2) for i in range(n)]
    for i in res:
        if i > max_val: 
            max_val = i


# @decorator_2
# def funh(bar1, bar2=""):
#     """
#     This function does something useful 
#     :param bar1: description
#     :param bar2: description
#     """ 
#     print("some\nmultiline\noutput")

    
if __name__ == "__main__": 
    # Task 1 tests
    func()
    funx()
    func()
    funx()
    func()

    # Task 2 test
    # funh(None, bar2="")