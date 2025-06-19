#!/usr/bin/python3

import requests
import csv

# Function to fetch and print posts
def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
       
    # Print the status code
    print(f"Status Code: {response.status_code}")
    
    # Check if the request was successful
    if response.status_code == 200:
        posts = response.json()  # Parse the JSON data from the response
        
        # Iterate through the posts and print their titles
        for post in posts:
            print(post['title'])

# Function to fetch and save posts to CSV
def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        posts = response.json()  # Parse the JSON data from the response
        
        # Open a CSV file in write mode
        with open('posts.csv', mode='w', newline='') as file:
            fieldnames = ['id', 'title', 'body']  # CSV column headers
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            
            writer.writeheader()  # Write the header row
            
            # Iterate through the posts and write each post to the CSV file
            for post in posts:
                writer.writerow({
                    'id': post['id'],
                    'title': post['title'],
                    'body': post['body']
                })
