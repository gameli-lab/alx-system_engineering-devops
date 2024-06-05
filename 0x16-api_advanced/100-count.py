#!/usr/bin/python3
''' Counting wordlist '''

import requests
import re

def count_words(subreddit, word_list):
    ''' Base case: empty word list'''
    if not word_list:
        return

    ''' Recursive case'''
    response = requests.get("https://www.reddit.com/r/{}/hot.json".format(subreddit), headers={"User-agent": "Mozilla/5.0"})

    ''' Check for valid response'''
    if response.status_code != 200:
        print("Invalid subreddit or no posts match.")
        return

    data = response.json()
    titles = [post["data"]["title"] for post in data["data"]["children"]]

    word_count = {}
    for title in titles:
        title_lower = title.lower()
        for word in word_list:
            word_lower = word.lower()
            ''' Check for word boundaries to avoid matching substrings'''
            matches = re.findall(r'\b' + re.escape(word_lower) + r'\b', title_lower)
            if matches:
                if word_lower in word_count:
                    word_count[word_lower] += len(matches)
                else:
                    word_count[word_lower] = len(matches)

    ''' Print sorted count of keywords'''
    sorted_word_count = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_word_count:
        print(word, count)

    ''' Recursive call with updated subreddit and word_list '''
    count_words(subreddit, word_list)

