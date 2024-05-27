import scrapy

from scrapy_bosszp.items import BosszpItem


class BosszpSpider(scrapy.Spider):
    name = "bosszp"
    #允许访问的域名
    allowed_domains = ["www.zhipin.com"]
    #第一次要访问的域名
    start_urls = ["https://www.zhipin.com/web/geek/job?query=&city=101230100&position=100101"]
    #当前页
    current_page=1

    #是执行力start_urls后，执行的方法，response就是返回的对象
    def parse(self, response):
        job_list=response.xpath("//li[@class='job-card-wrapper']")
        for job_item in job_list:
            item=BosszpItem()
            item['job_name']=job_item.xpath(".//span[@class='job-name']/text()").get()
            item['job_area']=job_item.xpath(".//span[@class='job-area']/text()").get()
            item['company_name']=job_item.xpath(".//h3[@class='company-name']/a/text()").get()
            item['salary']=job_item.xpath(".//span[@class='salary']/text()").get()
            item['work_experience']=job_item.xpath(".//ul[@class='tag-list']/li/text()")[0].get()
            item['educational_background']=job_item.xpath(".//ul[@class='tag-list']/li/text()")[1].get()
            yield item
        #爬取5页数据
        if self.current_page<=5:
            self.current_page=self.current_page+1
            next_url=f"{self.start_urls[0]}&page={self.current_page}"
            yield scrapy.Request(next_url, callback=self.parse)