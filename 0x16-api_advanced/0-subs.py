#!/usr/bin/python3
"""
Number of susbscribers
"""
import requests


def number_of_subscribers(subreddit):
	"""
	Request API
	"""
	headers = {
		"User-Agent": "API advanced"
	}
	url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
	res = requests.get(url, headers=headers, allow_redirects=False)
	if res.status_code != 200:
		return 0
	result = res.json().get('data').get('subscribers')
	return result
