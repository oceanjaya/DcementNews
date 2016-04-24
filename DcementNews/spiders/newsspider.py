# -*- coding: utf-8 -*-
import scrapy
import re
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from DcementNews.items import  DcementNewsItem

class DcementNewsSpider(scrapy.Spider):
    name = "news"
    allowed_domains = ["www.dcement.com"]
    start_urls = ['http://www.dcement.com/Category_43/Index.aspx']
    for i in range(2,596):
        start_urls.append('http://www.dcement.com/Category_43/Index_%d.aspx'%i)
    def parse(self, response):
        for url in response.xpath("//ul[contains(@class,'infoList')]/li/a/@href").extract():
            url='http://www.dcement.com'+url
            yield scrapy.Request(url,callback=self.parse_content)

    def parse_content(self,response):
        try:
            url=response.url
            time_raw=response.xpath('//div[@class="property"]/span[1]/text()').extract()[0]
            time_list=re.findall(u'(\d+)年(\d+)月(\d+)日',time_raw)[0]
            sourse_raw=response.xpath('//div[@class="property"]/span[3]/text()').extract()[0]
            sourse=re.findall(u'来源: (.+)',sourse_raw)[0]
            time=''.join(time_list)
            title=response.xpath('//h2[@class="title"]/text()').extract()[0]
            content=response.xpath('string(//div[@class="conTxt"])').extract()[0]

            # 写入TXT文件
            filename="news_output_txt/"+title+".txt"
            if not os.path.isfile(filename):
                with open(filename,'wb') as f:
                    f.write(title.decode('utf-8')+'\n\n')
                    f.write(time_raw.decode('utf-8')+'\n')
                    f.write(sourse_raw.decode('utf-8')+'\n')
                    f.write(content.decode('utf-8'))
                    f.close()

            #包装到字典对象

            dcement_news=DcementNewsItem({
                'url':url,
                'time':time,
                'source':sourse,
                'title':title,
                'content':content
            })


            return dcement_news
        except Exception,e:
            print e
            print "Error"+" "+url







