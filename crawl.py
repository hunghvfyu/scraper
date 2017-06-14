# -*- coding: utf-8 -*-
import scrapy


class CrawlSpider(scrapy.Spider):
    name = 'crawl'
    allowed_domains = ['scraper2']
    start_urls = ['http://scraper2/']

    def parse(self, response):
        pass
