# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JdbooksItem(scrapy.Item):
    # define the fields for your item here like:
    # 建立模型
    big_category = scrapy.Field()
    big_category_lin = scrapy.Field()
    small_category = scrapy.Field()
    small_category_link = scrapy.Field()
    pass
