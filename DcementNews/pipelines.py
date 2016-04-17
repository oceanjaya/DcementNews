# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb
db=MySQLdb.connect("localhost","spider","xyz","dcement_news")
cursor = db.cursor()
db.set_character_set('utf8')
cursor.execute('SET NAMES utf8;')
cursor.execute('SET CHARACTER SET utf8;')
cursor.execute('SET character_set_connection=utf8;')
insert_sql = "INSERT INTO `dcement_news`.`industry_news` ( `url`, `time`, `title`, `content`) \
                    VALUES ('%s','%s','%s','%s')"




class DcementnewsPipeline(object):
    def process_item(self, item, spider):
        sql=insert_sql%(item['url'].encode('utf-8'),item['time'].encode('utf-8'),
                        item['title'].encode('utf-8'),item['content'].encode('utf-8'))
        try:
            cursor.execute(sql)
            db.commit()
        except Exception,e:
            print e
        return item