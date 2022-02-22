# coding: utf-8
import configparser, tweepy, time, sys

def main():
    init()
    api = get_api()
    client = get_client()
    me = client.get_me()
    keyword = sys.argv[1]
    results = api.search_tweets(keyword)
    for result in results:
        user = result.user
        friendship = api.get_friendship(source_id = me.data.id, target_id = user.id)
        if friendship[0].following == False:
            api.create_friendship(user_id = user.id)


def init():
    global consumer_key
    global consumer_secret
    global access_token
    global access_token_secret
    config = configparser.RawConfigParser()
    config.read('config.ini', encoding='utf-8')
    consumer_key = config.get('CONFIG', 'consumer_key')
    consumer_secret = config.get('CONFIG', 'consumer_secret')
    access_token = config.get('CONFIG', 'access_token')
    access_token_secret = config.get('CONFIG', 'access_token_secret')

def get_api():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return tweepy.API(auth)

def get_client():
    return tweepy.Client(consumer_key=consumer_key, 
                         consumer_secret=consumer_secret,
                         access_token=access_token,
                         access_token_secret=access_token_secret)

if __name__ == "__main__":
    main()