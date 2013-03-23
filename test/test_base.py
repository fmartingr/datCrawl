import unittest
from datCrawl import *
from test.requirements import *

URL = 'http://en.wikipedia.org/wiki/Python'


class datCrawlBaseTests(unittest.TestCase):

    def test_instance_check(self):
        core = datCrawl()
        self.assertTrue(isinstance(core, datCrawl))

    def test_register_urls(self):
        core = datCrawl()
        data = ('action', 'http://www.google.es/', 'AwesomeGoogleCrawler')
        core.register_url(data[0], data[1], data[2])
        self.assertEqual(core.urls[0], data)

    def test_running_full_crawler(self):
        core = datCrawl()
        core.register_crawler(AwesomeWikipediaTitleCrawler)
        result = core.run(URL)
        self.assertEqual(result['title'], 'Python')

    def test_worker_instance(self):
        core = datCrawl()
        core.register_crawler(AwesomeWikipediaTitleCrawler)
        worker = core.worker(URL)
        self.assertTrue(isinstance(worker, datCrawlWorker))
        self.assertEqual(URL, worker.url)

if __name__ == '__main__':
    unittest.main()
