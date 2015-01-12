"""
Hardcoded list of episodes.
A DB would be better, but hey.
"""

import datetime
import PyRSS2Gen
import os.path
import glob
import yaml
from dateutil.tz import tzutc


# Extracted from:
# https://github.com/DirkR/capturadio/blob/master/capturadio/rss.py
class ItunesRSSItem(PyRSS2Gen.RSSItem):

    def publish_extensions(self, handler):
        if self.image_url is not None:
            handler.startElement('media:thumbnail', {'url': self.image_url})
            handler.endElement('media:thumbnail')


class Episode:
    def __init__(self, title, slug, description, pubDate, length, pic):
        self.title = title
        self.slug = slug
        self.description = description
        self.pubDate = pubDate
        self.length = length
        self.pic = pic

    def to_rss_item(self):
        url = 'http://tech.no.com/episode/{}'.format(self.slug)
        item = ItunesRSSItem(
            title=self.title,
            description=self.description,
            enclosure=self.enclosure(),
            pubDate = self.pubDate,
            link = url,
            guid = PyRSS2Gen.Guid(url),
            )
        item.image_url = self.pic
        return item


    def enclosure(self):
        url = 'http://tech.no.com/episode/{}/download'.format(self.slug)
        return PyRSS2Gen.Enclosure(url, self.length, 'audio/mpeg')

    @staticmethod
    def from_yml(yml_file):
        with open(yml_file) as f:
            d = yaml.load(f)
        title = d['title']
        description = d['desc']
        if description is None:
            description = ''
        description += '\n\n' + render_tracklist(d['tracks'])
        pubDate = d['meta']['published']
        length = d['meta']['size']
        pic = d['meta']['pic']
        slug = os.path.splitext(os.path.basename(yml_file))[0]
        e = Episode(title, slug, description, pubDate, length, pic)
        return e


def render_tracklist(tracks):
    if tracks is None:
        return ''
    r = '<h3>Tracklist:</h3>'
    r += '<ul>'
    r += ''.join([u'<li>{artist} - {track}</li>'.format(**track) for track in tracks])
    r += '</ul>'
    return r

def entries():
    ep_yml = glob.glob('episodes/*.yml')
    episodes = [Episode.from_yml(f) for f in ep_yml] + EPISODES
    def date_of(ep):
        return ep.pubDate.date()
    episodes.sort(key=date_of, reverse=True)
    return [ep.to_rss_item() for ep in episodes]

EPISODES = [
    Episode(u'Just Drift',
     u'just-drift',
     u'I started deep in the spectrum of electronic music, with progressive house. My initial goal was to cut it to 25min to make a pomodoro mix but it was just too intense.\r\nI could not leave it there.\r\n\r\nI hope you will enjoy this mix as much as I enjoyed putting it together.\r\n\r\n\u2665\r\nE.',
     datetime.datetime(2014, 4, 28, 12, 41, 39, tzinfo=tzutc()),
     64490880,
     u'http://images-mix.netdna-ssl.com/w/300/h/300/q/85/upload/images/extaudio/34fd7667-1344-462e-8df3-2b33124dd839.jpg',
     ),
    Episode(u'Pas-modoro classique',
     u'pas-modoro-classique',
     u"Un pomodoro en forme de trait d'union entre la Renaissance et la musique classique contemporaine.",
     datetime.datetime(2014, 4, 24, 14, 5, 56, tzinfo=tzutc()),
     66767227,
     u'http://images-mix.netdna-ssl.com/w/300/h/300/q/85/upload/images/profile/17f0211d-20a1-417c-9901-4b2e6b4a4831.jpeg',
     ),
    Episode(u'The Pomodoro Sessions - Episode 11',
     u'the-pomodoro-sessions-episode-11',
     u'Upset => Techno\r\n\r\n\u2665 \r\n\r\nMichel',
     datetime.datetime(2014, 4, 15, 7, 20, 26, tzinfo=tzutc()),
     60004445,
     u'http://images-mix.netdna-ssl.com/w/300/h/300/q/85/upload/images/extaudio/336ad8a5-b4ff-4371-815c-ea3e4f81538b.png',
     ),
    Episode(u'The Pomodoro Sessions - Episode 10',
     u'the-pomodoro-sessions-episode-10',
     u'Spring => Tech house.\r\n\r\n\u2665\r\n\r\nMichel',
     datetime.datetime(2014, 4, 7, 8, 38, 3, tzinfo=tzutc()),
     60142611,
     u'http://images-mix.netdna-ssl.com/w/300/h/300/q/85/upload/images/extaudio/19b92597-f3b4-46df-a4cb-06281ee8c644.png',
     ),
    Episode(u'Voyage, Voyages, le retour',
     u'voyage-voyages-le-retour',
     u"Yet another set for the tired lone traveller's headphones\r\n\r\n\u2665 & \u266b ,\r\n\r\nMichel",
     datetime.datetime(2014, 3, 25, 8, 21, 13, tzinfo=tzutc()),
     138232859,
     u'http://images-mix.netdna-ssl.com/w/300/h/300/q/85/upload/images/extaudio/8d5f7979-7b29-467b-b289-c55462ca9729.jpg',
     ),
    ]
