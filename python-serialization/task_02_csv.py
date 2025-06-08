#!/usr/bin/python3
"""
Module with tasks for working with CSV and JSON format.
"""
import csv
import json


def convert_csv_to_json(filename: str):
    if isinstance(filename, str):
        for_json = []
        try:
            with open(filename, mode="r") as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for row in csv_reader:
                    for_json.append(row)
        except (AttributeError, TypeError, csv.Error) as error:
            print(f"Object cannot be deserialized: {error}")
            return False
        except (OSError, FileNotFoundError) as error:
            print(f"File operation failed: {error}")
            return False
        except Exception as error:
            print(f"Unexpected error: {error}")
            return False
        try:
            with open(filename, mode="w") as json_file:
                json.dump(for_json, json_file, indent=4)
        except (AttributeError, TypeError, pickle.PicklingError) as error:
            print(f"Object cannot be serialized: {error}")
            return False
        except (OSError, FileNotFoundError) as error:
            print(f"File operation failed: {error}")
            return False
        except Exception as error:
            print(f"Unexpected error: {error}")
            return False
        return True
