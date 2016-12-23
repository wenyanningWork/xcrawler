#!/usr/bin/env python3
# -*-coding: utf-8-*-
# Author : Christopher Lee
# License: MIT License
# File   : crawler.py
# Date   : 2016-12-24 03:08
# Version: 0.0.1
# Description: description of this file.

import logging
from xcrawler.core.engine import CrawlerEngine

__version__ = '0.0.1'
__author__ = 'Chris'


class CrawlerProcess(object):
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self._spiders = []
        self._engine = CrawlerEngine()

    def crawl(self, spider_cls, *args, **kwargs):
        self._spiders.append((spider_cls, args, kwargs))

    def start(self):
        for cls, args, kwargs in self._spiders:
            self._engine.submit(cls, args, kwargs)

        # Block here until every requests completed
        self._engine.start()


def main():
    pass


if __name__ == '__main__':
    main()
