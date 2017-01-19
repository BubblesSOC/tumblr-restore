import argparse
import json
import pytumblr

def load_credentials():
    from pkg_resources import resource_string
    return json.loads(resource_string(__name__, 'tumblr_credentials.json'))

class TumblrRestore:
    def __init__(self):
        credentials = load_credentials()
        self.client = pytumblr.TumblrRestClient(credentials['consumer_key'], credentials['consumer_secret'], credentials['oauth_token'], credentials['oauth_token_secret'])


def main():
    parser = argparse.ArgumentParser(description='Import Tumblr posts to a specified blog from a JSON backup')
    args = parser.parse_args()
    print(args)

if __name__ == '__main__':
    main()
