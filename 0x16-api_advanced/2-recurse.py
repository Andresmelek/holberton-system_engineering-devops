#!/usr/bin/python3
"""
recursive function that queries the Reddit API and returns a
list containing the titles of all hot articles for a given subreddit.
"""
import json
import requests


def recurse(subreddit, hot_list=[], after=""):
    """ curssion """
    if after is None:
        return title_list

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'linux:com.myapp:v.1'}
    params = {'limit': 100, 'after': after}

    response = requests.get(url=url, headers=headers, params=params)

    if response.status_code == 404:
        return None

    response = response.json()
    for post in response.get('data').get('children'):
        title_list.append(post.get('data').get('title'))
    nextt = response.get('data').get('after')
    return recurse(subreddit, title_list, nextt)
