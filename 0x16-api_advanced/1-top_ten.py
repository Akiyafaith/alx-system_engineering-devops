#!/usr/bin/python3
""" Function that Queries the Reddit API and print the titles of hot posts"""
import requests
 

def top_ten(subreddit):
    """ Query the Reddit API and print the titles of the fist 10 hot posts for a given subreddit"""
    user_agent = 'MyBot/1.0'
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': user_agent}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return


    data = response.json().get("data")
    if data is not None and "children" in data:
        for post in data["children"][:10]:
            post_data = post.get("data")
            if post_data is not None and "title" in post_data:
                print(post_data["title"])

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
