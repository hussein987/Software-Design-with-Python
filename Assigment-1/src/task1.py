def decorator_1(fun):
    print(f"The function {fun.__name__} is decorated")
    def call_counter(x):
        call_counter.calls += 1
        return fun(x)
    call_counter.calls = 0
    return call_counter

# @decorator_1
# def test_fun(x):
#     return x ** 2


# if __name__ == '__main__':
#     print(test_fun.__dict__)
#     for i in range(10):
#         print(test_fun(i))
#     print(f"The function {test_fun.__name__} was called {test_fun.calls} times")