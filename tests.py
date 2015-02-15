import feedparser
from flask import url_for
from flask.ext.testing import TestCase

from app.factory import create_app


class TestMyView(TestCase):
    def create_app(self):
        return create_app()

    def test_home(self):
        r = self.client.get(url_for('.home'))
        self.assert200(r)

    def test_favicon(self):
        r = self.client.get(url_for('.favicon'), follow_redirects=True)
        self.assert200(r)
        self.assertEqual(r.content_type, 'image/vnd.microsoft.icon')

    def test_podcast_info(self):
        r = self.client.get(url_for('.podcast_info'))
        self.assert200(r)

    def test_rss(self):
        r = self.client.get(url_for('.podcast_feed'))
        self.assertEqual(r.content_type, 'application/rss+xml')
        feed = feedparser.parse(r.data)
        self.assertEqual(feed.encoding, 'utf-8')
        self.assertIn('image', feed.feed)
        msg = 'Bozo: {}'.format(feed.get('bozo_exception', 'no'))
        self.assertEqual(feed.bozo, 0, msg)
        self.assertGreater(len(feed.entries), 0)
        entry = feed.entries[0]
        self.assertNotEqual(entry.summary, '')
        self.assertNotEqual(entry.enclosures, [])
        self.assertIn('published', entry)
        self.assertIn('media_thumbnail', entry)
        self.assertIn('guid', entry)

    def test_episode(self):
        r = self.client.get(url_for('.view_episode', slug='blabla'))
        self.assert200(r)

    def test_download(self):
        r = self.client.get(url_for('.download_episode', slug='blabla'))
        self.assertEqual(r.status_code, 302)
