#!/usr/bin/env python3
# -*-coding: utf-8-*-
# Author : Christopher Lee
# License: MIT License
# File   : engine.py
# Date   : 2016-12-24 03:03
# Version: 0.0.1
# Description: description of this file.

import logging
import threading
from concurrent.futures import ThreadPoolExecutor
from pprint import pformat
from queue import Queue, Empty

import requests

from xcrawler.spider.request import Request
from xcrawler.spider.response import Response

__version__ = '0.0.1'
__author__ = 'Chris'


class CrawlerEngine(object):
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.status = False
        self.concurrent_requests = 10
        self._requests_queue = Queue()
        self._responses_queue = Queue()
        self._spiders = []

    def start(self):
        self.logger.debug('Crawler engine started.')
        self.status = True

        self._init_seed_requests()

        # start download scheduler thread in background
        threading.Thread(target=self._sch_download, daemon=True).start()

        # process all the responses in foreground
        self._process_queued_responses()

    def submit(self, spider_cls, *args, **kwargs):
        self._spiders.append(spider_cls(*args, crawler=self, **kwargs))

    def crawl(self, request, spider):
        self._process_request(request, spider)

    def _init_seed_requests(self):
        for spider in self._spiders:
            try:
                [self.crawl(request, spider) for request in getattr(spider, 'start_requests')()]
            except:
                self.logger.error('Spider missing method "start_requests".')

    def _process_request(self, request, spider):
        self.logger.debug('[{}] Processing request: {}'.format(spider.name, request))
        self._requests_queue.put_nowait((request, spider))

    def _process_response(self, response, spider):
        self.logger.debug('[{}] Processing response: {}'.format(spider.name, response))
        try:
            parse = getattr(spider, 'callback', None) or getattr(spider, 'parse')
        except Exception:
            self.logger.error('Spider missing default callback "parse".')
        else:
            for r in parse(response):
                if r is None:
                    continue

                if isinstance(r, dict):
                    self._process_item(r, spider)
                elif isinstance(r, Request):
                    self.crawl(r, spider)
                else:
                    self.logger.error('Expected types are `dict`, `Request` and `None`')

    def _process_item(self, item, spider):
        self.logger.debug('[{}] Scraped item: {}'.format(spider.name, pformat(item)))

    def _process_queued_responses(self):
        executor = ThreadPoolExecutor(self.concurrent_requests // 2)

        while self.status:
            futures = []
            for resp, spider in self._next_responses_batch():
                futures.append(executor.submit(self._process_response, resp, spider))

        self.logger.debug('Stop processing requests')

    def _sch_download(self):
        executor = ThreadPoolExecutor(self.concurrent_requests)
        while self.status:
            for req, spider in self._next_requests_batch():
                executor.submit(self._download, req, spider)

        self.logger.debug('Stop downloaders.')
        executor.shutdown(False)

    def _download(self, request, spider):
        try:
            r = requests.get(request.url, cookies=request.cookies,
                             headers=request.headers,
                             proxies={'http': request.proxy, 'https': request.proxy})
            self._responses_queue.put_nowait((Response(r.url, r.content, request), spider))
        except Exception as err:
            self.logger.error(err)

    def _next_requests_batch(self):
        for i in range(self.concurrent_requests):
            try:
                yield self._requests_queue.get()
            except Empty:
                pass

    def _next_responses_batch(self):
        for i in range(self.concurrent_requests // 2):
            try:
                yield self._responses_queue.get()
            except Empty:
                pass


def main():
    pass


if __name__ == '__main__':
    main()
