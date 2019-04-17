# -*- coding: utf-8 -*-
import scrapy


class CompanyInfoSpider(scrapy.Spider):
    name = 'company_info'
    allowed_domains = ['tianyancha.com']
    start_urls = ['http://tianyancha.com/']

    def parse(self, response):
        pass
