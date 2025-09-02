import tweepy
import json

from dotenv import load_dotenv
import os, tweepy
#from run_prompt import execute_gemini

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET_KEY = os.getenv("API_SECRET_KEY")
BEARER_TOKEN = os.getenv("BEARER_TOKEN")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

if __name__ == "__main__":
        twitterClient = tweepy.Client(
            bearer_token=BEARER_TOKEN,
            access_token_secret=ACCESS_TOKEN_SECRET,
            consumer_key=API_KEY,
            consumer_secret=API_SECRET_KEY,
            access_token=ACCESS_TOKEN,
            wait_on_rate_limit=True,
        )

        user = twitterClient.get_user(username="amazon")
        

        user_id = user.data.id

        # print ("User:", user.data.name)

        #get tweets
        tweets = twitterClient.get_users_tweets(
                user_id,
                max_results=50,
                tweet_fields=['created_at', 'public_metrics', 'text']
                )

        #save the tweets to Json file
        with open("extracted_tweets.json", "w") as json_file:
                json.dump([tweet.data for tweet in tweets.data], json_file, indent=4)

                
 #   bearer_token=BEARER_TOKEN,
  #  consumer_key=API_KEY,
   # consumer_secret=API_SECRET_KEY,
#access_token=ACCESS_TOKEN,
 #   access_token_secret=ACCESS_TOKEN_SECRET,
 #   wait_on_rate_limit=True,)

#user = twitterClient.get_user(username="sundarpichai")

#print (user.data.id)

#sundarpichai_id = user.data.id

# url --> https://x.com/sundarpichai
#tweets = twitterClient.get_users_tweets(sundarpichai_id,max_results=5)

#print(tweets.data)