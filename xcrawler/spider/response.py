#!/usr/bin/env python3
# -*-coding: utf-8-*-
# Author : Christopher Lee
# License: MIT License
# File   : response.py
# Date   : 2016-12-24 03:02
# Version: 0.0.1
# Description: description of this file.


__version__ = '0.0.1'
__author__ = 'Chris'


class Response(object):
    def __init__(self, url, content, request):
        self.request = request
        self.url = url
        self.content = content or ''
        self.meta = getattr(request, 'meta', None)

    def __repr__(self):
        return '<Response url="{}" content="{}">'.format(self.url,
                                                         self.content[:60])
