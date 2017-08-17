#!/usr/bin/env python

import os, tweepy
from secrets import *
from time import gmtime, strftime

logfile_name = "fli_birdz_bot.log"

# Authenticate connection to twitter account
auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
api = tweepy.API(auth)

# Follow back followers
def follow():
        followed = ''
        for follower in tweepy.Cursor(api.followers).items():
                follower.follow()
                followed += (follower.screen_name + ' ')
                log('Followed: ' + followed)

# Write to the log what occurred when trying to authenticate / send the tweet
def log(message):
        path = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        with open(os.path.join(path, logfile_name), 'a+') as f:
                t = strftime('%d %b %Y %H:%M:%S', gmtime())
                f.write("\n" + t + " " + str(message))

def main():
        follow()

main()
