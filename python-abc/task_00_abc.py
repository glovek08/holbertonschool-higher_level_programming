#!/usr/bin/python3
"""
Module that creates an abstract Animal class
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract class using the abc's ABC module collection
    """
    @abstractmethod
    def sound():
        pass


class Dog(Animal):
    """
    Subclass of Animal that defines a Dog with his onomatopoeia
    """
    def sound():
        """
        Returns the sound made by a dog.
        """
        return "Bark"


class Cat(Animal):
    """
    Subclass of Animal that defines a cat with his onomatopoeia
    """
    def sound():
        """
        Returns the sound made by a dog.
        """
        return "Meow"
