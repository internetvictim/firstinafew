# this is a list flattener
def flattener():
    my_list = []  # create an empty list
    numberof = int(input("how many lists?"))  # ask user for how many lists
    for times in range(0, numberof):  # loop to create the lists
        user_input = input(f"list number {times + 1} go!")  # input the lists
        # create a list of integers by applying(map) integerisation
        temp_list = list(map(int, user_input.split(",")))
        # into the splitted input and storing it into a temporary empty list
        my_list.append(temp_list)  # add the list into my_list
    flattened_list = []  # this is the ultimate list
    # for i in my_list:
    # if isinstance(i, list):
    #    for j in i:
    #      flattened_list.append(j)
    # else:
    #  flattened_list.append(i)

    flattened_list = [item for sublist in my_list for item in sublist]
    print(flattened_list)


flattener()
