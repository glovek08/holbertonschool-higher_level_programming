#!/usr/bin/python3

# super_list = [1, 2, 5, 2, 3]

def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        for each in my_list:
            if i >= x:
                break
            print(each, end="")
            i += 1
    except Exception as error:
        print(error)
        return i
    else:
        return i
    finally:
        print()

# safe_print_list(super_list, 2)
