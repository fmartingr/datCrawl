import unittest
from datCrawl import *


class AwesomeGoogleCrawler(Crawler):
    urls = [
        ('es', 'http\:\/\/(www\.)?google\.es', ),
        ('de', 'http\:\/\/(www\.)?google\.de', )
    ]


class AwesomeEmptyCrawler(Crawler):
    pass


class AwesomeWikipediaTitleCrawler(Crawler):
    urls = [
        ('title', 'http\:\/\/en.wikipedia.org\/wiki\/(.*)', )
    ]

    def action_title(self, url):
        return {'title': 'Python'}


class datCrawlTests(unittest.TestCase):

    def test_instance_check(self):
        core = datCrawl()
        self.assertTrue(isinstance(core, datCrawl))

    def test_register_urls(self):
        core = datCrawl()
        data = ('action', 'http://www.google.es/', 'AwesomeGoogleCrawler')
        core.register_url(data[0], data[1], data[2])
        self.assertEquals(core.urls[0], data)

    def test_register_crawler_with_urls(self):
        core = datCrawl()
        core.register_crawler(AwesomeGoogleCrawler)
        self.assertEqual(core.crawlers['AwesomeGoogleCrawler'], AwesomeGoogleCrawler)
        # Some other checks if the tuple are well parsed, in order: action, url, crawler name
        self.assertEqual(core.urls[0][0], AwesomeGoogleCrawler().urls[0][1])
        self.assertEqual(core.urls[0][1], AwesomeGoogleCrawler().urls[0][0])
        self.assertEqual(core.urls[0][2], AwesomeGoogleCrawler().__class__.__name__)
        self.assertEqual(core.urls[1][0], AwesomeGoogleCrawler().urls[1][1])
        self.assertEqual(core.urls[1][1], AwesomeGoogleCrawler().urls[1][0])
        self.assertEqual(core.urls[1][2], AwesomeGoogleCrawler().__class__.__name__)

    def test_no_crawler_registered_for_url(self):
        core = datCrawl()
        core.register_crawler(AwesomeGoogleCrawler)
        self.assertEqual(core.crawlers['AwesomeGoogleCrawler'], AwesomeGoogleCrawler)
        self.assertRaises(CrawlerForThisURLNotFound, lambda: core.run('http://www.github.com'))

    def test_register_crawler_without_urls(self):
        core = datCrawl()
        self.assertRaises(CrawlerDontHaveUrlsToWatch, lambda: core.register_crawler(AwesomeEmptyCrawler))

    def test_register_incorrect_crawler(self):
        core = datCrawl()
        self.assertRaises(CrawlerIsNotInstanceOfBaseCrawler, lambda: core.register_crawler(object))

    def test_running_without_registered_crawlers(self):
        core = datCrawl()
        self.assertRaises(NoCrawlerRegistered, lambda: core.run('www.google.es'))

    def test_running_without_url_parameters(self):
        core = datCrawl()
        self.assertRaises(TypeError, lambda: core.run())

    def test_running_full_crawler(self):
        core = datCrawl()
        core.register_crawler(AwesomeWikipediaTitleCrawler)
        result = core.run('http://en.wikipedia.org/wiki/Python')
        self.assertEquals(result['title'], 'Python')

if __name__ == '__main__':
    unittest.main()
