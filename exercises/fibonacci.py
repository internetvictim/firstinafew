

def fib(number):
    if number == 0:
        return sequence == []
    elif number == 1:
        return sequence == [0]
    else:
        sequence = [0, 1]
        for i in range(2, number):
            nextnum = sequence[i - 1] + sequence[i - 2]
            sequence.append(nextnum)
    return sequence


print("What is the size of the sequence you want?")
try:
    size = int(input("Size: "))
    print(f"fibonacci sequence : {fib(size)}")
except ValueError:
    print("Not a valid input")
