import unittest
from datCrawl import *
from test.requirements import *


class datCrawlCrawlerTests(unittest.TestCase):
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

    def test_register_incorrect_crawler(self):
        core = datCrawl()
        self.assertRaises(CrawlerIsNotInstanceOfBase, lambda: core.register_crawler(object))

    def test_cant_register_crawler_twice(self):
        core = datCrawl()
        core.register_crawler(AwesomeGoogleCrawler)
        self.assertRaises(CrawlerAlreadyRegistered, lambda: core.register_crawler(AwesomeGoogleCrawler))

    def test_no_crawler_registered_for_url(self):
        core = datCrawl()
        core.register_crawler(AwesomeGoogleCrawler)
        self.assertEqual(core.crawlers['AwesomeGoogleCrawler'], AwesomeGoogleCrawler)
        self.assertRaises(CrawlerForThisURLNotFound, lambda: core.run('http://www.github.com'))

    def test_register_crawler_without_urls(self):
        core = datCrawl()
        self.assertRaises(CrawlerDontHaveUrlsToWatch, lambda: core.register_crawler(AwesomeEmptyCrawler))

    def test_running_without_registered_crawlers(self):
        core = datCrawl()
        self.assertRaises(NoCrawlerRegistered, lambda: core.run('www.google.es'))

    def test_running_without_url_parameters(self):
        core = datCrawl()
        self.assertRaises(TypeError, lambda: core.run())

    def test_kwargs_beign_sent(self):
        core = datCrawl()
        core.register_crawler(AwesomeGoogleKwargsCrawler)
        self.assertEqual(core.run('http://google.es'), 'es')
        self.assertEqual(core.run('http://google.com'), 'com')
        self.assertEqual(core.run('http://google.co.jp'), 'co.jp')

    def test_crawler_url_need_regex_with_group(self):
        core = datCrawl()
        core.register_crawler(CrawlerWithRegexGroupError)
        self.assertRaises(CrawlerUrlDontHaveGroupDefined, lambda: core.run('http://google.es'))

if __name__ == '__main__':
    unittest.main()
