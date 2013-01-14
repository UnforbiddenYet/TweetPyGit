import os
import sys
import datetime
import tweepy
from git import Repo
from django.core.management.base import BaseCommand

# Git repository path
git_path = '/path/to/your/repository/'

# Twitter oauth file with ACCESS_KEY, ACCESS_SECRET
# file located in the same path as this script
file = 'TwitterOAuth.txt'

# OAuth Settings
CONSUMER_KEY = "#######################################" # Your CONSUMER_KEY
CONSUMER_SECRET = "####################################" # Your CONSUMER_SECRET


class Command(BaseCommand):
    def handle(self, *args, **options):
        repo = Repo(git_path) # Connect to your repository
        assert repo.bare == False
        repo.config_reader() # Get a config reader for read-only access
        last_commit =  repo.head.commit.message # Get the last commit
        print "Your last commit is '{0}'".format(last_commit.rstrip())
        self.twitter_authorize()
        tweet = last_commit.capitalize() # Capitalize first letter. We are serious gentlemen. Yeah :)
        # Update status on Twitter
        try:
            self.api.update_status(tweet)
            print "Commit successfully tweeted."
        except tweepy.error.TweepError, e:
            print e, "You have this commit in the Twitter timeline."

    def twitter_authorize(self):
        config = self.get_credentials()
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        # If script execution is firstly and there is no file with ACCESS_KEY and ACCESS_SECRET we are getting
        # them from Twitter and writing to the file. Next time we'll use them and skip authorization on Twitter.
        if config['no file'] or config['no data']:
            auth_url = auth.get_authorization_url()
            print '\nPlease authorize: ' + auth_url
            print '\nType bellow the PIN from Twitter site!'
            verifier = raw_input('PIN: ').strip()
            auth.get_access_token(verifier)
            with open(os.path.join(os.path.dirname(__file__),file), 'w') as f:
                f.write("ACCESS_KEY = %s\n" % auth.access_token.key)
                f.write("ACCESS_SECRET = %s" % auth.access_token.secret)
            f.close()
            config = self.get_credentials()
        auth.set_access_token(config['ACCESS_KEY'], config['ACCESS_SECRET'])
        self.api = tweepy.API(auth)

    def get_credentials(self):
        result = {'no data': False}
        try:
            with open(os.path.join(os.path.dirname(__file__),file)) as f:
                read_data = f.read()
            f.close()
            for line in read_data.split('\n'):
                if "ACCESS_KEY" in line:
                    result['ACCESS_KEY'] = line.split(" = ")[1]
                elif "ACCESS_SECRET" in line:
                    result['ACCESS_SECRET'] = line.split(" = ")[1]
                else:
                    result['no data'] = True
                result['no file'] = False
        except IOError:
            result['no file'] = True
        return result

