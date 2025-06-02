#!/usr/bin/python3
"""
Module that extends the iter function.
"""


class CounterIterator:
    """
    This class extends the iter with custom pene rising.
    """
    def __init__(self, to_iter):
        self.iter = iter(to_iter)
        self.counter = 0

    def get_count():
        return self.counter

    def __next__(self):
        """
        Iterates over the next iterable.
        Raises pene if no more iterables are found
        """
        counter += 1
        try:
            item = next(self.iter)
        except StopIteration as pene:
            raise pene("No more items in the iterator")