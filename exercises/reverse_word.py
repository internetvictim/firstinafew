def reverse_word(word):
    if len(word) == 1:
        return word
    else:
        return word[-1] + reverse_word(word[0:-1])


print(reverse_word("word"))
