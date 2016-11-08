# In this assignment you must do a Twitter search on any term of your choice.
# Deliverables:
# 1) Print each tweet
# 2) Print the average subjectivity of the results
# 3) Print the average polarity of the results

# Be prepared to change the search term during demo.


import tweepy
import nltk
import requests
import requests_oauthlib
from textblob import TextBlob

# Unique code from Twitter
access_token = "791350505062760448-wBIfVcpp2jN4N01vudQqeWSiAuUbgrO"
access_token_secret = "hbHUIIT7f3Ebtb4LeXr0UYlZ1iOSuBUEeltb4bE5KCtck"
consumer_key = "lZ5f9CfP8zaTp6OqbX2FDrF8m"
consumer_secret = "PF2sd98ybkxNBdVo43Lg6M3Go6BDz2BY9JtfWsIUOGAU3n8PxG"


# Boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

#Now we can Create Tweets, Delete Tweets, and Find Twitter Users
pubtweets = api.search('UMSI')

# avgsub = 0
# avgpol = 0
# count = 0 

# for tweet in pubtweets:
# 	print(tweet.text)
# 	analysis = TextBlob(tweet.text)
# 	tweetsub = analysis.subjectivity
# 	tweetpol = analysis.polarity
# 	count += 1
# 	avgsub += tweetsub
# 	avgpol += tweetpol
# 	print("Tweet Subjectivity: ", tweetsub)
# 	print("Tweet Polarity: ", tweetpol)




print("Average subjectivity is ", (avgsub / count))
print("Average polarity is ", (avgpol / count))

