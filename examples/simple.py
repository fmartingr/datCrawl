from datCrawl import *
from datCrawl.downloaders import DefaultDownloader
try:
    from lxml.cssselect import CSSSelector
    from lxml.etree import fromstring as document_fromstring
except:
    print "For this example to work you must install lxml and cssselect"
    print " via pip or easy_install:"
    print " # pip install lxml csselect"
    exit()


class DefaultDownloaderWithCustomUserAgent(DefaultDownloader):
    def get(self, url, **kwargs):
        import urllib2
        try:
            options = kwargs.get('options')
            headers = {}
            if 'headers' in options:
                headers = options['headers']
            req = urllib2.Request(url, "", headers)
            response = urllib2.urlopen(req)
            data = response.read()
            return data
        except Exception as error:
            raise Exception("Error downloading %s:" % (url, error))


class AwesomeWikipediaTitleCrawler(Crawler):
    urls = [
        ('get_title', '(?P<url>http\:\/\/en.wikipedia.org\/wiki\/(?P<name>.*))', )
    ]
    downloader = 'DefaultDownloaderWithCustomUserAgent'
    # Downloader options with custom user agent.
    downloader_options = {
        'headers': {'User-agent': 'Firefox'}
    }

    def action_get_title(self, data, **kwargs):
        try:
            document = document_fromstring(data)
            selector = CSSSelector('h1.firstHeading > span')
            return {'title': selector(document)[0].text}
        except Exception as e:
            print e

crawler = datCrawl()
crawler.register_downloader(DefaultDownloaderWithCustomUserAgent)
crawler.register_crawler(AwesomeWikipediaTitleCrawler)
print crawler.run("http://en.wikipedia.org/wiki/Python_(programming_language)")
# returns {'title': 'Python (programming language)'}
