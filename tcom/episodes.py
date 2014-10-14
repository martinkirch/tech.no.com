"""
Hardcoded list of episodes.
A DB would be better, but hey.
"""

import PyRSS2Gen


class Episode:
    def __init__(self, title, description):
        self.title = title
        self.description = description

    def to_rss_item(self):
        item = PyRSS2Gen.RSSItem(
            title=self.title,
            description=self.description,
            )
        return item


def entries():
    return [ep.to_rss_item() for ep in EPISODES]


EPISODES = [
    Episode(u'The Pomodoro Sessions - Episode 13', u"The Pomodoro technique is a time management strategy in which you split tasks by 25 min intervals. As long as a mix from this series. \r\nLoad a Pomodoro Sessions episode, click play, work. When it's over, take a break!\r\n\r\nIn this episode, cold dub techno. I finished it with a lovely Moby remix which I hope you won't find out of place; I didn't."),
    Episode(u'The Pomodoro Sessions - Episode 12', u"The Pomodoro technique is a time management strategy in which you split tasks by 25 min intervals. As long as a mix from this series.\r\nLoad a Pomodoro Sessions episode, click play, work. When it's over, take a break!\r\n\r\nThis episode, a few minimal and progressive tracks."),
    Episode(u'Just Drift', u'I started deep in the spectrum of electronic music, with progressive house. My initial goal was to cut it to 25min to make a pomodoro mix but it was just too intense.\r\nI could not leave it there.\r\n\r\nI hope you will enjoy this mix as much as I enjoyed putting it together.\r\n\r\n\u2665\r\nE.'),
    Episode(u'Pas-modoro classique', u"Un pomodoro en forme de trait d'union entre la Renaissance et la musique classique contemporaine."),
    Episode(u'The Pomodoro Sessions - Episode 11', u'Upset => Techno\r\n\r\n\u2665 \r\n\r\nMichel'),
    Episode(u'The Pomodoro Sessions - Episode 10', u'Spring => Tech house.\r\n\r\n\u2665\r\n\r\nMichel'),
    Episode(u'Voyage, Voyages, le retour', u"Yet another set for the tired lone traveller's headphones\r\n\r\n\u2665 & \u266b ,\r\n\r\nMichel"),
    Episode(u'Sample & Funky', u'Artists love sampling other tracks. In this mix we jump from one track to another through a sample in common.'),
    Episode(u'The Pomodoro Sessions - Episode 9', u'A progressive mix of long electronic tracks to accomodate with low temperatures and snowy weather, from ambient to techno.'),
    Episode(u'Voyage, voyages', u"A set for the tired lone traveller's headphones..."),
    ]
