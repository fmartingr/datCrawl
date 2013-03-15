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


class CrawlerForThisURLNotFound(Exception):
    "When there's no crawler found for a specific URL"
    pass


class CrawlerAlreadyRegistered(Exception):
    "When you try to register the same crawler."
    pass
