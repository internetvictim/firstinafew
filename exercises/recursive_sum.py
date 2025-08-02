def recursive_sum(number):
    if number == 0:
        return 0
    else:
        sumofnums = number + recursive_sum(number - 1)
        return sumofnums


my_input = int(input("what number do you want to sum up?"))
print(recursive_sum(my_input))
