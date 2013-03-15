class Crawler(object):
    "Base crawler class."
    urls = []  # List of tuples with regular expression of URLs that the crawler handle

    def do(self, action, url):
        try:
            method = getattr(self, 'action_%s' % action)
            result = method(url)
            return result
        except AttributeError:
            raise CrawlerActionDoesNotExist('%s: action (%s) does not exist' % (self.__class__.__name__, action))
