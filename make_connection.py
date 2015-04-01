# Yahoo! OAuth Credentials - http://developer.yahoo.com/dashboard/

# Credentials for an App hunter registered to be used only for test

CONSUMER_KEY      = 'dj0yJmk9clJFN2N6bTRSM3E4JmQ9WVdrOWJHSkdhamRFTm1VbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD0zZQ--'
CONSUMER_SECRET   = 'f9545904f2cc39f67104031c32ef83dfe37c6570'
APPLICATION_ID    = 'lbFj7D6e'
CALLBACK_URL      = 'localhost.owens.coffee'

from rauth import OAuth1Service

yahoo = OAuth1Service( 
	consumer_key=CONSUMER_KEY,
	consumer_secret=CONSUMER_SECRET, 
	name='yahoo', access_token_url= 'https://api.login.yahoo.com/oauth/v2/get_token',
	authorize_url= "https://api.login.yahoo.com/oauth/v2/request_auth"	, 
	request_token_url= "https://api.login.yahoo.com/oauth/v2/get_request_token",
	base_url='https://api.login.yahoo.com/oauth/v2/')

request_token, request_token_secret = yahoo.get_request_token(data = { 'oauth_callback': "oob" })


print "Request Token:"
print " - oauth_token = %s" % request_token
print " - oauth_token_secret = %s" % request_token_secret
auth_url = yahoo.get_authorize_url(request_token)
print 'Visit this URL in your browser: ' + auth_url
pin = raw_input('Enter PIN from browser: ')
session = yahoo.get_auth_session(request_token, request_token_secret, method='POST', data={'oauth_verifier': pin})