#!/usr/bin/python3
"""Print the titles of the first 10 Hot Posts from a subreddit."""
import requests

def top_ten(subreddit):
    """Fetch and print the top 10 hot post titles from a subreddit."""
    headers = {'User-Agent': 'MyRedditBot/0.0.1'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        # If the subreddit is not found, print None
        if response.status_code != 200:
            print(None)
            return

        # Parse the JSON response to get the list of posts
        data = response.json().get('data', {}).get('children', [])
        if not data:
            print(None)
            return

        # Print the titles of the first 10 posts
        for post in data:
            print(post.get('data', {}).get('title'))
    
    except Exception:
        print(None)
