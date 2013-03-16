from datCrawl.crawlers import Crawler


class AwesomeGoogleCrawler(Crawler):
    urls = [
        ('es', 'http\:\/\/(www\.)?google\.es', ),
        ('de', 'http\:\/\/(www\.)?google\.de', )
    ]


class AwesomeEmptyCrawler(Crawler):
    pass


class AwesomeWikipediaTitleCrawler(Crawler):
    urls = [
        ('get_title', 'http\:\/\/en.wikipedia.org\/wiki\/(.*)', )
    ]
    downloader = 'Downloader'

    def action_get_title(self, data):
        # LOOK, IM CRAWLING THE INTERNETS!
        return {'title': 'Python'}
