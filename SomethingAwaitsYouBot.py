import tweepy

from secret import *

auth = tweepy.OAuthHandler(C_KEY, C_SECRET)

try:
    redirect_url = auth.get_authorization_url()
except tweepy.TweepError:
    print('Error! Failed to get request token.')

verifier = raw_input('Verifier:')
