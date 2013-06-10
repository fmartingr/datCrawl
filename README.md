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

[Go to the documentation](http://datcrawl.readthedocs.org)

```
pip install datCrawl
```

## To do

- Better documentation
- Maybe a standalone tool?
- Logging mechanics (too many Exceptions IMO)

## A basic example

See examples/simple.py

## License

See LICENSE file.
