#!/usr/bin/env python

import os, tweepy
from secrets import *
from time import gmtime, strftime

bot_username = "fli_birdz_bot"
logfile_name = bot_username + ".log"

# Authenticate connection to twitter account
auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
api = tweepy.API(auth)

# Follow back followers
for follower in tweepy.Cursor(api.followers).items():
  follower.follow()
  log("Followed: " + follower.screen_name)
