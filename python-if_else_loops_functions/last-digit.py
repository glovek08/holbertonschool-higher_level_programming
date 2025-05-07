#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = -abs(number) % 10 if number < 0 else abs(number) % 10
print(f"Last digit of {number} is {last_digit} ", end="")
print("and is greater than 5" if last_digit > 5 else "and is less than 6 and not 0" if last_digit != 0 else "and is 0")
