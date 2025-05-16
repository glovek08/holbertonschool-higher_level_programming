#!/usr/bin/python3
# dict1 = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0}
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    sorted_dict = a_dictionary.copy()
    try:
        sorted_dict = (sorted(sorted_dict.items(), key=lambda item: item[1]))
        return sorted_dict[-1][0]
    except Exception as error:
        print(error)
        return None 
# print(f"Before: {dict1}")
# print(f"After: {best_score(dict1)}")
