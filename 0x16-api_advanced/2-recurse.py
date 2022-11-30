#!/usr/bin/python3
"""
    Queries Reddit's API to find all hot posts listed for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """ Recursively find all the hot posts for a given Reddit subreddit.

    Args:
        subreddit (str): The name of the subreddit that will be used to query
        the API.
        host_list (list of str): List containing titles of hot posts of the
        subreddit.
        after (str): ID of the last hot post in the returned result. Used to
        get the next 100 hot posts after this ID.

    Returns:
        The list containing the titles of all hot articles of a given
        subreddit.
        None if the subreddit does not exist.
    """
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36\
    (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
    headers = {'User-Agent': user_agent}
    url = 'https://www.reddit.com/r/{}/hot/.json?limit=100'.format(subreddit)
    if after is not None:
        url += '&after=' + after
    resp = requests.get(url,
                        headers=headers,
                        allow_redirects=False)
    if resp.status_code == 200:
        resp_dict = resp.json()
        data_dict = resp_dict.get('data', {})
        a_list = data_dict.get('children', [])
        for post in a_list:
            post_dict = post.get('data', {})
            title = post_dict.get('title')
            if title is not None:
                hot_list.append(title)
        after = data_dict.get('after')
        if after is None:
            return hot_list
        else:
            return (recurse(subreddit, hot_list, after))
    else:
        return None
