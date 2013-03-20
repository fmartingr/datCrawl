from datCrawl.crawlers import Crawler
from datCrawl.downloaders import Downloader


class AwesomeGoogleCrawler(Crawler):
    urls = [
        ('es', '(?P<url>http\:\/\/google\.(?P<tld>es))', ),
        ('de', '(?P<url>http\:\/\/google\.(?P<tld>de))', )
    ]


# For testing kwargs
class AwesomeGoogleKwargsCrawler(Crawler):
    urls = [
        ('do_things', '(?P<url>http\:\/\/google\.(?P<tld>es|com|co\.jp))', ),
    ]

    def action_do_things(self, data, **kwargs):
        return kwargs.get('matches').group('tld')


class CrawlerWithRegexGroupError(Crawler):
    urls = [
        ('es', '(?P<this_should_be_url>http\:\/\/google\.es)', ),
    ]


class AwesomeEmptyCrawler(Crawler):
    pass


class AwesomeWikipediaTitleCrawler(Crawler):
    urls = [
        ('get_title', '(?P<url>http\:\/\/en.wikipedia.org\/wiki\/(?P<name>.*))', )
    ]
    downloader = 'Downloader'

    def action_get_title(self, data, **kwargs):
        # LOOK, IM CRAWLING THE INTERNETS!
        return {'title': 'Python'}


class CrawlerWithOptions(AwesomeGoogleKwargsCrawler):
    downloader_options = {'are_sent': True}
    downloader = 'DownloaderThatReturnKwargs'

    def action_do_things(self, data, **kwargs):
        return data


class DownloaderThatReturnKwargs(Downloader):
    def get(self, url, **kwargs):
        options = kwargs.get('options')
        return options['are_sent']
