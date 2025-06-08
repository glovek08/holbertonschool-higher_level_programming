#!/usr/bin/python3
"""
Module that serializes dictionary into JSON file and
deserialize JSON file to recreate a dictionary.
"""
import pickle
from os import path


def serialize_and_save_to_file(data, filename):
    if (isinstance(filename, str)):
        try:
            with open(filename, mode="wb") as a_file:
                pickle.dump(data, a_file)
        except OSError as error:
            raise error
        except Exception:
            raise Exception


def load_and_deserialize(filename):
    if (isinstance(filename, str)):
        try:
            with open(filename, mode="rb") as a_file:
                return pickle.load(a_file)
        except OSError as error:
            raise error
        except Exception:
            raise Exception
