# fli-birdz-twitter-bot

Twitter bot that tweets random facts about birds daily

---

Python script *scraping.py* scrapes four chosen webpages for the bird facts that are shown on each. If the fact is less than or equal to 140 characters, it is written to *facts.txt*. This script is only run once prior to the first automated running of *bot.py* so as to create and fill *facts.txt*. I created this using [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) and [Requests](http://docs.python-requests.org/en/master/).

Python script *bot.py* pulls what to tweet from *facts.txt* (while also deleting that line from the file so that it doesn't get used again), authenticates connection to the twitter account and attempts to send out the tweet. Whatever occurs is written to a log file. Crontab used for scheduling daily automation.

---

**[@fli_birdz_bot](https://twitter.com/fli_birdz_bot)**: The bot will send a tweet everyday at 12pm (Eastern time) starting on 7/26/2017. I will end the automation on 9/9/2017. (The bot also follows back its followers)

---

Basic framework forked from [molly/twitterbot_framework](https://github.com/molly/twitterbot_framework) for creating Twitter bots using Python 3 and [tweepy](http://www.tweepy.org). This goes along with her [tutorial](http://blog.mollywhite.net/twitter-bots-pt2/) on creating Twitter bots.

---

Created as a fun side project so that my team has a supply of random bird facts to cheer.
