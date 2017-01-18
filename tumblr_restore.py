import argparse
import json
import pytumblr

def main():
    parser = argparse.ArgumentParser(description='Import Tumblr posts to a specified blog from a JSON backup')
    args = parser.parse_args()
    print(args)

if __name__ == '__main__':
    main()
