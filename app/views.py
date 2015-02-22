from flask import Blueprint
from flask import redirect
from flask import render_template
from flask import Response
from flask import url_for

from episode import Episode

tcom = Blueprint('tcom', __name__)


@tcom.route('/')
def home():
    episodes = Episode.all()
    return render_template('home.html', episodes=episodes)


@tcom.route('/favicon.ico')
def favicon():
    return redirect(url_for('static', filename='favicon.ico'))


@tcom.route('/podcast')
def podcast_info():
    return render_template('podcast.html')


@tcom.route('/podcast.xml')
def podcast_feed():
    episodes = Episode.all()
    resp = Response(render_template('feed.xml', episodes=episodes),
                    content_type='application/rss+xml')
    return resp


@tcom.route('/episode/<slug>')
def view_episode(slug):
    return render_template('episode.html', slug=slug)


@tcom.route('/episode/<slug>/download')
def download_episode(slug):
    bucket = 'files.tech.no.com'
    fmt = 'https://s3-eu-west-1.amazonaws.com/{}/podcasts/{}.mp3'
    url = fmt.format(bucket, slug)
    return redirect(url)
