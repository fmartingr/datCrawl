from datCrawl import datCrawl
from datCrawl.crawlers import Crawler
from datCrawl.downloaders import DefaultDownloader
try:
    from lxml.cssselect import CSSSelector
    from lxml.html.soupparser import fromstring
except:
    print "For this example to work you must install lxml, csselect"
    print "and BeautifulSoup via pip or easy_install:"
    print " # pip install lxml cssselect BeautifulSoup"
    exit()


class GithubNameCrawler(Crawler):
    urls = [
        (
            'get_name',
            '(?P<url>https\:\/\/github\.com\/fmartingr\/(?P<name>.*))'
        )
    ]
    downloader = 'DefaultDownloader'

    def action_get_name(self, data, **kwargs):
        try:
            document = fromstring(data)
            selector = CSSSelector('.js-current-repository')
            name = selector(document)[0].text
            data = {
                'name': name
            }
            return data
        except Exception as e:
            print e


datcrawl = datCrawl()
datcrawl.register_downloader(DefaultDownloader)
datcrawl.register_crawler(GithubNameCrawler)
print datcrawl.run("https://github.com/fmartingr/datCrawl")
# returns {'name': 'datCrawl'}
