import os
import tweepy
import csv
import re
import time

from config import *

# print(CONSUMER_KEY1)
# Authenticate
consumer_key=CONSUMER_KEY
consumer_secret=CONSUMER_SECRET

access_token=ACCESS_TOKEN
access_token_secret=ACCESS_TOKEN_SECRET


tweetsPerQry = 10
maxTweets = 150
# search_key = ['@Telkomsel', 'pjj']
# search_terms = ('@Telkomsel AND pjj')
# search_terms = ('@Telkomsel')
search_terms = ('@Telkomsel -filter:retweets')
# search_terms = 'pjj AND @Telkomsel -filter:retweets'
maxId = -1
tweetCount = 0
# date_since = "2020-01-01"
# date_until = "2020-08-24"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# contoh
# csvFile = open('tes20210425.csv', 'a', encoding='utf-8')
csvFile = open('tesyyyymmdd.csv', 'a', encoding='utf-8')
csvWriter = csv.writer(csvFile, delimiter=';')

# def hapus_link(tweet):
#     url_reg = r'https?://\S+'
#     result = re.sub(url_reg, '', tweet)
#     return result

# def hapus_emote(tweet):
#     return result

# Retrieve Tweets
# public_tweets = api.search(q=['Telkomsel', 'pjj'], count=10)
while tweetCount < maxTweets:
    progress(tweetCount+10, maxTweets, suffix='Doin long job')
    time.sleep(0.5)

    if maxId <= 0:
        newTweets = api.search(q=search_terms, count=tweetsPerQry, result_type="recent", tweet_mode="extended")
        # newTweets = api.search(q=search_terms, count=tweetsPerQry, since=date_since, tweet_mode="extended")
        # newTweets = api.search(q=search_terms, count=tweetsPerQry, since=date_since, until=date_until, tweet_mode="extended")

    else:
        newTweets = api.search(q=search_terms, count=tweetsPerQry, result_type="recent", tweet_mode="extended", max_id=str(maxId-1))
        # newTweets = api.search(q=search_terms, count=tweetsPerQry, since=date_since, tweet_mode="extended", max_id=str(maxId-1))
        # newTweets = api.search(q=search_terms, count=tweetsPerQry, since=date_since, until=date_until, tweet_mode="extended", max_id=str(maxId-1))

    if not newTweets:
        print("Tweets habis")
        break

    for tweet in newTweets:
        # dictTweet = {
        #     # "no" : maxId,
        #     "username" : tweet.user.name,
        #     "tweet" : tweet.full_text.encode('utf-8')
        # }
        # print("Username {username} : {tweet}".format(username=dictTweet["username"], tweet=dictTweet["tweet"]))
        # print("{username};{tweet}".format(username=dictTweet["username"], tweet=dictTweet["tweet"]))

        # csvWriter.writerow([tweet.user.screen_name, tweet.full_text])
        csvWriter.writerow([tweet.created_at, tweet.user.screen_name, tweet.full_text])
        # csvWriter.writerow([tweet.user.name, tweet.full_text])
        # csvWriter.writerow([tweet.user.name, hapus_link(tweet.full_text)])

        # data = pd.DataFrame(data=dictTweet, columns=[''])

        # with open('tes20210208.csv', "w", encoding='utf-8', newline='') as csv_file:
        #     fieldNames = ["username", "tweet"]
        #     writer = csv.DictWriter(csv_file, fieldnames = fieldNames, delimiter=";")
        #     writer.writeheader()
        #     for data in dictTweet:
        #         writer.writerow(data)
            # writer.writerow(data)

    tweetCount += len(newTweets)
    maxId = newTweets[-1].id
