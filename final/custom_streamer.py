from datetime import datetime, timedelta
from typing import List

from twython import TwythonStreamer

from register_twitter import RegisterTwitter
from tweet import Tweet


class CustomStreamer(TwythonStreamer):
    tweets: List[Tweet]
    end_time: datetime

    def __init__(self, minutes_to_listen: int = 1, seconds_to_listen: int = 0):
        super().__init__(*RegisterTwitter().credentials())
        self.end_time = datetime.now() + timedelta(minutes=minutes_to_listen, seconds=seconds_to_listen)
        self.tweets = []

    def on_success(self, data):
        if datetime.now() >= self.end_time:
            return self.disconnect()
        if data.get('lang', 'en') == 'en':
            self.tweets.append(Tweet(data))

    def on_error(self, status_code, data, headers=None):
        print(status_code, data)
        self.disconnect()


# if __name__ == '__main__':
#     tweet_dict = {}
#     languages = ('Rust', 'Python', 'WebAssembly')
#     twitterStreamer = CustomStreamer()
#     twitterStreamer.statuses.filter(track=','.join(languages))
