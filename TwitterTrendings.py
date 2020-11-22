# -- coding: utf-8 --
import sys
import tweepy
import json

#Autenticações
auth = tweepy.OAuthHandler('46pvnSwIVylfWepbPsP4433wL', 'xWDPHaUkk0ub93qj1DaYgJcO8QtkPUhNFIE7uBAvzbSVLLpLzR')
auth.set_access_token('1952916806-9WbU9ROPLd4aVPprQZqWJhaW4RSXrBw4oK8A4Ow',
'gW5iuYPtrTxVhPmQxBemsKz6jCAOqbYx1fT0ewKHFyAkG')


api = tweepy.API(auth)

#ID para o Brasil é 23424768.
#https://dev.twitter.com/docs/api/1.1/get/trends/place e http://developer.yahoo.com/geo/geoplanet/
BRAZIL_WOE_ID = 23424768

brazil_trends = api.trends_place(BRAZIL_WOE_ID)

trends = json.loads(json.dumps(brazil_trends, indent=1))
