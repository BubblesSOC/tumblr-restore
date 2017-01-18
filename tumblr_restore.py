import json
import pytumblr

def main():
    with open('tumblr_credentials.json', 'r') as f:
        credentials = json.load(f)
        print(credentials)
