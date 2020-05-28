from datetime import datetime
from typing import Tuple, List

from twython import TwythonStreamer

from register_twitter import RegisterTwitter
from tweet import Tweet


class CustomStreamer(TwythonStreamer):
    tweets: List[Tweet] = []

    def __init__(self, minutes_to_listen: int = 1):
        super().__init__(*RegisterTwitter().credentials())

    def on_success(self, data):
        self.tweets.append(Tweet(data))

    def on_error(self, status_code, data, headers=None):
        print(status_code, data)
        self.connected = False

    def disconnect(self) -> Tuple[Tweet]:
        self.connected = False
        return tuple(self.tweets)
