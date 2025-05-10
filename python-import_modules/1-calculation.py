#!/usr/bin/python3
import inspect
import calculator_1 as calc1
b = 5
a = 10
i = 0
operator = ['+', '-', '*', '/']
    #DERP mode?
    # print("{} + {} = {}".format(a, b, calc1.add(a,b)))
    # print("{} - {} = {}".format(a, b, calc1.sub(a,b)))
    # print("{} * {} = {}".format(a, b, calc1.mul(a,b)))
    # print("{} / {} = {}".format(a, b, calc1.div(a,b)))
if __name__ == "__main__":
    calc_functions = {
        name: obj for name, obj in inspect.getmembers(calc1, inspect.isfunction)
    } 
    for fname in calc_functions:
        print("{} {} {} = {}".format(a, operator[i], b, calc_functions[fname](a, b)))
        i += 1
    i = 0
