class Downloader(object):
    "Base downloader object"
    pass


class DefaultDownloader(Downloader):
    "Downloader using urllib2"

    def get(self, url):
        import urllib2
        try:
            req = urllib2.Request(url)
            response = urllib2.urlopen(req)
            data = response.read()
            return data
        except Exception, e:
            raise Exception(e)
