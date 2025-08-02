# THIS IS A PALINDROME CHECKER

def palindrome(word):
    word = word.lower()
    reversed_word = word[::-1]
    if reversed_word == word:
        return True
    else:
        return False

    # word_list = list(word)
    # reverse_word = []
    # for i in range(len(word_list) - 1, -1, -1):
      #   reverse_word.append(word_list[i])
    # if ''.join(reverse_word) == word:
      #   return True
    # else:
      #   return False


print("Enter your Palindrome")
my_word = str(input("Here : "))
if palindrome(my_word):
    print("Yes! your word is a Palindrome")
else:
    print("Nope, Try again :(")
