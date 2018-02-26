import tweepy
import os
 
# Consumer keys and access tokens, used for OAuth
consumer_key = 'GZI67A7mCUSVAiKSotV7VL8iL'
consumer_secret = 'iUb3v4KEB1GtCiXHxoygRTfZtpZYLayh74vcdMqGtCIahhqPDW'
access_token = '966150848358289408-zYjf4OeRmT5BEpThOIebtAsxkd8e7DV'
access_token_secret = '0eSbBzenK7v935Y4mvZZDyZ0iBdw9rK0klLlzgemupEZb'

 
# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
# Creation of the actual interface, using authentication
api = tweepy.API(auth)

# Creates the user object. The me() method returns the user whose authentication keys were used.
user = api.me()
 
print('Name: ' + user.name)
print('Location: ' + user.location)
print('Friends: ' + str(user.friends_count))
 
# Sample method, used to update a status
# api.update_status('Hello Form RBI Lab!')

# load image
imagePath = "img.jpg"
status = "Hi! From Python script=)"

# Send the tweet.
api.update_with_media(imagePath, status)
