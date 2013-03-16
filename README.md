datCrawl
========
Crawling as easy as an API


Branch | Status
------ | ------
master | [![Build Status](https://api.travis-ci.org/fmartingr/datCrawl.png)](https://travis-ci.org/fmartingr/datCrawl)
develop | [![Build Status](https://api.travis-ci.org/fmartingr/datCrawl.png?branch=develop)](https://travis-ci.org/fmartingr/datCrawl)

## Why?
After some time working with some software for crawling purposes, I saw that you needed to make custom functions and custom code for every aspect of your application. Working with celery is the simplest example of that. For indexing two separate sites you needed to use two (or more) separate tasks, even if the work was the same.

I'm trying to simplify that.

When you're working with a crawler, the most basic thing you want to get is a object with the fields that you scrapped from the content, so I thought... If it were as easy as "calling" an URL and receiving an object, that would be awesome! After all, you only want certain data from a certain URL (which is the same when you call an API).

## The works
I've divided the thing in two components: Downloaders and Crawlers.

The `Downloader` subclasses are simple workers that get the content from a certain URL.

The `Crawler` subclases are where the scrapping work is done. The schema is something like: (more on all of this later)

- A crawler manages certain URL patterns (as regular expressions)
- It have a related Downloader class as his side to get the data.
- Every URL we want to "monitor" is asociated with an action.
- We define those actions as methods in our class. (i.ex: action_[action name])

## Usage

For now, refer to the example below or in the repo. Better documentation is on the works.

```
pip install datCrawl
```

## To do

- Better documentation
- `Downloader` options
- Maybe a standalone tool?
- Logging mechanics (too many Exceptions IMO)

## A basic example

``` python
from datCrawl import *
from datCrawl.downloaders import DefaultDownloader
from lxml.cssselect import CSSSelector
from lxml.etree import fromstring as document_fromstring

# Here we define our custom downloader.
# Looks like the DefaultDownloader but this have a
# User-Agent header so Wikipedia don't forbbids us access :)
class DefaultDownloaderWithCustomUserAgent(DefaultDownloader):
    def get(self, url):
        import urllib2
        try:
            headers = {'User-Agent': 'Firefox'}
            req = urllib2.Request(url, "", headers)
            response = urllib2.urlopen(req)
            data = response.read()
            return data
        except Exception:
            raise Exception("Error downloading %s" % url)

# Here is our crawler, it just get the title from a certain article.
class AwesomeWikipediaTitleCrawler(Crawler):
    # The actions -> url pattern asociated with this crawler
    urls = [
        ('get_title', 'http\:\/\/en.wikipedia.org\/wiki\/(.*)', )
    ]
    # The downloader this crawlers needs
    downloader = 'DefaultDownloaderWithCustomUserAgent'

    # The action
    def action_get_title(self, data):
        try:
            document = document_fromstring(data)
            selector = CSSSelector('h1.firstHeading > span')
            return {'title': selector(document)[0].text}
        except Exception as e:
            print e
        #return {'title': 'Python'}

# The magic
crawler = datCrawl()  # The base class
# Register the downloader
crawler.register_downloader(DefaultDownloaderWithCustomUserAgent)
# Register the crawler
crawler.register_crawler(AwesomeWikipediaTitleCrawler)
# Eat pie.
print crawler.run("http://en.wikipedia.org/wiki/Python_(programming_language)")

```
