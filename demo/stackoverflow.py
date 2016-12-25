#!/usr/bin/env python3
# -*-coding: utf-8-*-
# Author : Christopher Lee
# License: MIT License
# File   : stackoverflow.py
# Date   : 2016-12-25 20:30
# Version: 0.0.1
# Description: stackoverflow.com
import json
import os
import sys
from xcrawler.spider import BaseSpider, Request
from lxml.html import fromstring

__version__ = '0.0.1'
__author__ = 'Chris'


class StackoverflowSpider(BaseSpider):
    name = 'stackoverflow_spider'
    start_urls = ['http://stackoverflow.com/questions/tagged/python']
    default_headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/50.0.2661.102 Safari/537.36'
    }
    proxy = 'socks5://127.0.0.1:1080'

    def spider_started(self):
        self.file = open('stk_items.jl', 'w')

    def spider_stopped(self):
        self.file.close()

    def make_requests_from_url(self, url):
        return Request(url, headers=self.default_headers, callback=self.parse)

    def parse(self, response):
        root = fromstring(response.content, response.base_url)
        next_page_rule = '//a[@rel="next"]/@href'
        question_element_rule = '//div[@class="question-summary"]'

        next_url = response.urljoin(self._extract_first(root, next_page_rule))
        yield Request(next_url, headers=self.default_headers)

        for ele in root.xpath(question_element_rule):
            item = dict()
            item['question_title'] = self._extract_first(ele, '//a[@class="question-hyperlink"]/text()')
            item['question_url'] = response.urljoin(self._extract_first(ele, '//a[@class="question-hyperlink"]/@href'))
            item['question_desc'] = self._extract_first(ele, '//div[@class="excerpt"]/text()').strip()
            item['question_tags'] = ele.xpath('//a[@class="post-tag"]/text()')
            item['votes'] = self._extract_first(ele, '//span[@class="vote-count-post "]/strong/text()')
            item['username'] = self._extract_first(ele, '//div[@class="user-details"]/a/text()')
            yield item

    def process_item(self, item):
        print(json.dumps(item, ensure_ascii=False, sort_keys=True, indent=4))
        print(json.dumps(item, ensure_ascii=False, sort_keys=True), file=self.file)

    def process_request(self, request):
        request.proxy = self.proxy

    @staticmethod
    def _extract_first(element, exp, default=''):
        r = element.xpath(exp)
        if len(r):
            return r[0]

        return default


def main():
    from xcrawler import CrawlerProcess

    settings = {
        'download_delay': 1,
        'download_timeout': 24,
        'retry_on_timeout': True,
        'concurrent_requests': 256,
        'queue_size': 1024
    }

    crawler = CrawlerProcess(settings, 'ERROR')
    crawler.crawl(StackoverflowSpider)
    crawler.start()


if __name__ == '__main__':
    main()
