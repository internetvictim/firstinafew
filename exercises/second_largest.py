# first : input from user
data_input = input("Enter your sequence of numbers with a space in between :")
# second : transform the input
data_list = list(map(int, data_input.split()))
# find the largest number manually
max_num = data_list[0]
for n in data_list:
    if n > max_num:
        max_num = n
max_number = max(data_list)  # easier way
print(max_number)
# find the second largest number manually
# new_list = data_list.copy()
# new_list.remove(max_num)
new_list = [n for n in data_list if n != max_num]
if not new_list:
    print("all the numbers are the same")
else:
    second_max = new_list[0]
    for n in new_list:
        if n > second_max:
            second_max = n
    deuxieme = max(new_list)  # easier way
    print(deuxieme)
    # print the result
    print(f"the biggest number is : {max_num}")
    print(f"the second biggest number is : {second_max}")


def nth_number(list, n):
    the_set = sorted(set(list), reverse=True)
    if len(the_set) >= n:
        return the_set[n-1]
    else:
        return None


print(nth_number(new_list, 3))
