class Downloader(object):
    "Base downloader object"
    def get(self, url):
        print("I'm a useless downloader :_")


class DefaultDownloader(Downloader):
    "Downloader using urllib2"

    def get(self, url):
        import urllib2
        try:
            req = urllib2.Request(url)
            response = urllib2.urlopen(req)
            data = response.read()
            return data
        except Exception as error:
            raise Exception("Error downloading %s: %s" % (url, error))
