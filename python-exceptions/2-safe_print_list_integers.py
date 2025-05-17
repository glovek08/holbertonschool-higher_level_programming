#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    try:
        i = 0
        for each in my_list:
            if (i >= x):
                break
            print("{:d}".format(each), end=" ")
            i += 1
    except (TypeError, ValueError) as error:
        pass
    finally:
        print()
        return (i)
