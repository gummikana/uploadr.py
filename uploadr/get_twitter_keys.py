#!/usr/bin/env python

import webbrowser
import tweepy

# This is a small script to read and print out the keys required to post updates to twitter
# Run this script and copy the result and put them into the token_key and token_secret fields
# To get the API token and API secret register your application at
# https://dev.twitter.com/apps/new
#
# More about this at http://joshthecoder.github.com/tweepy/docs/auth_tutorial.html#auth-tutorial
consumer_token = ""
consumer_secret = ""

# Copy paste your magic keys here
auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
webbrowser.open(auth.get_authorization_url())

pin = raw_input('Verification pin number from twitter.com: ').strip()
token = auth.get_access_token(verifier=pin)

# Give user the access token
print 'Access token:'
print '  Key: %s' % token.key
print '  Secret: %s' % token.secret

# you can use this to test out if you can actually post updates
# auth.set_access_token(key, secret)
# So now that we have our OAuthHandler equipped with an access token, we are ready for business:
# api = tweepy.API(auth)
# api.update_status("Does this thing actually work?")

