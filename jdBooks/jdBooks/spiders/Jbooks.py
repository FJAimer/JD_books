import scrapy
import json
from jdBooks.items import JdbooksItem


class JbooksSpider(scrapy.Spider):
    name = 'Jbooks'
    # 2、检查允许的域
    allowed_domains = ['jd.com']
    # 1、修改起始url
    # start_urls = ['https://book.jd.com/booksort.html']
    start_urls = ['https://pjapi.jd.com/book/sort?source=bookSort']

    # 3、实现爬取逻辑
    def parse(self, response):
        # print(type(response.body))
        json_obj = json.loads(response.body.decode())  # dict 字典
        # print(type(json_obj))
        yield json_obj
        # 获取所有图书大分类节点列表
        # big_node_list = response.xpath('//*[@id="booksort"]/div[2]/dl/dt/a')
        # 循环遍历图书大分类
        # for big_node in big_node_list[:1]:
        #     big_category = big_node.xpath("./text()").extract_first()
        #     big_category_link = big_node.xpath("./@href").extract_first()
        #     print(big_category,big_category_link)
