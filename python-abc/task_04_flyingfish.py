#!/usr/bin/python3
"""
This module is a zoo with an experimental research facility,
it has Fish and Birds, crazy scientists have been playing with their genes
and now they have flying shitting birds.
"""


class Fish:
    """
    Fish
    """
    def swim(self):
        print("The fish is swimming.")

    def habitat(self):
        print("The fish lives in water.")


class Bird:
    """
    A bird, watch out! some kids have feed them birds laxatives
    They now shit all over the place!
    """
    def fly(self):
        print("The bird is flying.")

    def habitat(self):
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    Damn scientists have created an abomination!
    Chiquita Banana, Chiquita Banana, OBAMA!
    """
    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in wather and the sky!")

# flying_shit = FlyingFish()
# flying_shit.fly()
# flying_shit.habitat()
# flying_shit.swim()
# print(FlyingFish.__mro__)
