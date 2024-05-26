# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BosszpItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    job_name=scrapy.Field()
    job_area=scrapy.Field()
    company_name=scrapy.Field()
    salary=scrapy.Field()
    work_experience=scrapy.Field()
    educational_background=scrapy.Field()

