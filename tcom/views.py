from pyramid.response import Response
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    MyModel,
    )

import PyRSS2Gen

import tcom.episodes

@view_config(route_name='home', renderer='home.mako')
def view_home(request):
    return {}

@view_config(route_name='episode', renderer='episode.mako')
def view_episode(request):
    slug = request.matchdict['slug']
    return dict(slug=slug)


# Extracted from:
# https://github.com/DirkR/capturadio/blob/master/capturadio/rss.py
class ItunesRSS(PyRSS2Gen.RSS2):
    """This class adds the "itunes" extension (<itunes:image>, etc.)
    to the rss feed."""

    rss_attrs = {
        "xmlns:itunes": "http://www.itunes.com/dtds/podcast-1.0.dtd",
        "xmlns:media": "http://search.yahoo.com/mrss/",
        "version": "2.0",
    }

    def publish_extensions(self, handler):
        # implement this method to embed the <itunes:*> elements
        # into the channel header.
        if self.image_url is not None:
            handler.startElement('itunes:image', {'href': self.image_url})
            handler.endElement('itunes:image')

@view_config(route_name='rssfeed')
def view_rss(request):
    rss = ItunesRSS(title='Michel Platiniste podcast',
                    link='http://tech.no.com',
                    description='The Michel Platiniste podcast',
                    items=tcom.episodes.entries(),
                    )
    rss.image_url = 'http://images-mix.netdna-ssl.com/w/300/h/300/q/85/upload/images/profile/17f0211d-20a1-417c-9901-4b2e6b4a4831.jpeg'
    resp = Response(rss.to_xml(encoding='utf-8'),
                    content_type='application/rss+xml')
    return resp

@view_config(route_name='download')
def view_download(request):
    slug = request.matchdict['slug']
    fmt = 'https://s3-eu-west-1.amazonaws.com/files.tech.no.com/podcasts/{}.mp3'
    url = fmt.format(slug)
    return HTTPFound(location=url)

@view_config(route_name='podcast', renderer='podcast.mako')
def view_podcast(request):
    return {}
