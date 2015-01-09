"""
Hardcoded list of episodes.
A DB would be better, but hey.
"""

import datetime
import PyRSS2Gen
import os.path
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
        description += '\n\n' + render_tracklist(d['tracks'])
        pubDate = d['meta']['published']
        length = d['meta']['size']
        pic = d['meta']['pic']
        slug = os.path.splitext(os.path.basename(yml_file))[0]
        e = Episode(title, slug, description, pubDate, length, pic)
        return e


def render_tracklist(tracks):
    r = '<h3>Tracklist:</h3>'
    r += '<ul>'
    r += ''.join(['<li>{artist} - {track}</li>'.format(**track) for track in tracks])
    r += '</ul>'
    return r

def entries():
    ep_yml = ['episodes/the-pomodoro-sessions-episode-16.yml']
    episodes = [Episode.from_yml(f) for f in ep_yml] + EPISODES
    return [ep.to_rss_item() for ep in episodes]

EPISODES = [
    Episode(u'The Pomodoro Sessions - Episode 15',
     u'the-pomodoro-sessions-episode-15',
     u"The Pomodoro technique is a time management strategy in which you split tasks by 25 min intervals. As long as a mix from this series.\r\nLoad a Pomodoro Sessions episode, click play, work. When it's over, take a break! \r\n\r\nDon't drink too much coffee during this one.",
     datetime.datetime(2014, 11, 5, 22, 8, 42, tzinfo=tzutc()),
     37714646,
     u'http://images-mix.netdna-ssl.com/w/300/h/300/q/85/upload/images/extaudio/25287090-125c-4c25-bb0b-0366da9fe2b4.png',
     ),
    Episode(u'The Pomodoro Sessions - Episode 14',
     u'the-pomodoro-sessions-episode-14',
     u"The Pomodoro technique is a time management strategy in which you split tasks by 25 min intervals. As long as a mix from this series.\r\nLoad a Pomodoro Sessions episode, click play, work. When it's over, take a break! \r\n\r\nOccasionally Michel needs to get a fix of oppressive songs.",
     datetime.datetime(2014, 10, 20, 8, 26, 17, tzinfo=tzutc()),
     60910331,
     u'http://images-mix.netdna-ssl.com/w/300/h/300/q/85/upload/images/extaudio/846f1588-b2b9-4d31-83b1-33334e16838b.png',
     ),
    Episode(u'The Pomodoro Sessions - Episode 13',
     u'the-pomodoro-sessions-episode-13',
     u"The Pomodoro technique is a time management strategy in which you split tasks by 25 min intervals. As long as a mix from this series. \r\nLoad a Pomodoro Sessions episode, click play, work. When it's over, take a break!\r\n\r\nIn this episode, cold dub techno. I finished it with a lovely Moby remix which I hope you won't find out of place; I didn't.",
     datetime.datetime(2014, 5, 27, 7, 19, 23, tzinfo=tzutc()),
     29723904,
     u'http://images-mix.netdna-ssl.com/w/300/h/300/q/85/upload/images/extaudio/3bafe648-175a-46cf-b955-b63191df2060.png',
     ),
    Episode(u'The Pomodoro Sessions - Episode 12',
     u'the-pomodoro-sessions-episode-12',
     u"The Pomodoro technique is a time management strategy in which you split tasks by 25 min intervals. As long as a mix from this series.\r\nLoad a Pomodoro Sessions episode, click play, work. When it's over, take a break!\r\n\r\nThis episode, a few minimal and progressive tracks.",
     datetime.datetime(2014, 5, 20, 11, 40, 7, tzinfo=tzutc()),
     28018560,
     u'http://images-mix.netdna-ssl.com/w/300/h/300/q/85/upload/images/extaudio/db974d0d-7853-4ad4-be5e-018293eaa467.png',
     ),
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
    Episode(u'Sample & Funky',
     u'sample-funky',
     u'Artists love sampling other tracks. In this mix we jump from one track to another through a sample in common.',
     datetime.datetime(2013, 12, 3, 10, 20, 24, tzinfo=tzutc()),
     21660315,
     u'http://images-mix.netdna-ssl.com/w/300/h/300/q/85/upload/images/profile/17f0211d-20a1-417c-9901-4b2e6b4a4831.jpeg',
     ),
    Episode(u'The Pomodoro Sessions - Episode 9',
     u'the-pomodoro-sessions-episode-9',
     u'A progressive mix of long electronic tracks to accomodate with low temperatures and snowy weather, from ambient to techno.',
     datetime.datetime(2013, 11, 25, 15, 11, 45, tzinfo=tzutc()),
     59897729,
     u'http://images-mix.netdna-ssl.com/w/300/h/300/q/85/upload/images/extaudio/c9526b69-7091-4b15-af45-3b4347b93689.png',
     ),
    Episode(u'Voyage, voyages',
     u'voyage-voyages',
     u"A set for the tired lone traveller's headphones...",
     datetime.datetime(2013, 9, 30, 15, 1, 12, tzinfo=tzutc()),
     86278833,
     u'http://images-mix.netdna-ssl.com/w/300/h/300/q/85/upload/images/extaudio/30754347-93c2-47b0-b99a-610bc1a8f055.jpg',
     ),
    Episode(u'The Pomodoro Sessions - Episode 8',
     u'the-pomodoro-sessions-episode-8',
     u"The Pomodoro technique is a time management strategy in which you split tasks by 25 min intervals. As long as a mix from this series. \r\nLoad a Pomodoro Sessions episode, click play, work. When it's over, take a break!\r\n\r\nThis episodes marks the return of this mix series. Summer is over. Let's drown ourselves into a (small) ocean of deep dub techno. Don't forget to bring a towel!",
     datetime.datetime(2013, 9, 24, 8, 48, 14, tzinfo=tzutc()),
     24755328,
     u'http://images-mix.netdna-ssl.com/w/300/h/300/q/85/upload/images/extaudio/68461c3d-5666-460e-b8d8-af3225573d1a.png',
     ),
    Episode(u'The Pomodoro Sessions - Episode 7',
     u'the-pomodoro-sessions-episode-7',
     u"The Pomodoro technique is a time management strategy in which you split tasks by 25 min intervals. As long as a mix from this series. \r\nLoad a Pomodoro Sessions episode, click play, work. When it's over, take a break!\r\n\r\nThis episode is full of minimal techno, in an attempt to demonstrate that plic plic + pioup pioup = plic pioup plic pioup.",
     datetime.datetime(2013, 6, 6, 12, 55, 40, tzinfo=tzutc()),
     32264640,
     u'http://images-mix.netdna-ssl.com/w/300/h/300/q/85/upload/images/extaudio/22b2aa06-7056-4bd7-85f5-31895982f1bd.png',
     ),
    Episode(u'The Pomodoro Sessions - Episode 6',
     u'the-pomodoro-sessions-episode-6',
     u"The Pomodoro technique is a time management strategy in which you split tasks by 25 min intervals. As long as a mix from this series.\r\nLoad a Pomodoro Sessions episode, click play, work. When it's over, take a break!\r\n\r\nThis episode is TECH HOUSE TIME !",
     datetime.datetime(2013, 5, 27, 21, 59, 9, tzinfo=tzutc()),
     48783586,
     u'http://images-mix.netdna-ssl.com/w/300/h/300/q/85/upload/images/extaudio/2afc6d84-11a1-43b5-a7df-930a1823acf4.jpg',
     ),
    Episode(u'The Pomodoro Sessions - Episode 5',
     u'the-pomodoro-sessions-episode-5',
     u"The Pomodoro technique is a time management strategy in which you split tasks by 25 min intervals. As long as a mix from this series. \r\nLoad a Pomodoro Sessions episode, click play, work. When it's over, take a break!\r\n\r\nYou'll take a voyage to the biggest black-hole at the center of the galaxy. As you'll approach and traverse the singularity, time will stretch forever, but keep calm, it's all in your brain.",
     datetime.datetime(2013, 5, 20, 15, 59, 56, tzinfo=tzutc()),
     57525992,
     u'http://images-mix.netdna-ssl.com/w/300/h/300/q/85/upload/images/extaudio/a2679fad-11ac-47a0-8aba-14dc4b3504d6.png',
     ),
    Episode(u'The Pomodoro Sessions - Episode 4',
     u'the-pomodoro-sessions-episode-4',
     u"The Pomodoro technique is a time management strategy in which you split tasks by 25 min intervals. As long as a mix from this series.\r\nLoad a Pomodoro Sessions episode, click play, work. When it's over, take a break!\r\n\r\nThis episode ? It's made of deep and heavy techno !",
     datetime.datetime(2013, 5, 6, 7, 46, 28, tzinfo=tzutc()),
     49736330,
     u'http://images-mix.netdna-ssl.com/w/300/h/300/q/85/upload/images/extaudio/c03dfa13-845d-4b92-8a09-4d3b95107ee1.png',
     ),
    Episode(u'The Pomodoro Sessions - Episode 3',
     u'the-pomodoro-sessions-episode-3',
     u"The Pomodoro technique is a time management strategy in which you split tasks by 25 min intervals. As long as a mix from this series. \r\nLoad a Pomodoro Sessions episode, click play, work. When it's over, take a break!\r\n\r\nIn this episode we dive deep in a world of dark techno with a few latino tech house sounds.",
     datetime.datetime(2013, 4, 26, 9, 35, 50, tzinfo=tzutc()),
     24498816,
     u'http://images-mix.netdna-ssl.com/w/300/h/300/q/85/upload/images/extaudio/b2cefd0b-4fdf-4ef5-bef2-2965c9c5e642.png',
     ),
    Episode(u'The Pomodoro Sessions - Episode 2',
     u'the-pomodoro-sessions-episode-2',
     u"The Pomodoro technique is a time management strategy in which you split tasks by 25 min intervals. As long as a mix from this series.\r\nLoad a Pomodoro Sessions episode, click play, work. When it's over, take a break!\r\n\r\nThis episode will let you flow smoothly through your 25 minutes...",
     datetime.datetime(2013, 4, 25, 8, 17, 58, tzinfo=tzutc()),
     46068526,
     u'http://images-mix.netdna-ssl.com/w/300/h/300/q/85/upload/images/extaudio/58ebd413-907b-4725-a479-2a38d6ac5fc8.png',
     ),
    Episode(u'The Pomodoro Sessions - Episode 1',
     u'the-pomodoro-sessions-episode-1',
     u"The Pomodoro technique is a time management strategy in which you split tasks by 25 min intervals. As long as a mix from this series.\r\nLoad a Pomodoro Sessions episode, click play, work. When it's over, take a break!\r\n\r\nLather, rinse, repeat.\r\n\r\nhttp://en.wikipedia.org/wiki/Pomodoro_Technique",
     datetime.datetime(2013, 4, 24, 11, 52, 10, tzinfo=tzutc()),
     23695872,
     u'http://images-mix.netdna-ssl.com/w/300/h/300/q/85/upload/images/extaudio/ad19fa7d-8404-4eda-9c52-03ebbb7d92cd.png',
     ),
    Episode(u'Pile ou face',
     u'pile-ou-face',
     u"Pile c'est progressive. Face c'est minimale. Un mix en diptyque et en st\xe9r\xe9o.",
     datetime.datetime(2012, 12, 18, 11, 40, 50, tzinfo=tzutc()),
     57486720,
     u'http://images-mix.netdna-ssl.com/w/300/h/300/q/85/upload/images/extaudio/ee78622a-1557-4ef7-b392-4b35f87c9b75.jpg',
     ),
    Episode(u'Minimal sunday',
     u'minimal-sunday',
     u'',
     datetime.datetime(2012, 11, 19, 10, 28, 13, tzinfo=tzutc()),
     54653568,
     u'http://images-mix.netdna-ssl.com/w/300/h/300/q/85/upload/images/profile/17f0211d-20a1-417c-9901-4b2e6b4a4831.jpeg',
     ),
    Episode(u'Lunettes carr\xe9es, chemises \xe0 carreaux',
     u'lunettes-carrees-chemises-a-carreaux',
     u'On a tous un cot\xe9 hipster, aussi.\r\n\r\n\r\n<3\r\n\r\nMarty',
     datetime.datetime(2012, 11, 10, 13, 10, 56, tzinfo=tzutc()),
     84813360,
     u'http://images-mix.netdna-ssl.com/w/300/h/300/q/85/upload/images/extaudio/71eb50f4-79af-4b5b-b086-09f7ee8dffbc.jpg',
     ),
    Episode(u'Tokamix #2 - La Guerre contre les Machines',
     u'tokamix-2-la-guerre-contre-les-machines',
     u'Temp\xeate dans la nimposph\xe8re, les machines prennent le pouvoir et elles se servent de samplers radioactifs.',
     datetime.datetime(2012, 11, 6, 10, 17, 43, tzinfo=tzutc()),
     102189008,
     u'http://images-mix.netdna-ssl.com/w/300/h/300/q/85/upload/images/extaudio/b70ef5d4-e5da-4c9a-bb19-35d7758375c8.jpg',
     ),
    Episode(u'Warming up GreHack 2012',
     u'warming-up-grehack-2012',
     u"Played two hours during GreHack CTF's warm-up cocktail.\r\n\r\nhttp://grehack.org/",
     datetime.datetime(2012, 10, 21, 19, 17, 5, tzinfo=tzutc()),
     233538950,
     u'http://images-mix.netdna-ssl.com/w/300/h/300/q/85/upload/images/extaudio/ccd2b410-2b66-43c1-8c62-735acb70dc5a.png',
     ),
    Episode(u'Liqueur forte ou caf\xe9 noir',
     u'liqueur-forte-ou-cafe-noir',
     u"Let's make summer a bit longer with this short mix of '80s edits and reworks.",
     datetime.datetime(2012, 10, 10, 21, 31, 18, tzinfo=tzutc()),
     29255022,
     u'http://images-mix.netdna-ssl.com/w/300/h/300/q/85/upload/images/extaudio/360d835f-2ed2-4ba7-a1c3-54bd9e5288d8.png',
     ),
    Episode(u"Once you go in, you don't come out",
     u'once-you-go-in-you-dont-come-out',
     u'',
     datetime.datetime(2012, 9, 4, 9, 52, 13, tzinfo=tzutc()),
     54826080,
     u'http://images-mix.netdna-ssl.com/w/300/h/300/q/85/upload/images/extaudio/6a548efa-f5d4-444f-adc2-458f583e8f35.jpg',
     ),
    Episode(u"Tout le monde s'amuse \xe0 115BPM",
     u'tout-le-monde-samuse-a-115bpm',
     u"Tout le monde s'amuse, tout le monde boit des grands cocktails.\r\nTout le monde a du disco, tout le monde est smooth.\r\n\r\n115 BPM, le sweet spot entre le chill et le conformisme du dancefloor.\r\n\r\nEnjoy.",
     datetime.datetime(2012, 7, 10, 23, 46, 39, tzinfo=tzutc()),
     44971008,
     u'http://images-mix.netdna-ssl.com/w/300/h/300/q/85/upload/images/extaudio/c26bc6e5-2b46-4966-8ade-08474bc62d6b.jpg',
     ),
    Episode(u"Downpitch'd Summer",
     u'downpitchd-summer',
     u'Je sais pas vous, mais ici il fait chaud, lourd, orageux ... Alors ne d\xe9passons pas les 122BPM.\r\n\r\n<3\r\n\r\nMarty',
     datetime.datetime(2012, 7, 10, 22, 49, 52, tzinfo=tzutc()),
     106358467,
     u'http://images-mix.netdna-ssl.com/w/300/h/300/q/85/upload/images/extaudio/cafd601a-0ce0-48e6-b57e-1e3b4bc766ee.jpg',
     ),
    Episode(u'Ping pong - Minitex',
     u'ping-pong-minitex',
     u'',
     datetime.datetime(2012, 4, 6, 10, 13, 36, tzinfo=tzutc()),
     189446400,
     u'http://images-mix.netdna-ssl.com/w/300/h/300/q/85/upload/images/extaudio/f55c12e9-4e3f-4c8e-8938-39cd52026e7f.jpg',
     ),
    Episode(u'GroovyBaby',
     u'groovybaby',
     u'La p\xeache !\r\n\r\n\r\nMarty',
     datetime.datetime(2012, 3, 29, 23, 4, 22, tzinfo=tzutc()),
     79936817,
     u'http://images-mix.netdna-ssl.com/w/300/h/300/q/85/upload/images/extaudio/406f2050-257f-4987-b275-3d4279e3a8d3.jpg',
     ),
    Episode(u'Smooth',
     u'smooth',
     u"L'ami du petit d\xe9jeuner sonore, feat. Smoothie La Tr\xe8s Tr\xe8s Smooth.\r\n\r\nD\xe9sol\xe9 pour les deux lancements bizarres dans le dernier tiers, le matos se fait vieux.\r\n\r\n\r\n<3\r\n\r\nMarty",
     datetime.datetime(2012, 3, 20, 23, 3, 3, tzinfo=tzutc()),
     70748885,
     u'http://images-mix.netdna-ssl.com/w/300/h/300/q/85/upload/images/extaudio/d07ee824-f404-4c54-a721-5bd5027f41c3.png',
     ),
    Episode(u'Ode aux Nuits',
     u'ode-aux-nuits',
     u"Une s\xe9lection de la programmation de l'\xe9dition \xe9dition 2012 des Nuits Sonores .",
     datetime.datetime(2012, 3, 8, 10, 18, 50, tzinfo=tzutc()),
     105249600,
     u'http://images-mix.netdna-ssl.com/w/300/h/300/q/85/upload/images/extaudio/92b6b957-b2a8-4009-b2ae-341bfe267f23.jpg',
     ),
    Episode(u'Techno 06/2009',
     u'techno-062009',
     u'',
     datetime.datetime(2011, 12, 5, 14, 28, 27, tzinfo=tzutc()),
     35550467,
     u'http://images-mix.netdna-ssl.com/w/300/h/300/q/85/upload/images/extaudio/4598b3d0-1718-45f2-b68c-2e2b3354b188.jpg',
     ),
    Episode(u'Promo 02/2010',
     u'promo-022010',
     u'An "old" mix I found sitting between two mp3s \u263a',
     datetime.datetime(2011, 11, 17, 11, 49, 20, tzinfo=tzutc()),
     113860440,
     u'http://images-mix.netdna-ssl.com/w/300/h/300/q/85/upload/images/extaudio/1283a5f8-ce8b-4c0a-8c45-764143d7749d.jpg',
     ),
    Episode(u'2999 seconds',
     u'2999-seconds',
     u'2999 seconds of techno, old & new.',
     datetime.datetime(2011, 11, 15, 7, 55, 17, tzinfo=tzutc()),
     0,
     u'http://images-mix.netdna-ssl.com/w/300/h/300/q/85/upload/images/extaudio/347746e5-c524-4279-9b42-5fd9be23ce34.jpg',
     ),
    ]
