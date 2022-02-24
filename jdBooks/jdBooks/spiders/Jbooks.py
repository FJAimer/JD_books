import scrapy
import json
from jdBooks.items import JdbooksItem


class JbooksSpider(scrapy.Spider):
    name = 'Jbooks'
    # 2、检查允许的域
    allowed_domains = ['jd.com']
    # 1、修改起始url
    start_urls = ['https://pjapi.jd.com/book/sort?source=bookSort']

    # 3、实现爬取逻辑
    def parse(self, response):
        # item = JdbooksItem()
        item = dict()
        json_obj = json.loads(response.body.decode())
        # print(type(json_obj))   # dict 字典
        # 获取所有图书大小分类数据列表
        data_list = json_obj["data"]
        for data in data_list:
            item['big_category'] = data['categoryName']
            big_father_Category_id = int(data['fatherCategoryId'])
            big_category_id = int(data['categoryId'])
            item['big_category_link'] = 'https://channel.jd.com/' + str(big_father_Category_id) + '-' + str(big_category_id) + '.html'
            # 获取所有小分类数据列表
            small_data_list = data['sonList']
            for small_data in small_data_list:
                item['small_category'] = small_data['categoryName']
                small_father_Category_id = int(small_data['fatherCategoryId'])
                small_category_id = int(small_data['categoryId'])
                item['small_category_link'] = 'https://list.jd.com/list.html?cat=' + str(big_father_Category_id) + ',' + str(small_father_Category_id) + ',' + str(small_category_id)

                yield item

