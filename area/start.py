# -*- coding: utf-8 -*-

from scrapy.crawler import CrawlerProcess
from area.spiders.area_spider import AreaSpider

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36'
})
process.crawl(AreaSpider)
process.start()
