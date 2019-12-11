# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field


class SogouItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    activity_name = Field()
    meta_content = Field()
    js_name = Field()
    date = Field()
    essay = Field()
