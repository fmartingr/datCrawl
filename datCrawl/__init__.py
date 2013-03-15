from datCrawl.exceptions import CrawlerDontHaveUrlsToWatch, \
    CrawlerIsNotInstanceOfBaseCrawler, CrawlerForThisURLNotFound, \
    NoCrawlerRegistered
from datCrawl.crawlers import Crawler
import re


class datCrawl(object):
    "Main class."

    def __init__(self):
        self.crawlers = {}
        self.urls = []

    def register_crawler(self, crawler):
        "Registers a crawler on the core to use in certain urls."
        class_name = crawler().__class__.__name__
        if isinstance(crawler(), Crawler):
            urls = crawler().urls
            if len(urls) > 0:
                [self.register_url(url, action, class_name) for action, url in urls]
                self.crawlers[class_name] = crawler
            else:
                raise CrawlerDontHaveUrlsToWatch('Crawler %s dont have URLs to watch for.' % class_name)
        else:
            raise CrawlerIsNotInstanceOfBaseCrawler('Crawler %s is not correctly created. (must be instance of base Crawler class)' % class_name)

    def register_url(self, url, action, crawler):
        "Registers a certain URL to work with a crawler"
        self.urls.append((url, action, crawler))

    def autoregister_crawlers():
        "Register all crawelers automagically."
        # TODO
        pass

    def run(self, url):
        if self.crawlers:
            for registered_url in self.urls:
                pattern = registered_url[0]
                regexp = re.compile(pattern)
                if regexp.match(url):
                    action = registered_url[1]
                    crawler = registered_url[2]
                    return self.crawlers[crawler]().do(action, url)
            raise CrawlerForThisURLNotFound("No crawler registered a URL pattern for: %s" % url)
        else:
            raise NoCrawlerRegistered("You must register a Crawler in order to do something.")
