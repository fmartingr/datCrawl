from datCrawl.exceptions import CrawlerDontHaveUrlsToWatch, \
    CrawlerIsNotInstanceOfBase, CrawlerForThisURLNotFound, \
    NoCrawlerRegistered, CrawlerAlreadyRegistered, DownloaderAlreadyRegistered, \
    DownloaderIsNotInstanceOfBase, DownloaderIsNotRegistered, CrawlerUrlDontHaveGroupDefined
from datCrawl.crawlers import Crawler
from datCrawl.downloaders import Downloader
import re


class datCrawl(object):
    "Main class."

    def __init__(self):
        self.crawlers = {}
        self.downloaders = {}
        self.urls = []
        self.register_downloader(Downloader)

    def register_crawler(self, crawler):
        "Registers a crawler on the core to use in certain urls."
        class_name = crawler().__class__.__name__
        if class_name not in self.crawlers:
            if isinstance(crawler(), Crawler):
                urls = crawler().urls
                if len(urls) > 0:
                    downloader = crawler.downloader
                    if not self.downloader_is_registered(downloader):
                        raise DownloaderIsNotRegistered("Downloader %s is not registered. Register it before your crawler." % downloader)
                    else:
                        [self.register_url(url, action, class_name) for action, url in urls]
                        self.crawlers[class_name] = crawler
                else:
                    raise CrawlerDontHaveUrlsToWatch('Crawler %s dont have URLs to watch for.' % class_name)
            else:
                raise CrawlerIsNotInstanceOfBase('Crawler %s is not correctly created. (must be instance of base Crawler class)' % class_name)
        else:
            raise CrawlerAlreadyRegistered("Crawler %s is already registered." % class_name)

    def register_url(self, url, action, crawler):
        "Registers a certain URL to work with a crawler."
        self.urls.append((url, action, crawler))

    def autoregister_crawlers():
        "Register all crawelers automagically."
        # TODO
        pass

    def register_downloader(self, downloader):
        downloader_name = downloader().__class__.__name__
        if isinstance(downloader(), Downloader):
            if not self.downloader_is_registered(downloader_name):
                self.downloaders[downloader_name] = downloader
            else:
                raise DownloaderAlreadyRegistered("Downloader %s is already registered" % downloader_name)
        else:
            raise DownloaderIsNotInstanceOfBase('Downloader %s is not correctly created. (must be instance of base Downloader class)' % downloader_name)

    def downloader_is_registered(self, downloader_name):
        return downloader_name in self.downloaders

    def download(self, url, downloader, options=None):
        if self.downloader_is_registered(downloader):
            getter = self.downloaders[downloader]()
            data = getter.get(url, options=options)
            return data
        else:
            raise DownloaderIsNotRegistered("Downloader %s is not registered. Register it before your crawler." % downloader)

    def match(self, url):
        if self.crawlers:
            for registered_url in self.urls:
                pattern = registered_url[0]
                regexp = re.compile(pattern)
                matches = regexp.match(url)
                if matches:
                    crawler = registered_url[2]
                    try:
                        crawl_url = matches.group('url')
                    except IndexError:
                        raise CrawlerUrlDontHaveGroupDefined('The pattern [%s] of crawler [%s] dont have a url group defined.' % (pattern, crawler))
                    action = registered_url[1]
                    downloader = getattr(self.crawlers[crawler], 'downloader')
                    worker = datCrawlWorker(crawl_url, self.crawlers[crawler], action, self.downloaders[downloader], matches)
                    return worker
            raise CrawlerForThisURLNotFound("No crawler registered a URL pattern for: %s" % url)
        else:
            raise NoCrawlerRegistered("You must register a Crawler in order to do something.")

    def worker(self, url):
        worker = self.match(url)
        return worker

    def run(self, url):
        worker = self.match(url)
        return worker.run()


class datCrawlWorker(object):
    def __init__(self, url, crawler, action, downloader, matches):
        self.url = url
        self.crawler = crawler
        self.crawler_action = action
        self.downloader = downloader
        self.downloader_options = getattr(self.crawler, 'downloader_options')
        self.matches = matches
        self.data = None
        self.crawled_data = None

    def download(self):
        if self.downloader:
            getter = self.downloader()
            data = getter.get(self.url, options=self.downloader_options)
            self.data = data
        else:
            raise DownloaderIsNotRegistered("Downloader %s is not registered. Register it before your crawler." % self.downloader)

    def crawl(self):
        if self.data:
            self.crawled_data = self.crawler().do(self.crawler_action, self.data, matches=self.matches)

    def run(self):
        self.download()
        self.crawl()
        return self.crawled_data
