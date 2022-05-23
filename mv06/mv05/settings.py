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