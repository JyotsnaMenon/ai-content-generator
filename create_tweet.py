import pandas as pd
import json

from run_prompt import execute_gemini_for_tweet_creation

def top_5_selection(analyzed_tweets, engagement_type:str):
    df = pd.DataFrame(analyzed_tweets)
    filtered_df = df[df['engagement_type'] == engagement_type]
    return filtered_df.nlargest(5, columns=['engagement_score']).values.tolist()

def create_tweet(analyzed_tweets):
    prompt = """
                 Write a tweet for a new Offer sale announcement
                 with 50 percentage drop on fashion brands and
                 25 percentage discount on electronic gadgets.
                 Make the tweet more catchy for young adults. 
    """


    engagement_type = "like"

    top_5_tweets = top_5_selection(analyzed_tweets,engagement_type)
    
    system_prompt = f"""
                    Create an engaging twitter tweet for my E-commerce(B2C) company
                    PROMPT: {prompt}
                     
                    Here are some example tweets and their sentiment analysis
                    with very high user engagements of other similar companies.
                    Example Tweets: 
                    {top_5_tweets}

                    Create the tweet, compare it with the example tweets and
                    predict and explain why and how this tweet will perform
                    well comparing to the given examples. 
                    """
    
    out= execute_gemini_for_tweet_creation(
        prompt=system_prompt,
    )

    out_dict=json.loads(out)
    tweet=out_dict['tweet']
    prediction=out_dict['prediction']
    explanation = out_dict['explanation']
    print("TWEET ======>")
    print(tweet)
    print("PREDICTION ======>")
    print(prediction)
    print("EXPLANATION ======>")
    print(explanation)

with open("analyzed_tweets.json") as f:
    data = json.load(f)
    print("Tweets loaded", data)
    create_tweet(data)   
