#!/usr/bin/env python3
# -*-coding: utf-8-*-
# Author : Christopher Lee
# License: MIT License
# File   : crawler.py
# Date   : 2016-12-24 03:08
# Version: 0.0.2
# Description: Crawler process starts the core engine.

import logging
from xcrawler.core.engine import CrawlerEngine

__version__ = '0.0.2'
__author__ = 'Chris'

__all__ = ['CrawlerProcess']


class CrawlerProcess(object):
    def __init__(self, settings=None, log_level='DEBUG'):
        """
        Crawler process controls the engine.

        :param settings: settings for the crawler
        :param log_level: default log level is `logging.DEBUG`
        """
        self.logger = logging.getLogger(__name__)
        self._engine = CrawlerEngine(**(settings or {}))
        self._log_level = log_level
        self._config_logger()

    def crawl(self, spider_cls, *args, **kwargs):
        self._engine.submit(spider_cls, *args, **kwargs)

    def start(self):
        self._engine.start()

    def _config_logger(self):
        logging.basicConfig(format='[%(asctime)s][%(module)s.%(lineno)d][%(levelname)s] %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S',
                            level=getattr(logging, self._log_level, logging.DEBUG))
