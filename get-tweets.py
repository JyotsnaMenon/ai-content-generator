import tweepy

from dotenv import load_dotenv
import os, tweepy

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET_KEY = os.getenv("API_SECRET_KEY")
BEARER_TOKEN = os.getenv("BEARER_TOKEN")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")


twitterClient = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    consumer_key=API_KEY,
    consumer_secret=API_SECRET_KEY,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET,
    wait_on_rate_limit=True,
)

user = twitterClient.get_user(username="sundarpichai")

print (user.data.id)

sundarpichai_id = user.data.id

# url --> https://x.com/sundarpichai
tweets = twitterClient.get_users_tweets(sundarpichai_id,max_results=5)

print(tweets.data)

