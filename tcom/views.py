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

conn_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to run the "initialize_tcom_db" script
    to initialize your database tables.  Check your virtual 
    environment's "bin" directory for this script and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""

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

@view_config(route_name='rssfeed')
def view_rss(request):
    rss = ItunesRSS(title='Michel Platiniste podcast',
                    link='http://tech.no.com',
                    description='The Michel Platiniste podcast',
                    items=tcom.episodes.entries(),
                    )
    resp = Response(rss.to_xml(encoding='utf-8'),
                    content_type='application/rss+xml')
    return resp

@view_config(route_name='download')
def view_download(request):
    slug = request.matchdict['slug']
    fmt = 'https://s3-eu-west-1.amazonaws.com/files.tech.no.com/podcasts/{}.mp3'
    url = fmt.format(slug)
    return HTTPFound(location=url)
