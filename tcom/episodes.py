"""
Hardcoded list of episodes.
A DB would be better, but hey.
"""

import PyRSS2Gen


class Episode:
    def __init__(self, title, slug, description):
        self.title = title
        self.slug = slug
        self.description = description

    def to_rss_item(self):
        item = PyRSS2Gen.RSSItem(
            title=self.title,
            description=self.description,
            enclosure=make_enclosure(self.slug),
            )
        return item


def make_enclosure(slug):
    url = 'http://tech.no.com/episode/{}/download'.format(slug)
    return PyRSS2Gen.Enclosure(url, enclosure_length(slug), 'audio/mpeg')


def enclosure_length(slug):
    return 0


def entries():
    return [ep.to_rss_item() for ep in EPISODES]


EPISODES = [
    Episode(u'The Pomodoro Sessions - Episode 13', u'the-pomodoro-sessions-episode-13', u"The Pomodoro technique is a time management strategy in which you split tasks by 25 min intervals. As long as a mix from this series. \r\nLoad a Pomodoro Sessions episode, click play, work. When it's over, take a break!\r\n\r\nIn this episode, cold dub techno. I finished it with a lovely Moby remix which I hope you won't find out of place; I didn't."),
    Episode(u'The Pomodoro Sessions - Episode 12', u'the-pomodoro-sessions-episode-12', u"The Pomodoro technique is a time management strategy in which you split tasks by 25 min intervals. As long as a mix from this series.\r\nLoad a Pomodoro Sessions episode, click play, work. When it's over, take a break!\r\n\r\nThis episode, a few minimal and progressive tracks."),
    Episode(u'Just Drift', u'just-drift', u'I started deep in the spectrum of electronic music, with progressive house. My initial goal was to cut it to 25min to make a pomodoro mix but it was just too intense.\r\nI could not leave it there.\r\n\r\nI hope you will enjoy this mix as much as I enjoyed putting it together.\r\n\r\n\u2665\r\nE.'),
    Episode(u'Pas-modoro classique', u'pas-modoro-classique', u"Un pomodoro en forme de trait d'union entre la Renaissance et la musique classique contemporaine."),
    Episode(u'The Pomodoro Sessions - Episode 11', u'the-pomodoro-sessions-episode-11', u'Upset => Techno\r\n\r\n\u2665 \r\n\r\nMichel'),
    Episode(u'The Pomodoro Sessions - Episode 10', u'the-pomodoro-sessions-episode-10', u'Spring => Tech house.\r\n\r\n\u2665\r\n\r\nMichel'),
    Episode(u'Voyage, Voyages, le retour', u'voyage-voyages-le-retour', u"Yet another set for the tired lone traveller's headphones\r\n\r\n\u2665 & \u266b ,\r\n\r\nMichel"),
    Episode(u'Sample & Funky', u'sample-funky', u'Artists love sampling other tracks. In this mix we jump from one track to another through a sample in common.'),
    Episode(u'The Pomodoro Sessions - Episode 9', u'the-pomodoro-sessions-episode-9', u'A progressive mix of long electronic tracks to accomodate with low temperatures and snowy weather, from ambient to techno.'),
    Episode(u'Voyage, voyages', u'voyage-voyages', u"A set for the tired lone traveller's headphones..."),
    Episode(u'The Pomodoro Sessions - Episode 8', u'the-pomodoro-sessions-episode-8', u"The Pomodoro technique is a time management strategy in which you split tasks by 25 min intervals. As long as a mix from this series. \r\nLoad a Pomodoro Sessions episode, click play, work. When it's over, take a break!\r\n\r\nThis episodes marks the return of this mix series. Summer is over. Let's drown ourselves into a (small) ocean of deep dub techno. Don't forget to bring a towel!"),
    Episode(u'The Pomodoro Sessions - Episode 7', u'the-pomodoro-sessions-episode-7', u"The Pomodoro technique is a time management strategy in which you split tasks by 25 min intervals. As long as a mix from this series. \r\nLoad a Pomodoro Sessions episode, click play, work. When it's over, take a break!\r\n\r\nThis episode is full of minimal techno, in an attempt to demonstrate that plic plic + pioup pioup = plic pioup plic pioup."),
    Episode(u'The Pomodoro Sessions - Episode 6', u'the-pomodoro-sessions-episode-6', u"The Pomodoro technique is a time management strategy in which you split tasks by 25 min intervals. As long as a mix from this series.\r\nLoad a Pomodoro Sessions episode, click play, work. When it's over, take a break!\r\n\r\nThis episode is TECH HOUSE TIME !"),
    Episode(u'The Pomodoro Sessions - Episode 5', u'the-pomodoro-sessions-episode-5', u"The Pomodoro technique is a time management strategy in which you split tasks by 25 min intervals. As long as a mix from this series. \r\nLoad a Pomodoro Sessions episode, click play, work. When it's over, take a break!\r\n\r\nYou'll take a voyage to the biggest black-hole at the center of the galaxy. As you'll approach and traverse the singularity, time will stretch forever, but keep calm, it's all in your brain."),
    Episode(u'The Pomodoro Sessions - Episode 4', u'the-pomodoro-sessions-episode-4', u"The Pomodoro technique is a time management strategy in which you split tasks by 25 min intervals. As long as a mix from this series.\r\nLoad a Pomodoro Sessions episode, click play, work. When it's over, take a break!\r\n\r\nThis episode ? It's made of deep and heavy techno !"),
    Episode(u'The Pomodoro Sessions - Episode 3', u'the-pomodoro-sessions-episode-3', u"The Pomodoro technique is a time management strategy in which you split tasks by 25 min intervals. As long as a mix from this series. \r\nLoad a Pomodoro Sessions episode, click play, work. When it's over, take a break!\r\n\r\nIn this episode we dive deep in a world of dark techno with a few latino tech house sounds."),
    Episode(u'The Pomodoro Sessions - Episode 2', u'the-pomodoro-sessions-episode-2', u"The Pomodoro technique is a time management strategy in which you split tasks by 25 min intervals. As long as a mix from this series.\r\nLoad a Pomodoro Sessions episode, click play, work. When it's over, take a break!\r\n\r\nThis episode will let you flow smoothly through your 25 minutes..."),
    Episode(u'The Pomodoro Sessions - Episode 1', u'the-pomodoro-sessions-episode-1', u"The Pomodoro technique is a time management strategy in which you split tasks by 25 min intervals. As long as a mix from this series.\r\nLoad a Pomodoro Sessions episode, click play, work. When it's over, take a break!\r\n\r\nLather, rinse, repeat.\r\n\r\nhttp://en.wikipedia.org/wiki/Pomodoro_Technique"),
    Episode(u'Pile ou face', u'pile-ou-face', u"Pile c'est progressive. Face c'est minimale. Un mix en diptyque et en st\xe9r\xe9o."),
    Episode(u'Minimal sunday', u'minimal-sunday', u''),
    ]
