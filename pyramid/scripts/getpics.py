import requests


def main():
    url = 'https://api.mixcloud.com/michelplatiniste/cloudcasts'
    ccs = requests.get(url, params=dict(limit=50)).json()
    for cc in ccs['data']:
        slug = cc['slug']
        pic = cc['pictures']['large']
        print '    {}: {},'.format(repr(slug), repr(pic))


if __name__ == '__main__':
    main()
