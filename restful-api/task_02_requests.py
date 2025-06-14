#!/usr/bin/python3
"""
Module to practice working with requests library
"""
import requests
import json
import csv


def fetch_and_print_posts():
    try:
        r = requests.get("https://jsonplaceholder.typicode.com/posts")
        r.raise_for_status()
    except Exception as request_error:
        print(request_error)
        exit()
    print(f"Status Code: {r.status_code}")
    if (r.status_code == 200):
        try:
            json_obj = r.json()
        except requests.exceptions.JSONDecodeError as json_error:
            print(json_error)
            exit()
        for key in json_obj:
            print(f"{key['title']}")
        

# fetch_and_print_posts()


def fetch_and_save_posts():
    try:
        r = requests.get("https://jsonplaceholder.typicode.com/posts")
        r.raise_for_status()
    except Exception as request_error:
        print(request_error)
        exit()
    if (r.status_code == 200):
        try:
            json_obj = r.json()
        except requests.exceptions.JSONDecodeError as json_error:
            print(json_error)
            exit()
        posts_list = [{'id': key['id'], 'title': key['title'],
                       'body': key['body']} for key in json_obj]
        # print(posts_list)
        # formatted_json = json.dumps(posts_list, indent=4)
        # print(formatted_json)
        try:
            with open("posts.csv", mode="w") as csv_file:
                fieldnames = posts_list[0].keys()
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
                for row in posts_list:
                    writer.writerow(row)
        except csv.Error as csv_error:
            print(f"Couldn't Write to CSV: {csv_error}")
            exit()
        except Exception as error:
            print(f"Generic Error: {error}")
            exit()


fetch_and_save_posts()

# create new list of dict and
# my_list = [
#     {
#         'id': (the post's id),
#         'title': (the post's title),
#         'body': (the post's body)
#     },
# ]
