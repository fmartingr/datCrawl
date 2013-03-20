import unittest
from datCrawl import datCrawl, downloaders
from datCrawl.exceptions import *
from test.requirements import *


class datCrawlDownloaderTests(unittest.TestCase):
    def test_register_downloader(self):
        core = datCrawl()
        core.register_downloader(downloaders.DefaultDownloader)
        self.assertEqual(core.downloaders['DefaultDownloader'], downloaders.DefaultDownloader)

    def test_register_incorrect_downloader(self):
        core = datCrawl()
        self.assertRaises(DownloaderIsNotInstanceOfBase, lambda: core.register_downloader(object))

    def test_cant_register_downloader_twice(self):
        core = datCrawl()
        core.register_downloader(downloaders.DefaultDownloader)
        self.assertRaises(DownloaderAlreadyRegistered, lambda: core.register_downloader(downloaders.DefaultDownloader))

    def test_downloader_receives_options(self):
        core = datCrawl()
        core.register_downloader(DownloaderThatReturnKwargs)
        core.register_crawler(CrawlerWithOptions)
        self.assertEqual(core.run('http://google.es'), True)

if __name__ == '__main__':
    unittest.main()
