#!/usr/bin/python3

def uniq_add(my_list=[]):
    try:
        return sum(set(my_list))
    except TypeError:
        try:
            return sum(set(el for el in my_list if isinstance(el, int)))
        except Exception as e:
            print(f"Error: {e}")
            return 0
