#!/usr/bin/python3
"""
Recurse for titles
"""
import requests


def recurse(subreddit, hot_list=[], next_page=None, count=0):
    """
    Title Liste
    """
    headers = {
      "User-Agent": "API advanced"
    }
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    params = {"limit": 50, "next_page": next_page, "count": count}
    res = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )
    if res.status_code != 200:
        return None
    result = res.json().get("data")
    next_page = result.get("next_page")
    count += result.get('dist')
    children = result.get("children")
    for child in children:
        title = child.get("data").get("title")
        hot_list.append(title)
    if next_page is not None:
        return recurse(subreddit, hot_list, next_page, count)
    return hot_list

