# -*- coding: utf-8 -*-

# Scrapy settings for douban_test project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'douban_test'

SPIDER_MODULES = ['douban_test.spiders']
NEWSPIDER_MODULE = 'douban_test.spiders'
MAXPAGE=1

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'douban_test (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
HTTPERROR_ALLOWED_CODES = [302]
# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   'Accept-Language': 'en',
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
   'Cookie': 'bid=rz_cI9hRUZs; gr_user_id=1d7acee2-0287-4a57-8cea-8f8d8de9926d; _vwo_uuid_v2=DB21B1A1625E65BEBD83CEB02102CB1F2|72d82e5166152ebf715de4564ef118cd; ll="118282"; douban-fav-remind=1; __utmc=30149280; __utmc=223695111; __yadk_uid=FObf6u96PSJsXokW8o81haedZ8ZrlBF6; __utmz=30149280.1534167820.6.6.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmz=223695111.1534167837.2.2.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/search; ps=y; dbcl2="182905276:wUYy5yjK3go"; ck=-IsS; push_noty_num=0; push_doumail_num=0; __utmv=30149280.18290; ap=1; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1534172159%2C%22https%3A%2F%2Fwww.douban.com%2Fsearch%3Fq%3D%25E7%2588%25B1%25E6%2583%2585%25E5%2585%25AC%25E5%25AF%2593%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.134256535.1531628836.1534167820.1534172159.7; __utmb=30149280.0.10.1534172159; __utma=223695111.1924155510.1534058560.1534167837.1534172159.3; __utmb=223695111.0.10.1534172159; _pk_id.100001.4cf6=52266675b8c2aea9.1534058560.3.1534172861.1534168875.',
}


# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'douban_test.middlewares.DoubanTestSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'douban_test.middlewares.DoubanTestDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'douban_test.pipelines.DoubanTestPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
