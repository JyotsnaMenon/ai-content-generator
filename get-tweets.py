import tweepy

API_KEY = "yjpvrQnmtJbJWjmLz5WZQu5ip"
API_SECRET_KEY = "UDTCOzYqTTeBSfhCTkosqg4dSvV5hQ7q5c1O1T8zl1dLwnioNp"
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAALaM3gEAAAAAss17uTZygQ0YeuFus%2FaUTafABwc%3DXVmcUjfAvkhhPnM5M9cYVnwISsv2arXFTLyLgc4wk4dXEMzHfi"
ACCESS_TOKEN = "1957418500160651264-KqrvEZVnQYinwbxwL4yA5NqVugBxX6"
ACCESS_TOKEN_SECRET = "nzZDHmnfOTReZY187BiVhcUWshzUSp9asRdadgIzEEQOT"


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