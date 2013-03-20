from datCrawl.exceptions import CrawlerActionDoesNotExist


class Crawler(object):
    "Base crawler class."
    urls = []  # List of tuples with regular expression of URLs that the crawler handle
    downloader = 'Downloader'  # Name of the downloader class to use
    downloader_options = None

    def do(self, action, data, **kwargs):
        try:
            method = getattr(self, 'action_%s' % action)
            result = method(data, **kwargs)
            return result
        except AttributeError as error:
            raise CrawlerActionDoesNotExist('%s: action (%s) does not exist: %s' % (self.__class__.__name__, action, error))
