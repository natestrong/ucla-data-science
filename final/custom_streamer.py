from datetime import datetime, timedelta
from typing import List

from twython import TwythonStreamer

from final.register_twitter import RegisterTwitter
from final.tweet import Tweet


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
        print(data['text'])
        print('__________________________________________')
        self.tweets.append(Tweet(data))

    def on_error(self, status_code, data, headers=None):
        print(status_code, data)
        self.connected = False


if __name__ == '__main__':
    tweet_dict = {}
    for language in ('Rust', 'Python', 'WebAssembly'):
        print(f'~~~~ {language} ~~~~')
        twitterStreamer = CustomStreamer(minutes_to_listen=0, seconds_to_listen=30)
        twitterStreamer.statuses.filter(track=language)
        print(twitterStreamer.statuses.filter)
        tweet_dict[language] = twitterStreamer.tweets
    print('done')
