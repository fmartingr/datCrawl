class Crawler(object):
    "Base crawler class."
    urls = []  # List with regular expression of URLs that the crawler handle


class CrawlerIsNotInstanceOfBaseCrawler(Exception):
    "Class is not instance of the base crawler"
    pass


class CrawlerDontHaveUrlsToWatch(Exception):
    "Crawler class have the -urls- parameter empty"
    pass


class datCrawl(object):
    def __init__(self):
        self.crawlers = {}
        self.urls = []

    def register_crawler(self, crawler):
        "Registers a crawler on the core to use in certain urls"
        class_name = crawler().__class__.__name__
        if isinstance(crawler(), Crawler):
            urls = crawler().urls
            if len(urls) > 0:
                [self.register_url(url, class_name) for url in urls]
                self.crawlers[class_name] = crawler
            else:
                raise CrawlerDontHaveUrlsToWatch('Crawler %s dont have URLs to watch for.' % class_name)
        else:
            raise CrawlerIsNotInstanceOfBaseCrawler('Crawler %s is not correctly created. (must be instance of base Crawler class)' % class_name)

    def register_url(self, url, crawler):
        "Registers a certain URL to work with a crawler"
        self.urls.append((url, crawler))
