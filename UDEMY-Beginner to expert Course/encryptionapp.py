def crypted (sentence):
    translaation = ""
    for element in sentence:
        if element in "Aa":
            translaation = translaation + "1"
        elif element in "Bb":
            translaation = translaation + "2"
        else:translaation = translaation + element

    return translaation

print(crypted(input("what do you want to crypt")))