def main():
    import mixcloud
    m = mixcloud.Mixcloud()
    michel = m.user('michelplatiniste')
    cloudcasts = michel.cloudcasts(limit=50)
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


def quote(s):
    return repr(s)


if __name__ == '__main__':
    main()
