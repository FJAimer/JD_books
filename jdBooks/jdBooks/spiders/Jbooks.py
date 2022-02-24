import scrapy


class JbooksSpider(scrapy.Spider):
    name = 'Jbooks'
    # 2、检查允许的域
    allowed_domains = ['jd.com']
    # 1、修改起始url
    start_urls = ['https://book.jd.com/booksort.html']

    # 3、实现爬取逻辑
    def parse(self, response):
        pass
