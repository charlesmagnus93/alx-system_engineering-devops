#!/usr/bin/python3
"""
Recurse for titles
"""
import requests


def recurse(subreddit, hot_list=[]):
    """
    Title Liste
    """
    headers = {
      "User-Agent": "API advanced"
    }
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    params = {"limit": 10}
    res = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )
    if res.status_code != 200:
        return None
    result = res.json().get("data")
    children = result.gt("children")
    for child in children:
        title = child.get("data").get("title")
        hot_list.append(title)
