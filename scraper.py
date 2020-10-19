#! python3

import dotenv
from dotenv import load_dotenv
import os
import praw
import pandas as pd
import datetime as dt
import json

load_dotenv()

client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('SECRET_KEY_27')
user_agent = 'JokeScraper'
username= os.getenv('REDDITUSER')
password= os.getenv('REDDITPW')

reddit = praw.Reddit(client_id=client_id, \
                     client_secret=client_secret, \
                     user_agent='JokeScraper', \
                     username=username, \
                     password=password)
subreddit = reddit.subreddit('oneliners')

def main():
    jokes = []
    for submission in subreddit.hot(limit=100):  
        jokes += [submission.title]
        print(submission.title)

    with open('jokes.txt', 'w') as f:
        for listitem in jokes:
            f.write('%s\n' % listitem)









main()
