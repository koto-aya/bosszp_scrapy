# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql


class ScrapyBosszpPipeline:
    def dbHandle(self):
        conn = pymysql.connect(
            host="localhost",
            user="root",
            passwd="root",
            charset="utf8",
            database="bosszp_db"
        )
        return conn

    def insertItemToDB(self,item):
        dbObj = self.dbHandle()
        cursor = dbObj.cursor()
        insertSql="insert into bosszp_info values(null,%s,%s,%s,%s,%s,%s)"
        try:
            cursor.execute(insertSql,(item['job_name'],item['job_area'],item['company_name'],item['salary'],item['work_experience'],item['educational_background']))
            cursor.connection.commit()
        except Exception as e:
            print(e)

    def process_item(self, item, spider):
        if item==None:
            raise Exception("参数错误")
        self.insertItemToDB(item)
        return item
