#!/usr/bin/python3
"""
Fetch Top 10 posts
"""
import requests


def top_ten(subreddit):
    """
    Top 10 titles
    """
    headers = {
      "User-Agent": "API advanced"
    }
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    res = requests.get(
        url, headers=headers, params={"limit": 10}, allow_redirects=False
    )
    if res.status_code != 200:
        print("None")
        return
    result = res.json().get("data")
    for child in result.get("children"):
        print(child.get("data").get("title"))
