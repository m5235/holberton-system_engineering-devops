#!/usr/bin/python3
"""
task 1
"""
import requests


def top_ten(subreddit):
    """ prints the titles of the first 10 hot posts
    """
    main_url = "https://www.reddit.com"
    headers = {
 "User-Agent": "chrome api (by /u/Cyber)"}
    request_info = requests.get(
        main_url + '/r/{}/hot.json?limit=10'.format(subreddit),
        headers=headers,
        allow_redirects=False,
        )
    if request_info.status_code == 404:
        return print(None)
    hottest = request_info.json().get("data").get("children")
    [print(child.get("data").get("title")) for child in hottest]

if __name__ == "__main__":
    number_of_subscribers()
