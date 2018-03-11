"""
Lettuce Tweet these chilly men
yah
yah yeet yah
"""

# Libs
import tweepy
import time
import json
# Files
from twitter_keys import getKeys
import haus

access_token, access_secret, consumer_key, consumer_secret = getKeys()
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
paul = tweepy.API(auth)

# Lets get those Haikus
haikus = haus.HaiHaus()

# Tweets [15] haikus every [60] seconds
print("\nStarting to Tweet...")
starttime = time.time()
i = 0
while i < len(haikus):
	myHai = haikus[i]
	myTweet = ""
	for word in myHai[0]:
		myTweet += word + ' '
	myTweet += '\n'
	for word in myHai[1]:
		myTweet += word + ' '
	myTweet += '\n'
	for word in myHai[2]:
		myTweet += word + ' '

	paul.update_status(myTweet)
	print("\nStatus Updated!")

	i += 1
	# How long between every tweet
	time.sleep(60.0 - ((time.time() - starttime) % 60.0))

print("\nComplete!")