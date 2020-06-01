from typing import NamedTuple


class LabeledTweet(NamedTuple):
    text: str
    is_programming: bool
