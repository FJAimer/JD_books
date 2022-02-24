# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json


class JdbooksPipeline:
    def open_spider(self, spider):
        if spider.name == 'Jbooks':
            self.file = open('jdbooks.json', 'w')

    def process_item(self, item, spider):
        if spider.name == 'Jbooks':
            # item = dict(item)
            str_data = json.dumps(item, ensure_ascii=False)
            self.file.write(str_data)
        return item

    def close_spider(self, spider):
        if spider.name == 'Jbooks':
            self.file.close()

