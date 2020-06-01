import datetime
from dateutil import parser
from dataclasses import dataclass
from typing import List


@dataclass
class Tweet:
    id_str: str
    text: str
    date: datetime
    user_handle: str
    user_description: str
    hashtags: List[str]

    def __init__(self, data_from_twython, data_from_firestore=None):
        if data_from_twython:
            self.id_str = data_from_twython.get('id_str')
            self.text = data_from_twython.get('text')
            self.user_handle = data_from_twython.get('user', {}).get('screen_name')
            self.user_description = data_from_twython.get('user', {}).get('description')

            _hashtags = data_from_twython.get('entities', {}).get('hashtags', [])
            self.hashtags = []
            for h in _hashtags:
                self.hashtags.append(h.get('text'))

            self.date = parser.parse(data_from_twython.get('created_at'))

        if data_from_firestore:
            self.__dict__.update(data_from_firestore)