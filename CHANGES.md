## 0.2.0 (WIP)
Modified crawler behaviour:
- Now every regular expression of a certain URL **needs** a group called `url`. That group will be the URL sent to the associated `Downloader`.
- The core send the match object (`re.compile.match()`) as a `kwarg` to the `Crawler`called: `matches`, so you can play around with URL values too accessing it via `kwargs.get('matches')`.
- Added an Exception and test cases for this behaviour: Checking for the `url` group on a pattern and checking for the kwargs being sent correctly.

## 0.1.1 (2013-03-16)
- Fixing pypi package

## 0.1.0 (2013-03-16)
- Initial release
