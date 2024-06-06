#!/usr/bin/python3
"""Top !0 module"""


import requests

def recurse(subreddit, hot_list=[]):
    """
    Recursively queries the Reddit API and returns a list containing the titles
    of all hot articles for a given subreddit.

    Args:
        subreddit: The name of the subreddit to search.
        hot_list: A list to store the titles of hot articles.

    Returns:
        A list containing the titles of all hot articles for the given subreddit,
        or None if no results are found.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "reddit-bot"}
    params = {"limit": 100, "after": hot_list[-1] if hot_list else None}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        children = data["data"]["children"]
        if children:
            for child in children:
                hot_list.append(child["data"]["title"])
            return recurse(subreddit, hot_list)
        else:
            return hot_list
    else:
        return None
