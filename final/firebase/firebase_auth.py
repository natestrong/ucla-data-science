import datetime
import os
from collections import defaultdict
from typing import List, DefaultDict

import firebase_admin
from firebase_admin import credentials, firestore

# from final.tweet import Tweet
# from final.tweet import Tweet


def get_db():
    firebase_json = f'{os.path.expanduser("~")}/credentials/firebase_auth.json'
    cred = credentials.Certificate(firebase_json)
    c = firebase_admin
    if not firebase_admin._apps:
        default_app = firebase_admin.initialize_app(cred)
    return firestore.client()


if __name__ == '__main__':
    db = get_db()
    # tweets_dict: DefaultDict[str, List[Tweet]] = defaultdict(list)
    # tweets_collection = db.collection('tweets').stream()
    # for doc in tweets_collection:
    #     _tweet = Tweet(None, doc.to_dict())
    #     tweets_dict[doc.get('language')].append(_tweet)

    test_collection = tweets_collection = db.collection('test')
    batch = db.batch()
    for x in range(1, 502):
        _document = {'name': x, 'squared': x * x}
        batch.set(test_collection.document(str(_document['name'])), _document)
        print('c')
    batch.commit()
    print('c')
