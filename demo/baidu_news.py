#!/usr/bin/env python3
# -*-coding: utf-8-*-
# Author : Christopher Lee
# License: MIT License
# File   : baidu_news.py
# Date   : 2016-12-25 11:46
# Version: 0.0.1
# Description: crawl news in `http://news.baidu.com/`

from xcrawler import CrawlerProcess
from xcrawler.spider import BaseSpider, Request
from lxml.html import fromstring
import json

__version__ = '0.0.1'
__author__ = 'Chris'


class BaiduNewsSpider(BaseSpider):
    name = 'baidu_news_spider'
    start_urls = ['http://news.baidu.com/']
    default_headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/50.0.2661.102 Safari/537.36'
    }

    def spider_started(self):
        self.file = open('items.jl', 'w')

    def spider_stopped(self):
        self.file.close()

    def spider_idle(self):
        # 引擎空闲时，你也可以从数据库中提取新的 URL 进来
        print('I am in idle mode')
        # self.crawler.crawl(new_request, spider=self)

    def make_requests_from_url(self, url):
        return Request(url, headers=self.default_headers)

    def parse(self, response):
        root = fromstring(response.content, base_url=response.base_url)
        for element in root.xpath('//a[@target="_blank"]'):
            title = self._extract_first(element, 'text()')
            link = self._extract_first(element, '@href').strip()
            if title:
                if link.startswith('http://') or link.startswith('https://'):
                    yield {'title': title, 'link': link}
                    yield Request(link, headers=self.default_headers, callback=self.parse_news,
                                  meta={'title': title})

    def parse_news(self, response):
        pass

    def process_item(self, item):
        print(item)
        print(json.dumps(item, ensure_ascii=False), file=self.file)

    @staticmethod
    def _extract_first(element, exp, default=''):
        r = element.xpath(exp)
        if len(r):
            return r[0]

        return default


def main():
    settings = {
        'download_delay': 1,
        'download_timeout': 6,
        'retry_on_timeout': True,
        'concurrent_requests': 16,
        'queue_size': 512
    }
    crawler = CrawlerProcess(settings, 'DEBUG')
    crawler.crawl(BaiduNewsSpider)
    crawler.start()


if __name__ == '__main__':
    main()
