def main():
    import mixcloud
    m = mixcloud.Mixcloud()
    michel = m.user('michelplatiniste')
    cloudcasts = michel.cloudcasts()
    for cloudcast in cloudcasts:
        print fmt(cloudcast)


def fmt(cc):
    return "    Episode({}, {}, {}),".format(quote(cc.name),
                                             quote(cc.key),
                                             quote(cc.description()),
                                             )


def quote(s):
    return repr(s)


if __name__ == '__main__':
    main()
