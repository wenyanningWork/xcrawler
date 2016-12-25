#!/usr/bin/env python3
# -*-coding: utf-8-*-
# Author : Christopher Lee
# License: MIT License
# File   : request.py
# Date   : 2016-12-24 03:02
# Version: 0.0.1
# Description: Request
from xcrawler.utils.url import safe_url

__version__ = '0.0.1'
__author__ = 'Chris'


class Request(object):
    def __init__(self, url, cookies=None, headers=None, meta=None, proxy=None, callback=None,
                 dont_filter=False):
        self.url = safe_url(url)
        self.cookies = cookies
        self.headers = headers or {}
        self.meta = meta
        self.proxy = proxy
        self.callback = callback
        self.dont_filter = dont_filter

    def __repr__(self):
        return '<Request url="{url}">'.format(**self.__dict__)
