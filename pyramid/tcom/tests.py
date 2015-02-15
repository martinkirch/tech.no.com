import unittest
import transaction

from pyramid import testing

from .models import DBSession

class TestMyView(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        from sqlalchemy import create_engine
        engine = create_engine('sqlite://')
        from .models import (
            Base,
            MyModel,
            )
        DBSession.configure(bind=engine)
        Base.metadata.create_all(engine)
        with transaction.manager:
            model = MyModel(name='one', value=55)
            DBSession.add(model)

    def tearDown(self):
        DBSession.remove()
        testing.tearDown()

    def test_it(self):
        from .views import view_home
        request = testing.DummyRequest()
        info = view_home(request)
        self.assertEqual(info, {})

    def test_rss(self):
        import feedparser
        from .views import view_rss
        request = testing.DummyRequest()
        resp = view_rss(request)
        self.assertEqual(resp.content_type, 'application/rss+xml')
        feed = feedparser.parse(resp.body)
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

    def test_download(self):
        from .views import view_download
        request = testing.DummyRequest()
        request.matchdict['slug'] = 'blabla'
        resp = view_download(request)
        self.assertEqual(resp.status_code, 302)
