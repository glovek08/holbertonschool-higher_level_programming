#!/usr/bin/python3
"""
Create a dragon that likes the fly, swim and burn cities!
"""


class SwimMixin:
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    def burn_city(self, city):
        print(f"The dragon burns the city of {city} to the ground!,\
             fuck them!")


# draco = Dragon()
# draco.fly()
# draco.swim()
# draco.burn_city("Montevideo")
