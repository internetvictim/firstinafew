def rec_fib(num):
    if num <= 1:
        return num
    return rec_fib(num - 2) + rec_fib(num - 1)


def my_fib(n):
    return [rec_fib for i in range(n)]
