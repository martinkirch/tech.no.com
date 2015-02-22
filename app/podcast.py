"""
Get episodes from yml files.
"""

import datetime
import PyRSS2Gen
from dateutil.tz import tzutc
from episode import Episode


# Extracted from:
# https://github.com/DirkR/capturadio/blob/master/capturadio/rss.py
class ItunesRSSItem(PyRSS2Gen.RSSItem):

    def publish_extensions(self, handler):
        if self.image_url is not None:
            handler.startElement('media:thumbnail', {'url': self.image_url})
            handler.endElement('media:thumbnail')


class RSSEpisode(object):
    def __init__(self, ep):
        self.ep = ep

    def enclosure(self):
        url = 'http://tech.no.com/episode/{}/download'.format(self.ep.slug)
        return PyRSS2Gen.Enclosure(url, self.ep.length, 'audio/mpeg')

    def description(self):
        description = self.ep.description
        description += '\n\n' + self.render_tracklist()
        return description

    def to_rss_item(self):
        url = 'http://tech.no.com/episode/{}'.format(self.ep.slug)
        item = ItunesRSSItem(
            title=self.ep.title,
            description=self.description(),
            enclosure=self.enclosure(),
            pubDate=self.ep.pubDate,
            link=url,
            guid=PyRSS2Gen.Guid(url),
            )
        item.image_url = self.ep.pic
        return item

    def render_track(self, track):
        return u'<li>{artist} - {track}</li>'.format(**track)

    def render_tracklist(self):
        if self.ep.tracks is None:
            return ''
        r = '<h3>Tracklist:</h3>'
        r += '<ul>'
        r += ''.join([self.render_track(track) for track in self.ep.tracks])
        r += '</ul>'
        return r


def podcast_entries():
    episodes = Episode.all()

    def date_of(ep):
        return ep.pubDate.date()

    episodes.sort(key=date_of, reverse=True)
    return [RSSEpisode(ep).to_rss_item() for ep in episodes]
