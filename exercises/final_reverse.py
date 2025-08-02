# def final_reverse(sentence):
# listed_sentence = sentence.split(" ")
# if len(listed_sentence) <= 1:
#   return sentence[::-1]
# else:
#   for i in range(len(listed_sentence)):
#      word = listed_sentence[i]
#     listed_sentence.pop(i)
#    sentence = " ".join(listed_sentence)
#   return word[::-1] + " " + final_reverse(sentence)

def final_reverse(sentence):
    listed_sentence = sentence.split(" ", 1)
    if len(listed_sentence) <= 1:
        return sentence[::-1]
    else:
        return listed_sentence[0][::-1] + " " + final_reverse(listed_sentence[1])


print(final_reverse("hello world this is nazim"))
