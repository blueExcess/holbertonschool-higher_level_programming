#!/usr/bin/python3
def no_c(my_string):
    newString = list(my_string)
    for i in range(len(newString)):
        if newString[i] == 'c' or newString[i] == 'C':
            newString[i] = ""
    my_string = "".join(newString)
    return my_string
