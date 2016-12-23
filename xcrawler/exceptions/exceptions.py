#!/usr/bin/env python3
# -*-coding: utf-8-*-
# Author : Christopher Lee
# License: MIT License
# File   : exceptions.py
# Date   : 2016-12-24 03:13
# Version: 0.0.1
# Description: description of this file.

__version__ = '0.0.1'
__author__ = 'Chris'


class DropItem(Exception):
    pass


class DropRequest(Exception):
    pass


class DropResponse(Exception):
    pass
