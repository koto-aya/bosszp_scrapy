# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


import matplotlib.pyplot as plt
# useful for handling different item types with a single interface
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
            salary=item['salary']
            if salary.endswith("元/天"):
                salary=f"{int(salary.split('-')[0] * 31 / 1000)}k"
            cursor.execute(insertSql,(item['job_name'],item['job_area'],item['company_name'],salary,item['work_experience'],item['educational_background']))
            cursor.connection.commit()
        except Exception as e:
            print(e)

    def process_item(self, item, spider):
        if item==None:
            raise Exception("参数错误")
        self.insertItemToDB(item)
        return item

    def close_spider(self, spider):
        conn = self.dbHandle()
        cursor = conn.cursor()
        sql = "SELECT work_experience,AVG(SUBSTRING_INDEX(IF(salary='面议' OR salary>=100,0,salary),'-',1)) as avg_s FROM " \
              "bosszp_info GROUP BY work_experience"
        cursor.execute(sql)
        data = cursor.fetchall()
        x = []  # x轴
        y = []  # y轴
        for xy in data:
            x.append(xy[0])
            y.append(xy[1])
        print(y)

        plt.bar(x, y)
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.title("柱状图")
        plt.xlabel("工作经验")
        plt.ylabel("平均薪资(单位：千/月)")
        plt.show()