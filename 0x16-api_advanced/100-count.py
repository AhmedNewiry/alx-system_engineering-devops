#!/usr/bin/python3
"""Top !0 module"""

import requests

def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts 
    listed for a given subreddit.

    Args:
        subreddit: The name of the subreddit to search.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "reddit-bot"}
    params = {"limit": 10}
    
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        data = response.json()
        children = data["data"]["children"]
        if children:
            for i, child in enumerate(children[:10], start=1):
                print(f"{i}. {child['data']['title']}")
        else:
            print("No hot posts found.")
    else:
        print("None")
