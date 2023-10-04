#!/usr/bin/python3

for num1 in range(0, 10):
    for num2 in range(num1 + 1, 10):
        if num1 != 8 or num2 != 9:
            print("{:02d}, ".format(num1 * 10 + num2), end="")
        else:
            print("{:02d}".format(num1 * 10 + num2))

