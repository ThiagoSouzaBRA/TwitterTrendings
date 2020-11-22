  
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

lista = []
for x in range(len(trends[0]['trends'])):
 
  nome = trends[0]['trends'][x]['name'] + ": "
  volume = str(trends[0]['trends'][x]['tweet_volume'])
  if(volume != 'None'):
    print((nome + volume).encode('utf-8').strip())
    lista.append((nome + volume).encode('utf-8').strip())

with open('tweets.txt', 'w') as f:
  f.write('\n'.join([str(i) for i in lista]))
