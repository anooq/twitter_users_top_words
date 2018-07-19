# twitter_users_top_words

A python script using nltk and scikit-learn libraries to get the term frequency of a twitter user.

- Given a twitter user name, this program would find which are the words used most frequently by this user, hence term frequency.

- Words are lemmatized using nltk WordNetLemmatizer, and english stop words

- Tweets are captured and written to tweets.txt

Usage:

- Create Twitter account and API access keys for application
- Store the keys in credentials.txt (assign appropriate values to oauth_token=, oauth_token_secret=,app_key=,app_secret=). Don't share these credentials!

- export TWITTER variable with the path of the Directory where credentials.txt is present
- run python twitter_top_words.py twitter_username max_tweets_to_search max_top_words_to_print lemmatize(optional)
