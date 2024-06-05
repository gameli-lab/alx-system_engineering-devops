!#/usr/bin/python3
'''
API request module
'''

import requests

def top_ten(subreddit):
    ''' Qeuries for the number of subscribers '''
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'Custom User Agent'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            print(post['data']['title'])
    else:
        print('None')

'''
if __name__ == "__main__":
    number_of_subscribers(subreddits)
'''
