

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

#日志输出
Spider类中抽出来的一个属性，在自构造的爬虫类中self.logger返回一个<class 'LoggerAdapter'>对象，而这个对象中有log、debgu、info等方法，所以我们可以在爬虫组件中使用self.logger.log()、self.logger.debug()等来输出日志，而在其它组件中，会将spider作为参数传进其他组件对象的方法中，所以我们也可以在其它组件中使用spider.logger.log()、spider.logger.debug()等在输出日志。

setting.py 的配置属性如下：
```
# 一般在使用时只会设置LOG_FILE和LOG_LEVEL两个配置项，其他配置项使用默认值

# 指定日志的输出文件
from datetime import datetime
LOG_FILE = "./%s-%02d%02d.log"%(BOT_NAME, datetime.now().month, datetime.now().day )
# 是否使用日志，默认为True
#LOG_ENABLED
# 日志使用的编码，默认为UTF-8
#LOG_ENCODING
# 日志级别，如果设置了，那么高于该级别的就会输入到指定文件中
LOG_LEVEL = "DEBUG"
# 设置日志的输出格式
#LOG_FORMAT
# 设置日志的日期输出格式
#LOG_DATEFORMAT
# 设置标准输出是否重定向到日志文件中，默认为False,如果设置为True,那么print("hello")就会被重定向到日志文件中
#LOG_STDOUT
# 如果设置为True,只会输出根路径，不会输出组件，默认为FALSE
LOG_SHORT_NAMES = True
#默认是 False
LOG_FILE_APPEND = True
```



