# accesstwitter.py taken from
# https://stackabuse.com/accessing-the-twitter-api-with-python/

# twitterAPI_1.py

# Import the Twython class
from twython import Twython  
import json

# Load credentials from json file
with open("twitter_credentials.json", "r") as file:  
    creds = json.load(file)

# Instantiate an object
python_tweets = Twython(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])

# Create our query
query = {'q': 'learn python',  
        'result_type': 'popular',
        'count': 10,
        'lang': 'en',
        }

from twython import TwythonStreamer  
import csv

# Filter out unwanted data
def process_tweet(tweet):  
    d = {}
    d['hashtags'] = [hashtag['text'] for hashtag in tweet['entities']['hashtags']]
    d['text'] = tweet['text']
    d['user'] = tweet['user']['screen_name']
    d['user_loc'] = tweet['user']['location']
    return d


# Create a class that inherits TwythonStreamer
class MyStreamer(TwythonStreamer):     

    # Received data
    def on_success(self, data):

        # Only collect tweets in English
        if data['lang'] == 'en':
            tweet_data = process_tweet(data)
            self.save_to_csv(tweet_data)

    # Problem with the API
    def on_error(self, status_code, data):
        print(status_code, data)
        self.disconnect()

    # Save each tweet to csv file
    def save_to_csv(self, tweet):
        with open(r'saved_tweets.csv', 'a') as file:
            writer = csv.writer(file)
            writer.writerow(list(tweet.values()))

# Instantiate from our streaming class
stream = MyStreamer(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'],  
                    creds['ACCESS_TOKEN'], creds['ACCESS_SECRET'])
# Start the stream
stream.statuses.filter(track='python')


# ===========
import pandas as pd
tweets = pd.read_csv("saved_tweets.csv")  
tweets.head()

### Search tweets
##dict_ = {'user': [], 'date': [], 'text': [], 'favorite_count': []}  
##for status in python_tweets.search(**query)['statuses']:  
##    dict_['user'].append(status['user']['screen_name'])
##    dict_['date'].append(status['created_at'])
##    dict_['text'].append(status['text'])
##    dict_['favorite_count'].append(status['favorite_count'])
##
### Structure data in a pandas DataFrame for easier manipulation
##df = pd.DataFrame(dict_)  
##df.sort_values(by='favorite_count', inplace=True, ascending=False)  
##df.head(5)  

