# -*- coding: utf-8 -*-
import scrapy


class CrawlerSpider(scrapy.Spider):
    name = 'crawler'
    allowed_domains = ['scraper2']
    start_urls = ['http://scraper2/']

    def parse(self, response):
        pass
