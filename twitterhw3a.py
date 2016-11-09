# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI-206 #Proj3 in the tweet.

# You will demo this live for grading.


import tweepy
import nltk
import glob
import random
import os
from TwitterAPI import TwitterAPI
#print("""No output necessary although you can print out a success/failure message if you want to.""")
print('\nJames Roesers Twitter: @james_roeser (look on twitter page to confirm results)')


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
api = TwitterAPI(consumer_key, consumer_secret, access_token, access_token_secret)
file = open('/Users/jamesroeser/Desktop/206/PROJECT-3/HW3-StudentCopy/twitterpic/smchg805s.jpg', 'rb')
#r-read it rb---read it, binary file
data = file.read()
r = api.request('statuses/update_with_media', {'status':'#UMSI-206 #Proj3'}, {'media[]':data})

print("Posted....status code =",r.status_code)

