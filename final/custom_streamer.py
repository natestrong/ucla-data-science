from datetime import datetime, timedelta
from typing import List

from twython import TwythonStreamer

from register_twitter import RegisterTwitter
from tweet import Tweet


class CustomStreamer(TwythonStreamer):
    tweets: List[Tweet] = []
    end_time: datetime

    def __init__(self, minutes_to_listen: int = 1):
        super().__init__(*RegisterTwitter().credentials())
        self.end_time = datetime.now() + timedelta(minutes=minutes_to_listen)

    def on_success(self, data):
        if datetime.now() >= self.end_time:
            return self.disconnect()
        self.tweets.append(Tweet(data))

    def on_error(self, status_code, data, headers=None):
        print(status_code, data)
        self.connected = False


if __name__ == '__main__':
    twitterStreamer = CustomStreamer(minutes_to_listen=1)
    twitterStreamer.statuses.filter(track='Python')
    tweets: List[Tweet] = twitterStreamer.tweets
    print('done')
