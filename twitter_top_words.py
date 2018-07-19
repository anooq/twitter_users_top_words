from nltk.twitter import Query, credsfromfile, TweetViewer
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
import sys

if (len(sys.argv)<4):
    print ('Usage:', sys.argv[0], ' twitter_username max_tweets_to_search max_top_words_to_print lemmatize(optional)' )
    quit()

#capture the output of tweetViewer to file for processing
sys.stdout = open('tweets.txt', 'w')

oauth = credsfromfile()
client = Query(**oauth)
client.register(TweetViewer(limit=sys.argv[2]))
client.user_tweets(sys.argv[1], sys.argv[2])


#give back control to stdout
sys.stdout = sys.__stdout__
lemmatizer = WordNetLemmatizer()

if (len(sys.argv)>4 and sys.argv[4].lower()=='lemmatize'):
    lemmatize=True
else:
    lemmatize=False


def text_cleaner(documents):
    text_cleaned = []
    for document in documents:
        text_cleaned.append(' '.join([lemmatizer.lemmatize(word.lower()) if (lemmatize) else word for word in document.split() if word.isalpha()]))
    return text_cleaned

text = []
with open ('tweets.txt') as fin:
    text.append(fin.read())

text_cleaned = text_cleaner(text)

cv = CountVectorizer(stop_words='english', max_features=int(sys.argv[3]))

fit_term_documents = cv.fit_transform(text_cleaned)

feature_names = cv.get_feature_names()

features_frequency=[(x,y) for (y,x) in sorted(zip(fit_term_documents.toarray().sum(axis=0),feature_names), key=lambda pair: pair[0], reverse=True)]

print (features_frequency)
