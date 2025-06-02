#!/usr/bin/python3
"""
Module that extends the iter function.
"""


class CountedIterator:
    """
    Custom iter implementation.
    """
    def __init__(self, to_iter):
        self.iter = iter(to_iter)
        self.counter = 0

    def get_count(self):
        return self.counter

    def __iter__(self):
        return self

    def __next__(self):
        try:
            item = next(self.iter)
            self.counter += 1
            return item
        except StopIteration:
            raise