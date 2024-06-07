#!/usr/bin/python3
'''
API request module
'''

import requests


def number_of_subscribers(subreddit):
    ''' Qeuries for the number of subscribers '''
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Custom User Agent'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
