class CrawlerIsNotInstanceOfBase(Exception):
    "Class is not instance of the base crawler."
    pass


class DownloaderIsNotInstanceOfBase(Exception):
    "Class is not instance of the base downloader."
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


class DownloaderAlreadyRegistered(Exception):
    "When you try to register the same downloader."
    pass


class DownloaderIsNotRegistered(Exception):
    "When you try to register a Crawler before its downloader."
    pass
