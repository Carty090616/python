# -*- coding: utf-8 -*-
import scrapy

from csdn.items import CsdnItem

class CsdnSpiderSpider(scrapy.Spider):
    # 爬虫名字
    name = 'csdn_spider'
    # 允许域
    allowed_domains = ['csdn.net']
    # 爬取的网址
    start_urls = ['http://blog.csdn.net/nav/news']

    def parse(self, response):
        # 先获取页面中class="list_con"的div标签，在获取class="title oneline"的子div标签
        body = response.xpath('//div[@class="list_con"]//div[@class="title oneline"]')
        for value in body:
            item = CsdnItem()
            try:
                item['title'] = value.xpath('./h2/a/text()')[0].extract().strip()
                item['href'] = value.xpath('./h2/a/@href')[0].extract()
            except Exception as e:
                print(e)
            else:
                print(item['title'] + ':' + item['href'])
            yield item
