#!/usr/bin/python3
"""Print the titles of the first 10 Hot Posts from a subreddit."""
import requests

def top_ten(subreddit):
    """Fetch and print the top 10 hot post titles from a subreddit."""
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        try:
            posts = response.json().get('data', {}).get('children', [])
            if not posts:
                print(None)
                return

            for post in posts:
                print(post.get('data', {}).get('title'))
        except (KeyError, ValueError):
            print(None)
    else:
        print(None)
