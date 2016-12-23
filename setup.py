#!/usr/bin/env python3
# -*-coding: utf-8-*-
# Author : Christopher Lee
# License: MIT License
# File   : setup.py
# Date   : 2016-12-24 03:20
# Version: 0.0.1
# Description: description of this file.

import sys
from distutils.core import setup

if sys.version_info < (3, 4):
    print('Sorry, supported python versions are Python 3.4+.')
    exit(1)

setup(
    name='xcrawler',
    version='0.0.1',
    packages=['xcrawler'],
    install_requires=['requests'],
    url='https://www.github.com/chrisleegit/xcrawler',
    license='MIT License',
    author='0xE8551CCB',
    author_email='christopherlee199398@gmail.com',
    keywords="xcrawler, a light-weight web crawler framework.",
    description="xcrawler is a light-weight and simple web crawler work. "
                "Part of it's design ideas are similar to `Scrapy`. "
                "I did this for learning purpose, in order to improve my "
                "programming skills. Please feel free and happy crawling. :)"
)
