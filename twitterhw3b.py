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

print('James Roesers Twitter: @james_roeser')


# Unique code from Twitter
access_token = "791350505062760448-wBIfVcpp2jN4N01vudQqeWSiAuUbgrO"
access_token_secret = "hbHUIIT7f3Ebtb4LeXr0UYlZ1iOSuBUEeltb4bE5KCtck"
consumer_key = "lZ5f9CfP8zaTp6OqbX2FDrF8m"
consumer_secret = "PF2sd98ybkxNBdVo43Lg6M3Go6BDz2BY9JtfWsIUOGAU3n8PxG"


# Boilerplate code 
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
#Now we can create and delete tweets and find users 
search_term = input('Please enter your search term-----> ')
pubtweets = api.search(search_term)

sub = 0
#subjectivity -- measures how factual
pol = 0
#polarity -- measures how positive or negative
count = 0 

for tweet in pubtweets:
	print('\nTweet-----> ',tweet.text)
	find = TextBlob(tweet.text)
	tsub = find.subjectivity
	tpol = find.polarity
	count += 1
	sub += tsub
	pol += tpol
	# print("Tweet Subjectivity-----> ", tsub)
	# print("Tweet Polarity-----> ", tpol)


print("\nAverage subjectivity = ", (sub / count))
print("Average polarity = ", (pol / count))

