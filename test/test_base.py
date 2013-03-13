import unittest
from datCrawl import base


class datCrawlTests(unittest.TestCase):

    def test_instance_check(self):
        try:
            core = base.datCrawl
        except Exception, e:
            print e
            print core
        self.assertTrue(core)

if __name__ == '__main__':
    unittest.main()
