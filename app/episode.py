import email.utils
import glob
import os.path
import time
import yaml

from flask import url_for


class Episode:
    def __init__(self, title, slug, description, pubDate, length, pic, tracks):
        self.title = title
        self.slug = slug
        self.description = description
        self.pubDate = pubDate
        self.length = length
        self.pic = pic
        self.tracks = tracks

    @staticmethod
    def from_yml(yml_file):
        with open(yml_file) as f:
            d = yaml.load(f)
        title = d['title']
        description = d['desc']
        if description is None:
            description = ''
        tracks = d['tracks']
        if 'meta' not in d:
            return
        pubDate = d['meta']['published']
        length = d['meta']['size']
        pic = d['meta']['pic']
        slug = os.path.splitext(os.path.basename(yml_file))[0]
        e = Episode(title, slug, description, pubDate, length, pic, tracks)
        return e

    @staticmethod
    def all():
        this_dir = os.path.dirname(os.path.abspath(__file__))
        ep_yml = glob.glob(os.path.join(this_dir, '..', 'episodes/*.yml'))
        episodes = []
        for f in ep_yml:
            episode = Episode.from_yml(f)
            if episode is not None:
                episodes.append(episode)
        return sorted(episodes, key=lambda x: x.pubDate, reverse=True)

    def url(self):
        return url_for('.view_episode', slug=self.slug)

    def rfc822date(self):
        timetuple = self.pubDate.timetuple()
        timestamp = time.mktime(timetuple)
        return email.utils.formatdate(timestamp)
