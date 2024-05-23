# Scrapy settings for scrapy_bosszp project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "scrapy_bosszp"

SPIDER_MODULES = ["scrapy_bosszp.spiders"]
NEWSPIDER_MODULE = "scrapy_bosszp.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "scrapy_bosszp (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en",
    "Cookie":"lastCity=101230100; __zp_seo_uuid__=adbd3150-a55c-46c7-aad7-19cb42ff9295; __g=-; "
             "__l=r=https%3A%2F%2Fcn.bing.com%2F&l=%2Fwww.zhipin.com%2Ffuzhou%2F&s=1&g=&s=3&friend_source=0; "
             "Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1716296282; wd_guid=b965da32-41ab-4831-8651-bf099fc5bb16; "
             "historyState=state; __fid=4ad66103c2e061985306b39d90108b2c; __c=1716296282; "
             "__a=28432526.1716296282..1716296282.7.1.7.7; "
             "__zp_stoken__=7419fw5x"
             "%2Bw4AlThojHsKOGBJ9GlDDgXR5w5VnwrBtwrjCh8OJZsOJwo7CusOVZnnDicOPwqrCg8OBw4ZdwrvCtcOKwq5hwrtfwqZbxIBuwpfCvcK8XMKsxKzEicOBxLfClFfDjcKoSDoSHREfHRIdER8dFxAdIxEeER0jESMkGB4kRzjCrnpCTFZBRWRjZBtRdXVddmUXZ1xST0FuYRgYQThNQU9Nw4hNw4wfw49Cw4ARw41Nw4dtQUdNQsOLwpY6PMONLh3DiBkew4JNI8ONwrhgw45CEcOSb8KVwqUuw4LDhEVJS8OCxYxKSCdIQk5OQk1VTkg3TcKAw5FtwonCkC7DgcKkMkIiVkhCVEBOSEJWQkhEQkp7MEhNMlYcIyQjETdNw4Few43DrEhC; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1716301341",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 "
                 "Safari/537.36 Edg/125.0.0.0",
    "Referer":"https://www.zhipin.com/"
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "scrapy_bosszp.middlewares.ScrapyBosszpSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    #"scrapy_bosszp.middlewares.ScrapyBosszpDownloaderMiddleware": 300,
    "scrapy_bosszp.middlewares.seleniumDownloaderMiddleware":1
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    "scrapy_bosszp.pipelines.ScrapyBosszpPipeline": 300,
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
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
