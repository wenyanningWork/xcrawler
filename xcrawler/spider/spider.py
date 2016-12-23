#!/usr/bin/env python3
# -*-coding: utf-8-*-
# Author : Christopher Lee
# License: MIT License
# File   : spider.py
# Date   : 2016-12-24 03:03
# Version: 0.0.1
# Description: description of this file.

import logging
from xcrawler.spider.request import Request

__version__ = '0.0.1'
__author__ = 'Chris'


class BaseSpider(object):
    name = ''
    settings = {}
    allowed_hosts = None
    start_urls = []

    def __init__(self, *args, **kwargs):
        self.crawler = kwargs.get('crawler', None)
        self.logger = logging.getLogger(__name__)

    def start_requests(self):
        for url in self.start_urls:
            yield self.make_requests_from_url(url)

    def make_requests_from_url(self, url):
        return Request(url, callback=self.parse)

    def parse(self, response):
        raise NotImplementedError

    def __repr__(self):
        return '<{} name="{}">'.format(self.__class__.__name__, self.name)
