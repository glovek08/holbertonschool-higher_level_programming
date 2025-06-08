#!/usr/bin/python3
"""
Module with tasks for working with CSV and JSON format.
"""
import csv
import json

def convert_csv_to_json(csv_filename: str):
    if not isinstance(csv_filename, str):
        print("Error: The CSV filename must be a string.")
        return False

    json_output_filename = "data.json"
    data_to_serialize = []

    try:
        with open(csv_filename, mode="r", newline='', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                data_to_serialize.append(row)
    except FileNotFoundError:
        print(f"Error: CSV file not found at '{csv_filename}'.")
        return False
    except csv.Error as e:
        print(f"Error reading CSV file '{csv_filename}': {e}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred while reading the CSV file: {e}")
        return False

    try:
        with open(json_output_filename, mode="w", encoding='utf-8') as json_file:
            json.dump(data_to_serialize, json_file, indent=4)
    except IOError as e:
        print(f"Error writing to JSON file '{json_output_filename}': {e}")
        return False
    except TypeError as e:
        print(f"Error serializing data to JSON: {e}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred while writing the JSON file: {e}")
        return False

    return True