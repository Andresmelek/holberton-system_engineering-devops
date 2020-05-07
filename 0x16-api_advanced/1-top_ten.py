#!/usr/bin/python3
"""
function that queries the Reddit API and returns the number of subscribers
"""

import json
import requests


def top_ten(subreddit):
    """
    top ten of subscribers
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'linux:com.myapp:v.1'}
    params = {'limit': 10}

    response = requests.get(url=url, headers=headers, params=params)

    if response.status_code == 404:
        print('None')
        return

    lt = response.json().get('data').get('children')

    for post in lt:
        print(post.get('data').get('title'))
