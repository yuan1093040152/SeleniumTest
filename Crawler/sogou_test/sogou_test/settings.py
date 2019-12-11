# -*- coding: utf-8 -*-

# Scrapy settings for sogou_test project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'sogou_test'

SPIDER_MODULES = ['sogou_test.spiders']
NEWSPIDER_MODULE = 'sogou_test.spiders'

MONGO_URI = '127.0.0.1'
MONGO_DATABASE = 'sogou'
MAXPAGE = 100

cookie1 = {'domain': '.sogou.com', 'expiry': 1535264468.300919, 'httpOnly': False, 'name': 'ppinf', 'path': '/', 'secure': False, 'value': '5|1534054865|1535264465|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZTo3MjolRTglQjQlQUIlRTUlODMlQTclRTclQkElQTAlRTclQkIlOTMlRTQlQjglQUQlRUYlQkMlOEMlRTUlOEIlQkYlRTYlODklQjB8Y3J0OjEwOjE1MzQwNTQ4NjV8cmVmbmljazo3MjolRTglQjQlQUIlRTUlODMlQTclRTclQkElQTAlRTclQkIlOTMlRTQlQjglQUQlRUYlQkMlOEMlRTUlOEIlQkYlRTYlODklQjB8dXNlcmlkOjQ0Om85dDJsdUtaMXlYblVWZHVCZjBXcUN2VUJ4ZmNAd2VpeGluLnNvaHUuY29tfA'}
cookie2 = {'domain': '.sogou.com', 'expiry': 1535264468.300985, 'httpOnly': False, 'name': 'pprdig', 'path': '/', 'secure': False, 'value': 'mABfMIU7I9peqto-9lOSQZPHR_exxc_3fNTIWvdqfj2LcHwLcDCiw_h32huH1pbUl1lCIzW1A01ugPlTZEcHW49Px-oiS_lIMDGKzVKbgIe-H1Kg_VPHALpI-z2gz6CQ_YJtPoxVz5fhr9dLHW8zpuSYEg1e5zl8chTbBkz44yY'}
cookie3 = {'domain': 'weixin.sogou.com', 'httpOnly': True, 'name': 'ppmdig', 'path': '/', 'secure': False, 'value': '1534054865000000f0b57a134b9ee96ff71318b245c860f6'}
cookie4 = {'domain': '.sogou.com', 'expiry': 1535264468.301019, 'httpOnly': False, 'name': 'sgid', 'path': '/', 'secure': False, 'value': '29-36164553-AVtv0dEPK9pSgTllicicldXhM'}
COOKIES = [cookie1,cookie2,cookie3,cookie4]


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'sogou_test (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

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
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'sogou_test.middlewares.SogouTestSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
#     'sogou_test.middlewares.SogouTestDownloaderMiddleware': 543,
    'sogou_test.middlewares.ProxyMiddleware': 541,
    'sogou_test.middlewares.SeleniumMiddleware': 542,
    
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'sogou_test.pipelines.MongoPipeline': 300,
}

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
