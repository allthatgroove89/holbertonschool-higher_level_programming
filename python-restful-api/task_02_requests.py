#!/usr/bin/python3

import requests
import csv

def fetch_and_print_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f'Status Code: {response.status_code}')
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])

def fetch_and_save_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f'Staus code:{response.status_code}')
    if response.status_code == 200:
        posts = response.json()
        filtered_posts = []
        for post in posts:
            filtered_post = {key: post[key] for key in ('id', 'title', 'body')}
            filtered_posts.append(filtered_post)

        with open('posts.csv', 'w', newline='') as csvfile:
                fieldnames = ['id', 'title', 'body']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for post in filtered_posts:writer.writerow(post)

