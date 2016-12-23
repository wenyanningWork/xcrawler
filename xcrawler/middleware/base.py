#!/usr/bin/env python3
# -*-coding: utf-8-*-
# Author : Christopher Lee
# License: MIT License
# File   : base.py
# Date   : 2016-12-24 03:14
# Version: 0.0.1
# Description: description of this file.


__version__ = '0.0.1'
__author__ = 'Chris'


class BaseMiddleware(object):
    def __init__(self):
        pass

    def process_request(self, request, spider):
        pass

    def process_response(self, response, spider):
        pass
