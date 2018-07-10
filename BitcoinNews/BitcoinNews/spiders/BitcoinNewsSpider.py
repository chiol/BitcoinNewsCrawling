# -*- coding: utf-8 -*-

import scrapy

from BitcoinNews.items import BitcoinnewsItem
from datetime import datetime

class BitcoinNewsSpider(scrapy.Spider):
    name = "bitcoinnewsCrawler"

    def start_requests(self):
        for i in range(1,576):
            yield scrapy.Request("https://news.bitcoin.com/page/{0}".format(i),self.parse_bitcoinnews)
        for i in range(1,99):
            yield scrapy.Request("https://www.cnbc.com/bitcoin/?page={0}".format(i),self.parse_cnbcnews)

    def parse_bitcoinnews(self,response):
        for sel in response.xpath('//div[@class="item-details"]'):
            item = BitcoinnewsItem()
            item['title'] = sel.xpath('h3[@class="entry-title td-module-title"]/a/text()').extract()[0]
            # item['address'] = sel.xpath('h3[@class="entry-title td-module-title"]/a/@href').extract()[0]
            date = sel.xpath('div[@class="td-module-meta-info"]/span/time/text()').extract()[0]
            date = datetime.strptime(date,"%b %d, %Y")
            item['date'] = str(date.year)+"-"+str(date.month)+"-"+str(date.day)
            yield item

    def parse_cnbcnews(self,response):
        for li in response.xpath('//ul[@class="stories_assetlist"]/li'):
            if(li.xpath('div/div/a/text()').extract() == []):
                continue
            item = BitcoinnewsItem()
            title = li.xpath('div/div/a/text()').extract()[0][37:]
            if(title.find('\n') != -1):
                title = title[:-20]
            item['title'] = title
            # item['address'] = li.xpath('div/div/a/@href').extract()[0]
            date = li.xpath('div/time/text()').extract()[0]
            if(date.find("Ago") != -1):
                date = datetime.now()
            else:
                date = date[date.find("ET")+8:]
                if(date[0] == " "):
                    date = date[1:]
                date = date.replace("Sept","Sep")
                try:
                    date = datetime.strptime(date,"%d %B %Y")
                except:
                    date = datetime.strptime(date,"%d %b %Y")
            item['date'] = str(date.year)+"-"+str(date.month)+"-"+str(date.day)
            yield item



