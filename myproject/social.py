import oauth2 as oauth
from settings import LINKEDIN_API_KEY, LINKEDIN_SECRET, LINKEDIN_OAUTH_TOKEN, LINKEDIN_OAUTH_SECRET, \
    TWITTER_TOKEN, TWITTER_SECRET, FACEBOOK_ID, OAUTH_TOKEN, OAUTH_SECRET
from twython import Twython
import fbconsole as fb

DEBUG_MEDIA = False

def updateAllMedia(form):

    if form['title']: status = form['title'].value()
    else: return
    if form['link']: link = form['link'].value()
    updateTwitterStatus(status + '\n' + link)

def updateTwitterStatus(status, dry_run=False):
  
    twitter = Twython(
        twitter_token=TWITTER_TOKEN,
	twitter_secret=TWITTER_SECRET,
	oauth_token=OAUTH_TOKEN,
	oauth_token_secret=OAUTH_SECRET
    )
    if dry_run: return twitter
    twitter.updateStatus(status=status)

def updateFacebookStatus(status):
    
 #   fb.APP_ID = FACEBOOK_ID
    fb.AUTH_SCOPE = ['publish_stream']
    fb.authenticate()
    fb.post('/crimson.beacon/feed', {'message': status})
    fb.logout()

def updateLinkedInStatus(status):
    
    # create a token for the authenticated user. We'll use this to access their profile
    token = oauth.Token(key=LINKEDIN_OAUTH_TOKEN, secret=LINKEDIN_OAUTH_SECRET)
    
    # create a consumer for us. We'll use this 
    consumer = oauth.Consumer(key=LINKEDIN_API_KEY, secret=LINKEDIN_SECRET)
    
    # this is the LinkedIn API endpoint we're trying to reach
    uri = 'http://api.linkedin.com/v1/people/url=http://www.linkedin.com/in/crimsonbeacon/current-status'
    
    # LinkedIn automatically prepends the user's name to this status, so beware! Also, this follows the request format they dictate on their docs
    body = '<?xml version="1.0" encoding="UTF-8"?><current-status>%s</current-status>' % status 
    
    # Create the oauth client using our consumer, and the authed user's token
    req = oauth.Client(consumer=consumer, token=token)
    
    # do it to it.
    resp, content = req.request(uri=uri, method='PUT', body=body)
    print "response: %s\ncontent:: %s" % (resp, content)

if DEBUG_MEDIA:
    ip = raw_input('test update status? fb | ln | none')
    if ip == 'fb':
        updateFacebookStatus('test update from fbconsole')
    if ip == 'ln':
        updateLinkedInStatus('test api status')

