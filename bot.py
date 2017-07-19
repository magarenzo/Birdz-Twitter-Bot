import os
import tweepy
from secrets import *
from time import gmtime, strftime

bot_username = 'fli_birdz_bot'
logfile_name = bot_username + ".log"

# read first line from file, delete that line from the file, tweet the line
def create_tweet():

    f = open("./facts.txt", "r")
    text = f.readline()
    if text == "":
        text = "I need to be given more facts to tweet!"
    lines = f.readlines()
    f.close()
    f = open("./facts.txt", "w")
    for line in lines:
        if line != text + "\n":
            f.write(line)
    return text

# authenticate connection to twitter account and send the tweet
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

# write to the log what occurred when trying to authenticate / send the tweet
def log(message):

    path = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(path, logfile_name), 'a+') as f:
        t = strftime("%d %b %Y %H:%M:%S", gmtime())
        f.write("\n" + t + " " + str(message))

if __name__ == "__main__":
    tweet_text = create_tweet()
    tweet(tweet_text)
