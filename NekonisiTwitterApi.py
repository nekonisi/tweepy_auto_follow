# coding: utf-8
import configparser, tweepy, os.path
class NekonisiTwitterApi:
    """wrapper class of tweepy
     About tweepy see following URL
     https://docs.tweepy.org/en/stable/"""

    def __init__(self):
        """Constructor"""
        config = configparser.RawConfigParser()
        config_path = os.path.join(os.path.dirname(__file__), 'config.ini')
        config.read(config_path, encoding='utf-8')
        consumer_key = config.get('CONFIG', 'consumer_key')
        consumer_secret = config.get('CONFIG', 'consumer_secret')
        access_token = config.get('CONFIG', 'access_token')
        access_token_secret = config.get('CONFIG', 'access_token_secret')
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)
        self.client = tweepy.Client(consumer_key=consumer_key, 
                        consumer_secret=consumer_secret,
                        access_token=access_token,
                        access_token_secret=access_token_secret)
        self.me = self.client.get_me()

    def auto_follow(self, keyword):
        """Auto folllow users with keyword

        Args:
            keyword (string): keyword for search
        """
        results = self.api.search_tweets(keyword)
        for result in results:
            user = result.user
            friendship = self.api.get_friendship(source_id = self.me.data.id, target_id = user.id)
            if friendship[0].following == False:
                self.api.create_friendship(user_id = user.id)
    
    def auto_unfollow(self):
        """Auto unfollow users
        Goodbye! unrequited love!
        """
        for friend_id in self.api.get_friend_ids():
            friendship = self.api.get_friendship(source_id = self.me.data.id, target_id = friend_id)
            if friendship[0].followed_by == False:
                self.api.destroy_friendship(user_id = friend_id)