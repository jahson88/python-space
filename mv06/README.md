

# 创建项目
1) scrapy startproject Title
# 进入项目
2) cd Title
# 创建爬虫文件
3）scrapy genspider title c.biancheng.net


# 编写代码
title.py

def parse(self,response):
	pass

修改配置文件settings 


# 5) 定义启动文件
下面定义项目启动文件 run.py， 代码如下：

纯文本复制

    from scrapy import cmdline
    #执行爬虫文件 -o 指定输出文件的格式
    cmdline.execute('scrapy crawl maoyan -o maoyan.csv'.split()) #执行项目，并且将数据存csv文件格式