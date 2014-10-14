"""
Hardcoded list of episodes.
A DB would be better, but hey.
"""

import PyRSS2Gen


class Episode:
    def __init__(self, title):
        self.title = title

    def to_rss_item(self):
        item = PyRSS2Gen.RSSItem(
            title=self.title,
            )
        return item


def entries():
    return [ep.to_rss_item() for ep in EPISODES]


EPISODES = [
    Episode("The Pomodoro Sessions - Episode 13"),
    ]
