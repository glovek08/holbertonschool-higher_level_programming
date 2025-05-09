#!/usr/bin/python3
import calculator_1 as calc1
b = 5
a = 10
if __name__ == "__main__":
    print("{} + {} = {}".format(a, b, calc1.add(a,b)))
    print("{} - {} = {}".format(a, b, calc1.sub(a,b)))
    print("{} * {} = {}".format(a, b, calc1.mul(a,b)))
    print("{} / {} = {}".format(a, b, calc1.div(a,b)))
