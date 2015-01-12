import mixcloud
import sys
import textwrap
import requests

def main():
    m = mixcloud.Mixcloud()
    u = m.user('michelplatiniste')
    if len(sys.argv) == 2:
        slug = sys.argv[1]
        cloudcast = u.cloudcast(slug)
        print_yml(cloudcast)
    else:
        cloudcasts = u.cloudcasts(limit=50)
        for cloudcast in cloudcasts:
            print fmt(cloudcast)


def fmt(cc):
    stuff = [quote(cc.name),
             quote(cc.key),
             quote(cc.description()),
             repr(cc.created_time),
             ]
    fmt = "    Episode(" + "{},\n     " * len(stuff) + "),"
    return fmt.format(*stuff)


def print_yml(cc):
    print u'title: {}'.format(cc.name)
    desc_indent = '\n' + 6 * ' '
    desc = cc.description().replace('\r\n', desc_indent)
    fill_desc = desc_indent.join(textwrap.wrap(desc, replace_whitespace=False))
    print u'desc: {}'.format(fill_desc)
    print 'tags:'
    for tag in cc.tags:
        print '  - {}'.format(tag)
    print 'tracks:'
    for section in cc.sections():
        start = section.start_time
        minutes = start / 60
        seconds = start % 60
        print '  - start: {}:{:02}'.format(minutes, seconds)
        print '    artist: {}'.format(section.track.artist.name)
        print '    track: {}'.format(section.track.name)
    url = get_pic(cc)
    print 'meta:'
    print '    published: {}'.format(cc.created_time.isoformat())
    print '    pic: {}'.format(url)


def get_pic(cc):
    slug = cc.key
    url = 'https://api.mixcloud.com/michelplatiniste/' + slug
    cc_data = requests.get(url).json()
    return cc_data['pictures']['large']


def quote(s):
    return repr(s)


if __name__ == '__main__':
    main()
