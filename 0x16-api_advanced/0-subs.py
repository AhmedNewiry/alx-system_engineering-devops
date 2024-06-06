#!/usr/bin/python3
"""How many subs? module"""


import requests
import sys

def number_of_subscribers(subreddit):
    """a function that queries the Reddit API and
       returns the number of subscribers 
    """
    subreddit = sys.argv[1]
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent':'113'}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except requests.RequestException:
        return 0

