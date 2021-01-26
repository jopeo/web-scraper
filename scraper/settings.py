# Scrapy settings for creepy project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

# import scrapy
# from scrapy.exporters import JsonItemExporter

BOT_NAME = 'creepy'

SPIDER_MODULES = ['creepy.spiders']
NEWSPIDER_MODULE = 'creepy.spiders'

FEEDS = {
    'elli6OUT.jsonl': {
        'format': 'jsonlines',
        'encoding': 'utf-8',
        'store_empty': False,
        'fields': ["pg_number", "num_art_avail", "pg_avail", "next_page", "this_pg_no", "art_on_sm_pg", "art_no", "_id", "date", "title", "pub_type", "doi_num", "doi_lnk", "url2pub_pm", "ful_txt_lnks", "authors", "abstract"],
        'indent': 4,
        'item_export_kwargs': {
           'export_empty_fields': True,
        },
    },
    '/home/user/documents/items.xml': {
        'format': 'xml',
        'fields': ["pg_number", "num_art_avail", "pg_avail", "next_page", "this_pg_no", "art_on_sm_pg", "art_no", "_id", "date", "title", "pub_type", "doi_num", "doi_lnk", "url2pub_pm", "ful_txt_lnks", "authors", "abstract"],
        'encoding': 'latin1',
        'indent': 8,
    },
    'elliOUT6.csv': {
        'format': 'csv',
        'fields': ["pg_number", "num_art_avail", "pg_avail", "next_page", "this_pg_no", "art_on_sm_pg", "art_no", "_id", "date", "title", "pub_type", "doi_num", "doi_lnk", "url2pub_pm", "ful_txt_lnks", "authors", "abstract"],
    },
}

FEED_EXPORT_ENCODING = 'utf-8',
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
DOWNLOAD_DELAY = 6,
CONCURRENT_REQUESTS_PER_DOMAIN = 1,
CONCURRENT_REQUESTS_PER_IP = 1,
COOKIES_ENABLED = False,

# FEEDS = {
# 	'items.json':                     {
# 		'format':             'json',
# 		'encoding':           'utf8',
# 		'store_empty':        False,
# 		'fields':             None,
# 		'indent':             4,
# 		'item_export_kwargs': {
# 			'export_empty_fields': True,
# 		},
#
# 	},
#
# }
#
# FEED_EXPORTERS = {
# 	'json':     scrapy.exporters.JsonItemExporter,
# }


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# 'creepy (+http://www.yourdomain.com)'
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs

# The amount of time (in secs) that the downloader should wait before downloading consecutive pages from the same website. This can be used to throttle the crawling speed to avoid hitting servers too hard. Decimal numbers are supported. Example:
# DOWNLOAD_DELAY = 0.25    # 250 ms of delay
# This setting is also affected by the RANDOMIZE_DOWNLOAD_DELAY setting (which is enabled by default). By default, Scrapy doesn’t wait a fixed amount of time between requests,
# but uses a random interval between 0.5 * DOWNLOAD_DELAY and 1.5 * DOWNLOAD_DELAY.
DOWNLOAD_DELAY = 6

# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 1
CONCURRENT_REQUESTS_PER_IP = 1

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'abskwords.middlewares.AbskwordsSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html

# DOWNLOADER_MIDDLEWARES = {
#    # 'abskwords.middlewares.AbskwordsDownloaderMiddleware': 543,
#    'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,
# }
#
# ROTATING_PROXY_LIST = [
#     "89.187.177.91:80",
#     "128.199.222.224:3128",
#     "89.187.177.107:80",
#     "144.217.101.245:3129",
#     "162.214.92.202:80",
#     "159.65.171.69:80",
#     "208.80.28.208:8080",
#     "3.209.199.217:80",
#     # 'proxy1.com:8000',
#     # 'proxy2.com:8031',
#     # # ...
# ]

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
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
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'creepy.middlewares.CreepySpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'creepy.middlewares.CreepyDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'creepy.pipelines.CreepyPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
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
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
