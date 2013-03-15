import datCrawl


class AwesomeWikipediaTitleCrawler(Crawler):
    urls = [
        ('title', 'http\:\/\/en.wikipedia.org\/wiki\/(.*)', )
    ]

    def action_title(self, url):
        return {'title': 'Python'}

crawler = datCrawl()
crawler.register_crawler(AwesomeWikipediaTitleCrawler)
print crawler.run("http://en.wikipedia.org/wiki/Python_(programming_language)")
