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
        ('title', 'http\:\/\/en.wikipedia.org\/wiki\/(.*)', )
    ]

    def action_title(self, url):
        # LOOK, IM CRAWLING THE INTERNETS!
        return {'title': 'Python'}
