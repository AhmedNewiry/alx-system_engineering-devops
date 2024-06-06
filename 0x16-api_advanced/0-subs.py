#!/usr/bin/python3
"""How many subs? module"""


import requests

def number_of_subscribers(subreddit):
    """ a function that queries the Reddit API
        and returns the number of subscribers
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; MyRedditApp/1.0; +http://yourwebsite.com)'}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except requests.RequestException:
        return 0
