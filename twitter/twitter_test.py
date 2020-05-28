#!/usr/bin/env python3
from dataclasses import asdict

from twython import TwythonStreamer

from twitter.register_twitter import RegisterTwitter


class MyStreamer(TwythonStreamer):
    tweets = []

    def __init__(self):
        super().__init__(*RegisterTwitter().credentials())

    def on_success(self, data):
        """
        What do we do when Twitter sends us data?
        Here data will be a Python dict representing a tweet.
        """
        # We only want to collect English-language tweets
        if data.get('lang') == 'en':
            self.tweets.append(data)
            print(f"received tweet #{len(self.tweets)}")
            print(data)

        # Stop when we've collected enough
        if len(self.tweets) >= 100:
            self.disconnect()

    def on_error(self, status_code, data, headers=None):
        print(status_code, data)


if __name__ == '__main__':
    twitter = MyStreamer()
    twitter.statuses.filter(track='data')
