#!/usr/bin/python3
"""
task 0
"""
import requests


def number_of_subscribers(subreddit):
    """ Requests subscribers for a specific sub-reddit
    """
    main_url = "https://www.reddit.com"
    headers = {
        "User-Agent": "Ubuntu:playing with API (by /u/Cyber)"}
    get_subredd = requests.get(
        main_url + '/r/{}/about.json'.format(subreddit),
        headers=headers,
        allow_redirects=False,
        )
    if get_subredd.status_code == 404:
        return 0
    return get_subredd.json().get("data").get("subscribers")


if __name__ == "__main__":
    number_of_subscribers()
