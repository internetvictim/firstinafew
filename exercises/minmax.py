# first take the input
try:
    user_input = input("List your numbers with a comma in between :")

    # transform the input into a list of integers
    listed_input = list(map(int, user_input.split(",")))
    # compare the numbers and attribute them into the corresponding list
    max_val = listed_input[0]
    min_val = max_val
    for n in listed_input:
        if n < min_val:
            min_val = n
        if n > max_val:
            max_val = n

    # display the result
    print(f"this is the max : {max_val}")
    print(f"this is the min : {min_val}")

    max_val_2 = max(listed_input)
    min_val_2 = min(listed_input)
    print(
        f"or i could just give it to you straight away with the functions : min : {min_val_2} max : {max_val_2}")
except ValueError:
    print("my brother in christ, read the instructions!")
