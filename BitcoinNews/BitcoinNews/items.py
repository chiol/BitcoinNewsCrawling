# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BitcoinnewsItem(scrapy.Item):
    # address = scrapy.Field()
    title = scrapy.Field()
    date = scrapy.Field()