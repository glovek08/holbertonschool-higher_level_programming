#!/usr/bin/python3
set_1 = {"Python", "C", "Javascript", "Pene"}
set_2 = {"Bash", "C", "Ruby", "Perl", "Pene"}


def common_elements(set_1, set_2):
    common_set = list()  # will convert to set to handle duplicates
    for el_s1 in set_1:
        for el_s2 in set_2:
            if el_s1 == el_s2:
                common_set.append(el_s2)
    return set(common_set)


print(common_elements(set_1, set_2))
