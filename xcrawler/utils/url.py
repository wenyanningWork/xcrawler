#!/usr/bin/env python3
# -*-coding: utf-8-*-
# Author : Christopher Lee
# License: MIT License
# File   : url.py
# Date   : 2016-12-24 22:23
# Version: 0.0.1
# Description: handy functions for url processing.

from hashlib import sha1
from urllib.parse import urlparse, urlencode, urlsplit, urlunsplit

__version__ = '0.0.1'
__author__ = 'Chris'


def url_fingerprint(url):
    h = sha1()
    h.update(url.encode('utf-8'))
    return h.hexdigest()


def safe_url(url, remove_empty_query=True):
    scheme, netloc, path, query, fragment = urlsplit(url)

    if not query:
        return url

    # Sort all the queries
    queries = []
    for q in query.split('&'):
        if '=' not in q:
            return url

        key, value = q.split('=')
        if remove_empty_query and not value:
            continue

        queries.append((key, value))

    queries.sort(key=lambda x: x[0])
    query = urlencode(queries)

    return urlunsplit((scheme, netloc, path, query, fragment))


def base_url(url):
    parser = urlparse(url)
    return '://'.join((parser.scheme or 'http', parser.netloc))


def main():
    url = (safe_url('http://fanyi.baidu.com/translate?jlfal=测试&aldtype=16047&ell='))
    print(url_fingerprint(url))


if __name__ == '__main__':
    main()
