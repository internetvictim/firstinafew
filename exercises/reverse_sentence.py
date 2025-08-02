def reverse_sentence(sentence):
    listed_sentence = sentence.split(" ")
    if len(listed_sentence) == 1:
        return sentence
    else:
        word = listed_sentence[-1]
        return word + " " + reverse_sentence(" ".join(listed_sentence[0:-1]))


print(reverse_sentence("hello world this is nazim"))
