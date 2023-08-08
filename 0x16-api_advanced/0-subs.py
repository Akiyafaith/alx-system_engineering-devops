#!/usr/bin/python3

import requests

def number_of_subscribers(subreddit):
    """ queries the Reddit API and returns the number of subscribers"""
    user_agent = 'MyBot/1.0'
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': user_agent}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'subscribers' in data['data']:
            return data['data']['subscribers']
    return 0
