#!/usr/bin/python3
import sys

args = sys.argv[1:]
sum = 0

if len(args) > 0:
    for arg in args:
        sum += int(arg)

print(sum)
