import tweepy
from tweepy import OAuthHandler
import google_api
 
consumer_key = 'consumer key'
consumer_secret = 'consumer secret'
access_token = 'access token'
access_secret = 'access secret'


def print_tweet(username,num):
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    api = tweepy.API(auth)

    tweets = api.user_timeline(screen_name=username,count=num)
    
    media_files = set()
    print('-----------------------------------------')
    print('Twitter Feeds')
    print('-----------------------------------------')
    
    d = 1
    for status in tweets:
        print(str(d) +'. ')
        print(status.text)
        media = status.entities.get('media', [])
        if(len(media) > 0):
            media_files.add(media[0]['media_url'])
        
        d+=1
    print('-----------------------------------------')
            
    print('Text Description of Images')
    print('-----------------------------------------')
    for media_url in media_files:
        print('Image url: '+ media_url)
        print('Description: ')
        google_api.google_image_detect(media_url)
    print('-----------------------------------------')
    