#!/usr/bin/python3

from collections import deque


def get_roman_value(char):
    if char == 'I':
        return 1
    elif char == 'V':
        return 5
    elif char == 'X':
        return 10
    elif char == 'L':
        return 50
    elif char == 'C':
        return 100
    elif char == 'D':
        return 500
    elif char == 'M':
        return 1000
    else:
        return 0


def roman_to_int(roman_string):
    result = 0
    max_int = 3999

    roman_chars = deque(roman_string.upper())

    memory = deque()  # queue -> stores processed characters (AKA Recall)

    while roman_chars:
        current_char = roman_chars[0]
        current_value = get_roman_value(current_char)
        if current_value == 0:
            roman_chars.popleft()
            continue
        if len(roman_chars) > 1:
            next_char = roman_chars[1]
            next_value = get_roman_value(next_char)

            if current_value < next_value:
                result -= current_value
            else:
                result += current_value
        else:
            result += current_value
        roman_chars.popleft()
        if result > max_int:
            return max_int
    return result

# print(roman_to_int("XXCMC"))
