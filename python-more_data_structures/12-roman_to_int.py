#!/usr/bin/python3


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

    s = roman_string.upper()
    n = len(s)

    i = 0
    while i < n:
        current_char = s[i]
        current_value = get_roman_value(current_char)

        if current_value == 0:
            i += 1
            continue

        if i + 1 < n:
            next_char = s[i + 1]
            next_value = get_roman_value(next_char)

            if current_value < next_value:
                result -= current_value
            else:
                result += current_value
        else:
            result += current_value

        i += 1

        if result > max_int:
            return max_int

    return result
