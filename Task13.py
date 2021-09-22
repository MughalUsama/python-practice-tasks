import time


def timee(func):
    def inner_function():
        start_time = time.time()
        func()
        end_time = time.time()
        print("Execution time:", end_time - start_time)

    return inner_function


@timee
def func1():
    print("Inside Func1")
    for i in range(2000):
        j = i ** 2
        j += i


@timee
def func2():
    print("Inside Func2")
    for i in range(2000):
        for j in range(3000):
            k = i * j
            k += 1


@timee
def func3():
    print("Inside Func3")
    for i in range(200):
        for j in range(200):
            for k in range(200):
                m = i * j - k
                m += 1


if __name__ == "__main__":
    func1()
    func2()
    func3()
