# -*- coding: utf-8 -*-

import scrapy
from area.item_loaders import AreaLoader
from area.items import Area


class AreaSpider(scrapy.Spider):
    name = 'area'

    def start_requests(self):
        yield scrapy.Request('http://www.stats.gov.cn/tjsj/tjbz/xzqhdm/', self.parse_lastest_link)

    def parse_lastest_link(self, response):
        link = response.css('ul.center_list_contlist > li:first-child > a')
        href = link.css('::attr(href)').extract_first()
        if href:
            update_time = link.css('.cont_tit03::text').re_first(ur'\d{4}年\d{1,2}月\d{1,2}日')
            self.logger.info('update time: %s', update_time)
            issue_time = link.css('.cont_tit02::text').extract_first()
            self.logger.info('issue time: %s', issue_time)

            url = response.urljoin(href)
            yield scrapy.Request(url, self.parse_area)

    def parse_area(self, response):
        for row in response.xpath("//div[@class='TRS_PreAppend']/p"):
            loader = AreaLoader(Area(), row)
            loader.add_xpath('code', 'string(.)', re=r'^\d+')
            loader.add_xpath('name', 'string(.)', re=r'\w+$')
            yield loader.load_item()
