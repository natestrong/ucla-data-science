import datetime
from dateutil import parser
from dataclasses import dataclass
from typing import List


@dataclass
class Tweet:
    text: str
    date: datetime
    user_handle: str
    user_description: str
    hashtags: List[str]

    def __init__(self, data_from_twython):
        self.text = data_from_twython.get('text')
        self.user_handle = data_from_twython.get('user', {}).get('screen_name')
        self.user_description = data_from_twython.get('user', {}).get('description')

        _hashtags = data_from_twython.get('hashtags', [])
        self.hashtags = []
        for h in _hashtags:
            self.hashtags.append(h.get('text'))

        self.date = parser.parse(data_from_twython.get('created_at'))
