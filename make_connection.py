import yahoo.application

# Yahoo! OAuth Credentials - http://developer.yahoo.com/dashboard/

CONSUMER_KEY      = '##'
CONSUMER_SECRET   = '##'
APPLICATION_ID    = '##'
CALLBACK_URL      = '##'

oauthapp      = yahoo.application.OAuthApplication(CONSUMER_KEY, CONSUMER_SECRET, APPLICATION_ID, CALLBACK_URL)

# Fetch request token
request_token = oauthapp.get_request_token(CALLBACK_URL)

# Redirect user to authorization url
redirect_url  = oauthapp.get_authorization_url(request_token)

# Exchange request token for authorized access token
verifier  = self.request.get('oauth_verifier') # must fetch oauth_verifier from request

access_token  = oauthapp.get_access_token(request_token, verifier)

# update access token
oauthapp.token = access_token

profile = oauthapp.getProfile()

print profile
