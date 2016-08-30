# -*- coding: utf-8 -*-

from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose
from datetime import datetime
import re


def sub(text, loader_context):
    pattern = loader_context.get('pattern')
    repl = loader_context.get('repl')
    return re.sub(pattern, repl, text)


def parse_date(text, loader_context):
    fmt = loader_context.get('fmt', '%Y-%m-%d')
    return datetime.strptime(text, fmt.encode('utf-8'))


class AreaRevisionLoader(ItemLoader):
    default_output_processor = TakeFirst()
    update_date_in = MapCompose(sub, parse_date, pattern=ur'(?P<year>\d{4})年(?P<month>\d{1,2})月(?P<day>\d{1,2})日', repl='\g<year>-\g<month>-\g<day>')
    issue_date_in = MapCompose(parse_date)


class AreaLoader(ItemLoader):
    default_input_processor = MapCompose(unicode.strip)
    default_output_processor = TakeFirst()