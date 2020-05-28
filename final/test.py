import time
from typing import List, Tuple

from final.custom_streamer import CustomStreamer
from final.tweet import Tweet

twitterStreamer = CustomStreamer()
twitterStreamer.statuses.filter(track='WebAssembly')
t_end = time.time() + 10
while time.time() < t_end:
    print('time loop')
    continue

tweets: Tuple[Tweet] = twitterStreamer.disconnect()

print(tweets)
print('done')
