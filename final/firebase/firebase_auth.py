import datetime
import os

import firebase_admin
from firebase_admin import credentials, firestore

# from final.tweet import Tweet


def get_db():
    firebase_json = f'{os.path.expanduser("~")}/credentials/firebase_auth.json'
    cred = credentials.Certificate(firebase_json)
    if len(firebase_admin._apps):
        return firebase_admin._apps['DEFAULT']
    default_app = firebase_admin.initialize_app(cred)
    return firestore.client()


if __name__ == '__main__':
    db = get_db()
    db2 = get_db()
    print('c')
    # tweet = Tweet({
    #     'id_str': 'abc123',
    #     'text': 'this my tweet',
    #     'user': {
    #         'screen_name': 'clark',
    #         'description': 'the coolest'
    #     },
    #     'hashtags': [
    #         {'text': 'lol'},
    #         {'text': 'iCanCount'},
    #     ],
    #     'created_at': 'January 6, 1991',
    #     'language': 'Python'
    # })
    document = db.collection('tweets').document('test')
    print('c')
