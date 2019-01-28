# -*- coding: utf-8 -*-
"""
This script will delete all your tweets in the specified account.
"""
############################################################################
# Script Name    : tweets-destroyer                     
# Description    : Script that will delete all your tweets. (My account was hacked so I had a lot of spam tweets :)
# Author:        : Andrey Ruban  
# Original idea  : Dave Jeffery
# Email          :  
# Requirements   : Python 3, tweepy module
############################################################################

import tweepy

CONSUMER_KEY = 'XXX1'
CONSUMER_SECRET = 'XXX2'
ACCESS_TOKEN_KEY= 'XXX3'
ACCESS_TOKEN_SECRET='XXX4'

def oauth_login(consumer_key, consumer_secret):
     # Authenticate with twitter using OAuth    
     auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
     auth.set_access_token(access_token, access_token_secret)
    
     # Construct and return the API instance
     return tweepy.API(auth)

def delete_tweets(api):
    print("Are you want to delete all tweets from the account @{}?".format(api.verify_credentials().screen_name))
    user_answer = input("Type yes to proceed:  ")
    if user_answer.lower() == 'yes':
        for status in tweepy.Cursor(api.user_timeline).items():
            try:
                api.destroy_status(status.id)
                print("Deleted:", status.id)
            except:
                print("Failed to delete:", status.id)

if __name__ == "__main__":
    api = oauth_login(consumer_key, consumer_secret)
    print("Authenticated in Twitter as: {}".format(api.me().screen_name))
    delete_tweets(api)
