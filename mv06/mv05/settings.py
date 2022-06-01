# Scrapy settings for mv05 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'mv05'

SPIDER_MODULES = ['mv05.spiders']
NEWSPIDER_MODULE = 'mv05.spiders'

DEPTH_LIMIT=3

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'mv05 (+http://www.yourdomain.com)'
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'

# Obey robots.txt rules
#ROBOTSTXT_OBEY = True
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32
CONCURRENT_REQUESTS = 1

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#延时3秒，不能动态改变，时间间隔固定，容易被发现，导致ip被封
#DOWNLOAD_DELAY = 3

# 启用后，当从相同的网站获取数据时，Scrapy将会等待一个随机的值，延迟时间为0.5到1.5之间的一个随机值乘以DOWNLOAD_DELAY
RANDOMIZE_DOWNLOAD_DELAY=True

# The download delay setting will honor only one of:
#对单个网站进行并发请求的最大值，默认为8
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#对单个IP进行并发请求的最大值，如果非0,则忽略CONCURRENT_REQUESTS_PER_DOMAIN设定，使用该IP限制设定。
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'mv05.middlewares.Mv05SpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'mv05.middlewares.Mv05DownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines  激活pipeline，否则不起作用； 多pipeline从底传递到高值
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'mv05.pipelines.Mv05Pipeline': 300,
#}
ITEM_PIPELINES = {
#    'mv05.pipelines.Mv05Pipeline': 100,
    'mv05.pipelines.Mv05SQLitePipeline': 300,
}

#自动限速扩展
# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#默认为False，设置为True可以启用该扩展
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
# #初始下载延迟，单位为秒，默认为5.0
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# 设置在高延迟情况下的下载延迟，单位为秒，默认为60
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#用于启动Debug模式，默认为False
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


SQLITE_FILE = "mvinfo.db"



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