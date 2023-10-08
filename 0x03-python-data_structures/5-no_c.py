#!/usr/bin/python3
# Isaiah Nweze (nwezeifeanyi93@gmail.com)

def no_c(my_string):
    listofchars = list(my_string)
    for char in listofchars:
        if char == 'c' or char == 'C':
            listofchars.remove(char)
    return("".join(listofchars))
