#!/usr/bin/python3
"""Top !0 module"""
import sys
import requests

def top_ten(subreddit):
    """ a function that queries the Reddit API and
        prints the titles of the first 10 ho
        t posts listed for a given subreddit
    """
    subreddit = sys.argv[1]
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "reddit"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        for post in data["data"]["children"]:
            print(post["data"]["title"])
    else:
        print(None)
