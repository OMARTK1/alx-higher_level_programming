#!/usr/bin/python3
def safe_print_list_integers(my_list=[], w=0):
    conta = 0
    for v in range(w):
        try:
            print("{:d}".format(my_list[v]), end="")
            conta += 1
        except (ValueError, TypeError):
            pass
    print()
    return conta
