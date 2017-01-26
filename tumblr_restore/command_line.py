import argparse
from pkg_resources import resource_string
import json
import os
import oauth2 as oauth
from urlparse import parse_qsl
import pytumblr

class TumblrRestore:
    def __init__(self, blog_name, path_to_json):
        self.blog_name = blog_name
        self.path_to_json = path_to_json

        self.load_credentials()
        self.authenticate()

        self.client = pytumblr.TumblrRestClient(self.consumer_key, self.consumer_secret, self.oauth_token, self.oauth_secret)

    def load_credentials(self):
        credentials = json.loads(resource_string(__name__, 'tumblr_credentials.json'))
        self.consumer_key = credentials['consumer_key']
        self.consumer_secret = credentials['consumer_secret']

    def authenticate(self):
        """
        https://github.com/joestump/python-oauth2/wiki/Twitter-Three-legged-OAuth
        """
        request_token_url = 'https://www.tumblr.com/oauth/request_token'
        authorize_url = 'https://www.tumblr.com/oauth/authorize'
        access_token_url = 'https://www.tumblr.com/oauth/access_token'

        consumer = oauth.Consumer(key=self.consumer_key, secret=self.consumer_secret)
        client = oauth.Client(consumer)

        """
        Step 1: Get a request token. This is a temporary token that is used for
        having the user authorize an access token and to sign the request to obtain
        said access token.
        """
        resp, content = client.request(request_token_url, "GET")
        request_token = dict(parse_qsl(content))

        """
        Step 2: Redirect to the provider. After the user has granted access to you,
        the consumer, the provider will redirect you to whatever URL you have told
        them to redirect to.
        Ex: http://tumblr-restore.bubblessoc.net/?oauth_token=XXXXX&oauth_verifier=XXXXX
        """
        print "Go to the following link in your browser:"
        print "%s?oauth_token=%s" % (authorize_url, request_token['oauth_token'])
        verifier = raw_input("Enter your verfication code: ")

        """
        Step 3: Once the consumer has redirected the user back to the oauth_callback
        URL you can request the access token the user has approved. You use the
        request token to sign this request. After this is done you throw away the
        request token and use the access token returned. You should store this
        access token somewhere safe, like a database, for future use.
        """
        token = oauth.Token(request_token['oauth_token'], request_token['oauth_token_secret'])
        token.set_verifier(verifier)
        client = oauth.Client(consumer, token)
        resp, content = client.request(access_token_url, "POST")
        access_token = dict(parse_qsl(content))
        self.oauth_token = access_token['oauth_token']
        self.oauth_secret = access_token['oauth_token_secret']

def main():
    restore = TumblrRestore('sulahnnehn-dev', '~/Source/tumblr-utils/2017-01/bubbless0c/json/')
    parser = argparse.ArgumentParser(description='Import Tumblr posts to a specified blog from a JSON backup')
    #parser.add_argument('blog-name', help="the name of the blog you're posting to")
    #parser.add_argument('path-to-json', help='path to the directory containing your tumblr-utils JSON backup files')
    args = parser.parse_args()
    print(args)

if __name__ == '__main__':
    main()
