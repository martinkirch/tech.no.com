import feedparser
from flask.ext.testing import TestCase

from app.factory import create_app
from app.views import home
#from app.views import view_rss


class TestMyView(TestCase):
    def create_app(self):
        return create_app()

    def test_home(self):
        r = self.client.get('/')
        self.assert200(r)

#    def test_rss(self):
#        request = testing.DummyRequest()
#        resp = view_rss(request)
#        self.assertEqual(resp.content_type, 'application/rss+xml')
#        feed = feedparser.parse(resp.body)
#        self.assertEqual(feed.encoding, 'utf-8')
#        self.assertIn('image', feed.feed)
#        msg = 'Bozo: {}'.format(feed.get('bozo_exception', 'no'))
#        self.assertEqual(feed.bozo, 0, msg)
#        self.assertGreater(len(feed.entries), 0)
#        entry = feed.entries[0]
#        self.assertNotEqual(entry.summary, '')
#        self.assertNotEqual(entry.enclosures, [])
#        self.assertIn('published', entry)
#        self.assertIn('media_thumbnail', entry)
#        self.assertIn('guid', entry)
#
#    def test_download(self):
#        from .views import view_download
#        request = testing.DummyRequest()
#        request.matchdict['slug'] = 'blabla'
#        resp = view_download(request)
#        self.assertEqual(resp.status_code, 302)
