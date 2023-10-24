#!/usr/bin/python3
magic_calculation = __import__('102-magic_calculation')
try:
    print(magic_calculation.magic_calculation(4, 1))
except Exception as e:
    print("Exception: {}".format(e))
