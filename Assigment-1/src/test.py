def call_counter(func):
    print(func.__dict__)
    def helper(x):
        helper.calls += 1
        return func(x)
    helper.calls = 0
    return helper

@call_counter
def succ(x):
    return x + 1

@call_counter
def succ_1(x):
    return x + 1


if __name__ == '__main__':
    print(succ.__dict__)
    print(succ.calls)
    for i in range(10):
        print(succ(i))
        print(succ_1(i))
    print(succ.calls)
    print(succ_1.calls)