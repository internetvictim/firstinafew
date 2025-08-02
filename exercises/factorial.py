# factorial
def factorial(num):
    result = 1
    for i in range(num, 0, -1):
        result *= i
    return result


print(factorial(5))


def rec_factorial(numb):
    if numb <= 1:
        return 1
    else:
        return numb * rec_factorial(numb-1)


print(rec_factorial(5))
