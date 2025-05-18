#!/usr/bin/python3

class TrueException(TypeError):
    raise TypeError

def raise_exception():
    raise TrueException()
