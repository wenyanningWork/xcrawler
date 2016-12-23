#!/usr/bin/env python3
# -*-coding: utf-8-*-
# Author : Christopher Lee
# License: MIT License
# File   : request.py
# Date   : 2016-12-24 03:02
# Version: 0.0.1
# Description: description of this file.


__version__ = '0.0.1'
__author__ = 'Chris'


class Request(object):
    def __init__(self, url, cookies=None, headers=None, meta=None, proxy=None, callback=None):
        self.url = url
        self.cookies = cookies
        self.headers = headers
        self.meta = meta
        self.proxy = proxy
        self.callback = callback

    def __repr__(self):
        return '<Request url="{url}" callback="{callback}">'.format(**self.__dict__)
