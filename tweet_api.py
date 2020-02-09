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

    d = 1
    for status in tweets:
        print('-----------------------------------------')
        print('Twitter Feed ' + str(d))
        print('-----------------------------------------')

        print(status.text)
        media = status.entities.get('media', [])
        if(len(media) > 0):
            print('-----------------------------------------')
            media_files.add(media[0]['media_url'])
            print('Image url: '+ media[0]['media_url'])
            print()
            print('Description: ')
            google_api.google_image_detect(media[0]['media_url'])
        print('-----------------------------------------')

        
        d+=1

    
    return True
