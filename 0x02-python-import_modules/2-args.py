#!/usr/bin/python3
from sys import argv

num_args = len(argv) - 1

print("{:d} {}{}".format(num_args, "argument" if num_args == 1 else "arguments", "." if num_args == 0 else ":"))

for i, arg in enumerate(argv[1:], 1):
    print("{:d}: {}".format(i, arg))
