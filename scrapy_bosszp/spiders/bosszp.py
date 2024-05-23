import scrapy
from selenium import webdriver
from selenium.webdriver.common.by import By


class BosszpSpider(scrapy.Spider):
    name = "bosszp"
    #允许访问的域名
    allowed_domains = ["https://www.zhipin.com"]
    #第一次要访问的域名
    start_urls = ["https://www.zhipin.com/web/geek/job?query=&city=101230100&position=100101"]

    #是执行力start_urls后，执行的方法，response就是返回的对象
    def parse(self, response):
        job_list=response.xpath("//li[@class='job-card-wrapper']")
        file = open('data.txt',"w+",encoding="utf-8")
        for job_item in job_list:
            job_name=job_item.xpath(".//span[@class='job-name']/text()").get()
            job_area=job_item.xpath(".//span[@class='job-area']/text()").get()
            company_name=job_item.xpath(".//h3[@class='company-name']/a/text()").get()
            file.write(f"职位名称{job_name}\n")
            file.write(f"工作地点{job_area}\n")
            file.write(f"招聘企业{company_name}\n")
            file.write("-----------------------------------\n")

        file.close()