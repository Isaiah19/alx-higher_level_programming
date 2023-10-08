#!/usr/bin/python3
# Isaiah Nweze (nwezeifeanyi93@gmail.com)

def print_reversed_list_integer(my_list=[]):
    if my_list:
        my_list.reverse()
        for number in my_list:
            print("{:d}".format(number))
