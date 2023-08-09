#!/usr/bin/python3
"""a recursive function that queries the Reddit API"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recursively query the Reddit Api and return a list of
    titles of all hot articles"""
    user_agent = 'MyBot/1.0'
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': user_agent}
    params = {'after': after} if after else {}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    if response.status_code == 404:
        return None
    data = response.json().get("data")
    if data is not None and "children" in data:
        for post in data["children"]:
            post_data = post.get("data")
            if post_data is not None and "title" in post_data:
                hot_list.append(post_data["title"])
       after = data.get("after")
        if after is not None:
            return recurse(subreddit, hot_list, after=after)
        else:
            return hot_list
    else:
        return None

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = recurse(sys.argv[1])
        if result is not None:
            print(len(result))
        else:
            print("None")
