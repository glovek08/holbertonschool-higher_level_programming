#!/usr/bin/python3
"""
Module to practice working with requests library
"""
import requests
import json


# def fetch_and_print_posts():
#     try:
#         r = requests.get("https://jsonplaceholder.typicode.com/posts")
#         r.raise_for_status()
#     except HTTPError as request_error:
#         print(request_error)
#         exit()
#     print(f"Status Code: {r.status_code}")
#     if (r.status_code == 200):
#         try:
#             json_obj = r.json()
#         except requests.exceptions.JSONDecodeError as json_error:
#             print(json_error)
#             exit()
#         for key in json_obj:
#             print(f"{key['title']}")

# fetch_and_print_posts()

def fetch_and_save_posts():
    try:
        r = requests.get("https://jsonplaceholder.typicode.com/posts")
        r.raise_for_status()
    except HTTPError as request_error:
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
        formatted_json = json.dumps(posts_list, indent=4)
        print(formatted_json)


fetch_and_save_posts()

# create new list of dict and
# my_list = [
#     {
#         'id': (the post's id),
#         'title': (the post's title),
#         'body': (the post's body)
#     },
# ]
