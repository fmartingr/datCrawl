## 0.3.0 (2013-03-23)
Added `datCrawlerWorker` class:
- This now does the download and crawling "phases"
- new: `datCrawl.worker(url)` and `datCrawl.match(url)`, both returns a `datCrawlerWorker`

## 0.2.0 (2013-03-16)
**Modified crawler behaviour**
- Now every regular expression of a certain URL **needs** a group called `url`. That group will be the URL sent to the associated `Downloader`.
- The core send the match object (`re.compile.match()`) as a `kwarg` to the `Crawler`called: `matches`, so you can play around with URL values too accessing it via `kwargs.get('matches')`.
- Added an Exception and test cases for this behaviour: Checking for the `url` group on a pattern and checking for the kwargs being sent correctly.

**Added options to `Downloaders`**
- Passed via kwarg `options`
- This will improve the reusability of the Downloader, so you don't have separated classes for proxies, user agents, etc.

## 0.1.1 (2013-03-16)
- Fixing pypi package

## 0.1.0 (2013-03-16)
- Initial release
