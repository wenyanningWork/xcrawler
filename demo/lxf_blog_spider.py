#!/usr/bin/env python3
# -*-coding: utf-8-*-
# Author : Christopher Lee
# License: MIT License
# File   : lxf_blog_spider.py
# Date   : 2016-12-24 00:15
# Version: 0.0.1
# Description: description of this file.


import logging

from xcrawler.core.crawler import CrawlerProcess
from xcrawler.spider.spider import BaseSpider

__version__ = '0.0.1'
__author__ = 'Chris'

logging.basicConfig(format='[%(asctime)s][%(module)s.%(lineno)d][%(levelname)s] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.DEBUG)


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


if __name__ == '__main__':
    main()
