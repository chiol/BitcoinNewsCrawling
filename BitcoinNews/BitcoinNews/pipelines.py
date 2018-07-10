# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exporters import CsvItemExporter
class BitcoinnewsPipeline(object):
    def process_item(self, item, spider):
        return item

class CSVPipeline(object):
    """Distribute items across multiple XML files according to their 'year' field"""
    f = open("bitcoinnews.csv", 'wb')
    exporter = CsvItemExporter(f)

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item