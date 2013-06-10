Quickstart
==========

Understanding the terms
-----------------------

Before you start using datCrawl, there are a few terms that you must understand. These are the :code:`crawler` and the :code:`downlaoder`.

The downloader
**************

This are code pieces that download data from the net. A downloader could use any library or software to perform the task.

datCrawl is provided with a base Downloader class called DefaultDownloader, that uses urllib2 for getting the data. You may construct as many as you need for your project.

It is recommended to use your own downloaders instead of using the DefaultDownloader that datCrawl provides, since that is there just for quick testing the package.

The crawler
***********

This is the part of the code that extract information from a certain site. You provide your crawler with certain url patterns (as regular expressions) and binds them to a class method that parses the input and returns the wanted output.


The first crawler
-----------------

I want to make a crawler that extract the name from my github projects, it will be something like this:

::

    from datCrawl.crawlers import Crawler


    class GithubNameCrawler(Crawler):
        downloader = 'DefaultDownloader'
        urls = [
            (
                'get_name',
                '(?P<url>https\:\/\/github\.com\/fmartingr\/(?P<name>.*))'
            )
        ]

        def action_get_name(self, data, **kwargs):
            try:
                document = fromstring(data)
                selector = CSSSelector('.js-current-repository')
                name = selector(document)[0].text
                data = {
                    'name': name
                }
                return data
            except Exception as e:
                print e

The class mandatory parameters are:
    * **downloader**: The class name of the downloader the crawler needs.
    * **urls**: A list of tuples with two values: a regular expression matching certain urls we want to parse and the name of the action to call if the regular expression finds a match.


Basic usage
-----------

After we have the Crawler, we can start working! [1]_

::

    from datCrawl import datCrawl
    from datCrawl.crawlers import Crawler
    from datCrawl.downloaders import DefaultDownloader
    from lxml.cssselect import CSSSelector
    from lxml.html.soupparser import fromstring
    # Our crawler goes here!

    # Summon the main class
    datcrawl = datCrawl()

    # Register the default downloader
    datcrawl.register_downloader(DefaultDownloader)

    # Register the crawler
    datcrawl.register_downloader(GithubNameCrawler)

    # Get this project name!
    print datcrawl.run("https://github.com/fmartingr/datCrawl")

    # returns {'name': 'datCrawl'}

That's it.

You can create Crawlers and Downloaders as complex as you want, but the basic usage is this. In simple cases you only need to create your crawler class and fire it, but for more complex situations you can have as many modules/classes as you need/want.

You have the full example script on the :code:`examples/github.py` file.

----------

.. [1] Please note that for this example to work you will need to install the lxml, cssselect and BeautifulSoup libraries.
