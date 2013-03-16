from datCrawl.exceptions import CrawlerActionDoesNotExist


class Crawler(object):
    "Base crawler class."
    urls = []  # List of tuples with regular expression of URLs that the crawler handle
    downloader = 'Downloader'  # Name of the downloader class to use

    def do(self, action, data):
        try:
            method = getattr(self, 'action_%s' % action)
            result = method(data)
            return result
        except AttributeError:
            raise CrawlerActionDoesNotExist('%s: action (%s) does not exist' % (self.__class__.__name__, action))
