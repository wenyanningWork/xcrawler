#!/usr/bin/env python3
# -*-coding: utf-8-*-
# Author : Christopher Lee
# License: MIT License
# File   : response.py
# Date   : 2016-12-24 03:02
# Version: 0.0.1
# Description: Response


from urllib.parse import urljoin
from xcrawler.utils.url import base_url

__version__ = '0.0.1'
__author__ = 'Chris'


class Response(object):
    def __init__(self, url, status, content, request, cookies=None, headers=None):
        self.request = request
        self.url = url
        self.base_url = base_url(url)
        self.cookies = cookies
        self.headers = headers
        self.status = status
        self.content = content or ''
        self.meta = getattr(request, 'meta', None)

    def urljoin(self, url):
        return urljoin(self.base_url, url)

    @property
    def content_as_unicode(self):
        return self.content.decode('utf-8')

    def __repr__(self):
        return '<Response status={} url="{}" content="{}">'.format(self.status, self.url,
                                                                   self.content[:60])
