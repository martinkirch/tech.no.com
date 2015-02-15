"""
Get episodes from yml files.
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
            pubDate=self.pubDate,
            link=url,
            guid=PyRSS2Gen.Guid(url),
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


def render_track(track):
    return u'<li>{artist} - {track}</li>'.format(**track)


def render_tracklist(tracks):
    if tracks is None:
        return ''
    r = '<h3>Tracklist:</h3>'
    r += '<ul>'
    r += ''.join([render_track(track) for track in tracks])
    r += '</ul>'
    return r


def podcast_entries():
    this_dir = os.path.dirname(os.path.abspath(__file__))
    ep_yml = glob.glob(os.path.join(this_dir, '..', 'episodes/*.yml'))
    episodes = [Episode.from_yml(f) for f in ep_yml]

    def date_of(ep):
        return ep.pubDate.date()

    episodes.sort(key=date_of, reverse=True)
    return [ep.to_rss_item() for ep in episodes]
