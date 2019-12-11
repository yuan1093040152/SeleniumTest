# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field

class QiushiItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    head_image = Field()
    name = Field()
    content = Field()
    gender = Field()
    age = Field()
    zan_number = Field()
    commit_number = Field()
    commit_content = Field()
    image = Field()
    
    
