# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

from itemadapter import ItemAdapter

import sqlite3

import  sys
sys.path.append( r"E:\py\scrapy\mv05" )

from mv05.settings import *

class Mv05Pipeline:
    def process_item(self, item, spider):
        print( item['id'], item['name'], item['url'], item['durat'], item['rating'], item['channel'] )
        return item  # 多个管道有体现


# 存入sqlite数据库的管道
class Mv05SQLitePipeline(object):
    #开始
    def open_spider(self, spider):
        # 爬虫项目启动，执行连接数据操作
        # 以下常量需要定义在settings配置文件中
        self.db = sqlite3.connect( SQLITE_FILE )
        self.cursor = self.db.cursor()
        if not self.checkExist():
            self.initTable()

    def checkExist(self ):
        try:
            exsitsql = "select 1 from movieinfo limit 1"
            self.cursor.execute( exsitsql )
            #不出错，就说明有此表
            return True
            #res = self.cursor.fetchone()
            #if not res:
            #    return False
            #return res[0] == 1
        except sqlite3.OperationalError as oe:
            print( oe )
            return False

    def initTable(self):
        self.cursor.execute('create table movieinfo (id varchar(20) primary key, name varchar(50),'
                            + ' url varchar(1024), durat varchar(10), rating varchar(4), channel varchar(100),'
                             + ' downloadurl varchar(1024), ipx varchar(4), length varchar(10) )')
        self.db.commit()

    # 向表中插入数据
    def process_item(self, item, spider):
        #如果没有 downloadurl，说明只是列表属性， downloadurl有值 说明获得的mv 的下载地址
        if item.get("downloadurl", "" ) == "" :
            ins = 'insert into movieinfo (id, name, url, durat, rating, channel) values(?,?,?,?,?,?)'
            L = [
                item['id'], item['name'], item['url'], item['durat'], item['rating'], item['channel']
            ]
            # self.cursor.execute("BEGIN TRANSACTION")
            self.cursor.execute(ins, L)
            self.db.commit()
            return item
        else:
            return self.updateUrl( item, spider )

    def updateUrl(self, item, spider ):
        ins = 'update movieinfo set downloadurl=?, ipx=?, length=?  where id=?'
        L = [
            item['downloadurl'], item['ipx'], item['length'], item['id']
        ]
        #self.cursor.execute("BEGIN TRANSACTION")

        self.cursor.execute(ins, L)
        self.db.commit()
        return item

   # 结束存放数据，在项目最后一步执行
    def close_spider(self, spider):
        # close_spider()函数只在所有数据抓取完毕后执行一次，
        self.cursor.close()
        self.db.close()
        print('执行了close_spider方法,项目已经关闭')


if __name__ == "__main__":
    from mv05.items import Mv05Item

    db = Mv05SQLitePipeline()
    db.open_spider( None )
    item = Mv05Item()
    item['id'] = '123'
    item['name'] = 'test'
    item['url'] = 'url'
    item['durat'] = '33'
    item['rating'] = '20%'
    item['channel'] = '/channel/test'
    item['downloadurl'] = 'downloadurl'
    item['ipx'] = '1080'
    item['length'] = '300 Mb'
    db.process_item( item, None )
    db.close_spider( None )