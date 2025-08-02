# recursion is about using a function inside itself

def rec_list(cursed):
    flattened_list = []
    for item in cursed:
        if isinstance(item, list):
            flattened_list.extend(rec_list(item))
        else:
            flattened_list.append(item)
    return flattened_list


my_list = [1, 5, 3, [2, 3, [5, 3], 3], 5]
print(rec_list(my_list))
