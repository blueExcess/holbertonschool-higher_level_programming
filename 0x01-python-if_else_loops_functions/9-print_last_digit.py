#!/usr/bin/python3
# function to print and return last digit of a number

def print_last_digit(number):
    if number < 0:
        d = number % -10
    else:
        d = number % 10
print("{:d}".format(d), end="")
return (d)
