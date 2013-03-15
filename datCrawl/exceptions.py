class CrawlerIsNotInstanceOfBaseCrawler(Exception):
    "Class is not instance of the base crawler."
    pass


class CrawlerDontHaveUrlsToWatch(Exception):
    "Crawler class have the -urls- parameter empty."
    pass


class NoCrawlerRegistered(Exception):
    "Running a crawl operation without a registered crawler."
    pass


class CrawlerActionDoesNotExist(Exception):
    "A crawler action has not been made."
    pass
