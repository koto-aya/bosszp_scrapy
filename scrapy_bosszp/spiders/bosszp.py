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
        browser=webdriver.Edge()
        browser.get(self.start_urls[0])
        browser.implicitly_wait(2)
        job_card=browser.find_element(By.CLASS_NAME,"job-card-wrapper")
        job_name=job_card.find_element(By.CLASS_NAME,"job-name").text
        print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        print(job_name)
        # with open("test.html","w+",encoding="utf-8") as file:
        #     file.write(content)