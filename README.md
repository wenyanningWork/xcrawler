# xcrawler, a light-weight web crawler framework
------------------------

# Introduction
xcrawler, it's a light-weight web crawler framework. Some of its design concepts are borrowed from the well-known framework [Scrapy](https://github.com/scrapy).
The downloader of the engine is implemented with the `requests` library. There are two different thread pools in the crawler's engine, one is for the
downloader and the other for the processors (to extract data and so on).

I'm very interested in web crawling, however, I'm just a newbie to web scraping. I did this so that I can learn more basics of web crawling and Python language.



# Features
- [x] Support plugins (middlewares) and pipelines;
- [x] Very easy to customize your own spider;
- [x] Process multiple requests and responses simultaneously.

# TO-DO
- [ ] Add more middlewares;
- [ ] Use priority_queue instead;
- [ ] Add command line support;
- [ ] Add docs and tests.

# Examples
```
from xcrawler.core.crawler import CrawlerProcess
from xcrawler.spider.spider import BaseSpider


class LXFBlogSpider(BaseSpider):
    name = 'lxf_blog_spider'
    allowed_hosts = ['liaoxuefeng.com']
    start_urls = ['http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000']

    def parse(self, response):
        pass


def main():
    p = CrawlerProcess()
    p.crawl(LXFBlogSpider)
    p.start()

main()
```

# License
xcrawler is licensed under the MIT license, please feel free and happy crawling!

