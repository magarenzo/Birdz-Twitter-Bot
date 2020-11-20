# Birdz Twitter Bot

Request webpages, scrape for and use data to create tweets

## Overview

`scrape_web.py` scrapes predetermined webpages for the bird facts that are shown on each. If the fact is less than or equal to 140 characters, it is written to a text file. This script is only ran once prior to the first automated running of `bot.py` so as to create and fill the text file

`bot.py` pulls what to tweet from a text file and then deletes that line from the file. The script then authenticates connection to the Twitter account and attempts to send out the tweet. Whatever occurs is written to a log file

`follow_back.py` makes sure that the account is following all of its followers. Whatever occurs is written to the same log file written to in `bot.py`

### Output

#### scrape_web.py

```
46 facts written to ./facts.txt for tweeting
```

### Crontab

```
0 12 * * * python ./bot.py`<br>`0 0,6,12,18 * * * python ./follow_back.py
```

## Dependencies

* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

* [Crontab](http://crontab.org/)

* [requests](http://docs.python-requests.org/en/master/)

* [tweepy](http://www.tweepy.org)

## Resources

* I use Crontab for scheduling daily automation

* Basic framework for `bot.py` was forked from [molly/twitterbot_framework](https://github.com/molly/twitterbot_framework) for creating Twitter bots using [Tweepy](http://www.tweepy.org). This goes along with her [tutorial](http://blog.mollywhite.net/twitter-bots-pt2/) on creating Twitter bots

## TODO

* If `bot.py` fails to send a tweet, do not delete that fact from the text file

* Remove repetitiveness from `scrape_web.py`

* Add error handling to `bot.py` and use a second log to record occurences

## Owner

[Michael A. Agarenzo](https://magarenzo.com)

This was originally created so that my old team would have a supply of random bird facts to cheer
