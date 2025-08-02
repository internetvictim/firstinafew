def splitter(words, delimiter):
    my_lynst = []
    lynstring = ""
    for i in words:
        if i == delimiter:
            my_lynst.append(lynstring)
            lynstring = ""
        else:
            lynstring += i
    my_lynst.append(lynstring)
    return my_lynst


def new_split(word, delimitor):
    mi_listo = []
    el_stringo = ""
    i = 0
    while i < len(word):
        if word[i:i+len(delimitor)] == delimitor:
            mi_listo.append(el_stringo.strip())
            el_stringo = ""
            i += len(delimitor)
        else:
            el_stringo += word[i]
            i += 1
    mi_listo.append(el_stringo)
    return mi_listo


print(new_split("hello -- brother -- johnny -- play-- da--guitar", "--"))
print(splitter("Bonjour, Monsieur, je, suis, nazim", ","))