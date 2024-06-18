import tweepy

# Define your credentials
bearer_token = 'YOUR_BEARER_TOKEN_HERE'

# Initialize client
client = tweepy.Client(bearer_token=bearer_token)

# Using Twitter API v2 to search tweets
query = 'Elon Musk -is:retweet'
tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at'], max_results=10)

for tweet in tweets.data:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
