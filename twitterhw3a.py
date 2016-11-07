# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI-206 #Proj3 in the tweet.

# You will demo this live for grading.

print("""No output necessary although you 
	can print out a success/failure message if you want to.""")



import tweepy
import nltk
import glob
import random
import os
from TwitterAPI import TwitterAPI


# Unique code from Twitter
access_token = "791350505062760448-wBIfVcpp2jN4N01vudQqeWSiAuUbgrO"
access_token_secret = "hbHUIIT7f3Ebtb4LeXr0UYlZ1iOSuBUEeltb4bE5KCtck"
consumer_key = "lZ5f9CfP8zaTp6OqbX2FDrF8m"
consumer_secret = "PF2sd98ybkxNBdVo43Lg6M3Go6BDz2BY9JtfWsIUOGAU3n8PxG"

# Boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

#api = tweepy.API(auth)
#Now we can Create Tweets, Delete Tweets, and Find Twitter Users



api = TwitterAPI(consumer_key, consumer_secret, access_token, access_token_secret)
file = open('/Users/jamesroeser/Desktop/206/PROJECT-3/HW3-StudentCopy/twitterpic/smchg805s.jpg', 'rb')
#r-read it rb---read it, binary file
data = file.read()
r = api.request('statuses/update_with_media', {'status':'#UMSI-206 #Proj3'}, {'media[]':data})

print(r.status_code)






# from PIL import Image
# import glob
# image_list = []
# for filename in glob.glob('/Users/jamesroeser/Desktop/206/PROJECT\ 3/HW3-StudentCopy/twitterpic/smchg805s*.jpg'): #assuming gif
# 	im=Image.open(filename)
# 	image_list.append(im)
# api.update_with_media(image_list)

#def randomimagetwitt(folder):
    #Takes the folder where your images are as the input and twitts one random file.
# images = glob.glob("/Users/jamesroeser/Desktop/206/PROJECT\ 3/HW3-StudentCopy/twitterpic/smchg805s*.jpg")
# image_open = images.open(images)
# api.update_with_media(image_open)
#Twitts
#randomimagetwitt("/Users/jamesroeser/Desktop/206/PROJECT 3/HW3-StudentCopy/twitterpic")


#/Users/jamesroeser/Desktop/206/PROJECT 3/HW3-StudentCopy/twitterpic


################################
######public_tweets = api.search('UMSI')
# for tweet in public_tweets:
# 	print(tweet.text)
#Learn more about Search
#https://dev.twitter.com/rest/public/search
##############
# adj_count = 0;

# for tweet in public_tweets:
# 	print(tweet.text)
# 	tagged_tokens = nltk.pos_tag(tweet.text) # gives us a tagged list of tuples
# 	for (word, tag) in tagged_tokens:
# 		if tag == "JJ":
# 			adj_count+=1

# print("There were ", adj_count,"adjectives in your tweets")
	
# #Learn more about Search
# #https://dev.twitter.com/rest/public/search
###################