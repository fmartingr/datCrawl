import unittest
from datCrawl import *


class AwesomeGoogleCrawler(Crawler):
    urls = [
        '(www\.)?google\.es',
        '(www\.)?google\.de'
    ]


class AwesomeEmptyCrawler(Crawler):
    pass


class datCrawlTests(unittest.TestCase):

    def test_instance_check(self):
        core = datCrawl()
        self.assertTrue(isinstance(core, datCrawl))

    def test_register_urls(self):
        core = datCrawl()
        data = ('http://www.google.es/', 'AwesomeGoogleCrawler')
        core.register_url(data[0], data[1])
        self.assertEquals(core.urls[0], data)

    def test_register_crawler_with_urls(self):
        core = datCrawl()
        core.register_crawler(AwesomeGoogleCrawler)
        self.assertEqual(core.crawlers['AwesomeGoogleCrawler'], AwesomeGoogleCrawler)
        self.assertEqual(core.urls[0][0], AwesomeGoogleCrawler().urls[0])
        self.assertEqual(core.urls[1][0], AwesomeGoogleCrawler().urls[1])

    def test_register_crawler_without_urls(self):
        core = datCrawl()
        self.assertRaises(CrawlerDontHaveUrlsToWatch, lambda: core.register_crawler(AwesomeEmptyCrawler))

    def test_register_incorrect_crawler(self):
        core = datCrawl()
        self.assertRaises(CrawlerIsNotInstanceOfBaseCrawler, lambda: core.register_crawler(object))


if __name__ == '__main__':
    unittest.main()
