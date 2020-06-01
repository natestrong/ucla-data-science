import random
from typing import List, NamedTuple

from final.firebase import firebase_auth
from final.tweet import Tweet

if __name__ == '__main__':
    db = firebase_auth.get_db()
    python_tweets: List[Tweet] = []
    for doc in db.collection('tweets').where("language", "==", "Python").stream():
        _tweet: Tweet = Tweet(None, doc.to_dict())
        if not 'trump' in _tweet.text.lower():
            continue
        # Don't add to our list of tweets if it is a duplicate
        if not any(x for x in python_tweets if x.text == _tweet.text):
            python_tweets.append(_tweet)

    labelled_collection = db.collection('labelled_tweets')
    random.shuffle(python_tweets)

    print('Reply "y" if Tweet is about programming, "n" if not. Enter anything else to skip.')
    for _tweet in python_tweets:
        is_programming = input(f'{_tweet.text}\n')
        if is_programming == 'y':
            is_programming = True
        elif is_programming == "n":
            is_programming = False
        else:
            continue

        document = {
            'text': _tweet.text,
            'is_programming': is_programming
        }

        labelled_collection.document(_tweet.id_str).set(document)
