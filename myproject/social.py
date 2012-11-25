import oauth2 as oauth
from settings import LINKEDIN_CONSUMER_KEY, LINKEDIN_CONSUMER_SECRET, \
    TWITTER_TOKEN, TWITTER_SECRET, OAUTH_TOKEN, OAUTH_SECRET
from twython import Twython

def updateTwitterStatus(status, dry_run=False):

    twitter = Twython(
        twitter_token=TWITTER_TOKEN,
	twitter_secret=TWITTER_SECRET,
	oauth_token=OAUTH_TOKEN,
	oauth_token_secret=OAUTH_SECRET
    )
    if dry_run: return twitter
    twitter.updateStatus(status=status)

def updateLinkedInStatus(request):
    
    # create a token for the authenticated user. We'll use this to access their profile
    token = oauth.Token(key=request.session['access_token'].key, secret=request.session['access_token'].secret)
    
    # create a consumer for us. We'll use this 
    consumer = oauth.Consumer(key=LINKEDIN_CONSUMER_KEY, secret=LINKEDIN_CONSUMER_SECRET)
    
    # this is the LinkedIn API endpoint we're trying to reach
    uri = 'http://api.linkedin.com/v1/people/~/current-status'
    
    # LinkedIn automatically prepends the user's name to this status, so beware! Also, this follows the request format they dictate on their docs
    body = '<?xml version="1.0" encoding="UTF-8"?><current-status>%s</current-status>' % request.POST['msg'] 
    
    # Create the oauth client using our consumer, and the authed user's token
    req = oauth.Client(consumer=consumer, token=token)
    
    # do it to it.
    resp, content = req.request(uri=uri, method='PUT', body=body)
    
    # if content is empty, that means the request went off w/out a hitch, return a 'success' to the AJAX callback
    if(content == ''):
        return HttpResponse('success')

    return HttpResponse(content)
