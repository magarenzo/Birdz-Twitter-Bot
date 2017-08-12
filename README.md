# fli-birdz-twitter-bot

Twitter bot that tweets random facts about birds daily

---

<i>scraping.py</i> scrapes predetermined webpages for the bird facts that are shown on each. If the fact is less than or equal to 140 characters, it is written to a text file. This script is only ran once prior to the first automated running of <i>bot.py</i> so as to create and fill the text file. I created this script using [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) and [Requests](http://docs.python-requests.org/en/master/).

<i>bot.py</i> pulls what to tweet from a text file and then deletes that line from the file. The script then authenticates connection to the Twitter account and attempts to send out the tweet. Whatever occurs is written to a log file. Basic framework for this was forked from [molly/twitterbot_framework](https://github.com/molly/twitterbot_framework) for creating Twitter bots using Python 3 and [Tweepy](http://www.tweepy.org). This goes along with her [tutorial](http://blog.mollywhite.net/twitter-bots-pt2/) on creating Twitter bots.

<i>follow-back.py</i> makes sure that the account is following all of its followers. Whatever occurs is written to the same log file written to in <i>bot.py</i>.

I use [Crontab](http://crontab.org/) for scheduling daily automation. <i>crontab.txt</i> provides an example of how this automation can be set up.

---

**[@fli_birdz_bot](https://twitter.com/fli_birdz_bot)** was created so that my team has a supply of random bird facts to cheer.
