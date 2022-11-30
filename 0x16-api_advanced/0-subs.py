#!/usr/bin/python3
"""
    Queries Reddit's API to find the number of subscribers for a given
    subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """ Makes a query to Reddit's API for a given subreddit and returns the
        number of subscribers to that subreddit.

    Args:
        subreddit (str): The name of the subreddit that will be used to query
        the API.

    Returns:
        Returns the number of subscribers to the subreddit.
        Returns 0 if the subreddit does not exist.
    """
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36\
    (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
    headers = {'User-Agent': user_agent}

    resp = requests.get('https://www.reddit.com/r/{}/new/.json?limit=1'
                        .format(subreddit),
                        headers=headers,
                        allow_redirects=False)
    subscribers = 0
    if resp.status_code == 200:
        a_dict = resp.json()
        a_dict = a_dict.get('data', {})
        a_list = a_dict.get('children', [])
        if len(a_list) != 0:
            a_dict = a_list[0]
            a_dict = a_dict.get('data', {})
            subscribers = a_dict.get('subreddit_subscribers', 0)
    return subscribers
