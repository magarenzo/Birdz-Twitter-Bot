#!/usr/bin/env python

import os, tweepy
from secrets import *
from time import gmtime, strftime

bot_username = "fli_birdz_bot"
logfile_name = bot_username + ".log"

# Read first line from file and delete it
def create_tweet():
  facts = './facts.txt'

  f = open(facts, 'r')
  text = f.readline()
  f.close()
  if text == "":
    text = "I need to be fed more facts to tweet!"
  else:
    f = open(facts, 'r')
    lines = f.readlines()
    f.close()
    f = open(facts, 'w')
    for line in lines:
      if line != (text):
        f.write(line)
    return text

# Authenticate connection to twitter account and send the tweet
def tweet(text):
  auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
  auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
  api = tweepy.API(auth)

  try:
    api.update_status(text)
  except tweepy.error.TweepError as e:
      log(e.message)
  else:
    log("Tweeted: " + text)

# Write to the log what occurred when trying to authenticate / send the tweet
def log(message):
  path = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
  with open(os.path.join(path, logfile_name), 'a+') as f:
    t = strftime('%d %b %Y %H:%M:%S', gmtime())
    f.write("\n" + t + " " + str(message))

# Activate the functions written above
def main():
  tweet_text = create_tweet()
  tweet(tweet_text)

main()
