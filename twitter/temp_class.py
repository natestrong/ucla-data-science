import math
from collections import defaultdict

class NaiveBayesClassifier:
    def __init__(self, smoothing: float = 0.5):
        self.smoothing = smoothing
        self.tokens: Set[str] = set()
        self.token_not_programming_counts: Dict[str, int] = defaultdict(int)
        self.token_is_programming_counts: Dict[str, int] = defaultdict(int)
        self.not_programming_tweets = self.is_programming_tweets = 0

    def train(self, labeled_tweets:List[LabeledTweet]) -> None:
        for _labeled_tweet in labeled_tweets:
            if not _labeled_tweet.is_programming:
                self.not_programming_tweets += 1
            else:
                self.is_programming_tweets += 1

        for token in tokenize(_labeled_tweet.text):
            self.tokens.add(token)
            if not _labeled_tweet.is_programming:
                self.token_not_programming_counts[token] += 1
            else:
                self.token_is_programming_counts[token] += 1

    def _probabilities(self, token:str) -> Tuple[float, float]:
        """Returns P(token | not_programming) and P(token | is_programming)"""
        not_programming = self.token_not_programming_counts[token]
        is_programming = self.token_is_programming_counts[token]

        p_token_not_programming = (not_programming + self.smoothing) / (self.not_programming_tweets + 2 * self.smoothing)
        p_token_is_programming = (is_programming + self.smoothing) / (self.is_programming_tweets + 2 * self.smoothing)

        return p_token_not_programming, p_token_is_programming

    def predict(self, text:str) -> float:
        text_tokens = tokenize(text)
        log_prob_not_programming = log_prob_is_programming = 0

        # Loop through all of the words
        for token in self.tokens:
            prob_not_programming, prob_is_programming = self._probabilities(token)
            if token in text_tokens:
                log_prob_not_programming += math.log(prob_not_programming)
                log_prob_is_programming += math.log(prob_is_programming)
            else:
                log_prob_not_programming += math.log(1.0 - prob_not_programming)
                log_prob_is_programming += math.log(1.0 - prob_is_programming)

        prob_not_programming = math.exp(log_prob_not_programming)
        prob_is_programming = math.exp(log_prob_is_programming)

        return prob_not_programming / prob_is_programming