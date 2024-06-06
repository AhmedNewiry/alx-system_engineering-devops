#!/usr/bin/python3
"""Top !0 module"""
import sys
import requests

def top_ten():
    """ a function that queries the Reddit API and
        prints the titles of the first 10 ho
        t posts listed for a given subreddit
    """
    if len(sys.argv) != 2:
        return None

    subreddit = sys.argv[1]
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': '113'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            titles = [post['data']['title'] for post in data['data']['children']]
            return titles
        else:
            return None
    except requests.RequestException:
        return None
