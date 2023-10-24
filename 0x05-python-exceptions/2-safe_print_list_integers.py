#!/usr/bin/python3
def safe_print_list_integers(my_list=[], w=0):
    conta = 0
    try:
        for v in range(w):
            if isinstance(my_list[v], int):
                print("{:d}".format(my_list[v]), end="")
                conta += 1
        print()
        return conta
    except IndexError:
        print()
        return conta
