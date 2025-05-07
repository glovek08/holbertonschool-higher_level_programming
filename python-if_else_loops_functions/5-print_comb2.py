#!/usr/bin/python3
for num in range(100):
  print("{num}".format(num = num), end=", " if num < 99 else "\n")
  
