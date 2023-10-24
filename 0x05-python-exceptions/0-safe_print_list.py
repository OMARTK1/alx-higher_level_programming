#!/usr/bin/python3
def safe_print_list(my_list=[], w=0):
    try:
        conta = 0
        for v in range(w):
            print(my_list[v], end="")
            conta += 1
        print()
        return conta
    except IndexError:
        print()
        return conta
