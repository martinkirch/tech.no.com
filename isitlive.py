import feedparser
import requests
import unittest


class TestLive(unittest.TestCase):

    def test_rss(self):
        url = 'http://tech.no.com/podcast.xml'
        f = feedparser.parse(url)
        self.assertEqual(f.bozo, 0)
        for e in f.entries:
            self.assertEqual(len(e.enclosures), 1)
            enclosure = e.enclosures[0]
            link = enclosure.href
            if link == 'http://tech.no.com/episode/2999-seconds/download':
                # Damn I lost it
                continue
            r = requests.head(link)
            self.assertTrue(r.is_redirect)
            redir_link = r.headers['location']
            r = requests.head(redir_link)
            self.assertEqual(r.status_code, 200, 'Status code for: ' + link)
            resp_bytes = r.headers['content-length']
            exp_bytes = enclosure.length
            msg = 'For {}: {} != {}'.format(link, resp_bytes, exp_bytes)
            self.assertEqual(resp_bytes, exp_bytes, msg)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
