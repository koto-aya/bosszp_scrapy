import scrapy


class BosszpSpider(scrapy.Spider):
    name = "bosszp"
    allowed_domains = ["www.zhipin.com"]
    start_urls = ["http://www.zhipin.com/"]

    def parse(self, response):
        pass
