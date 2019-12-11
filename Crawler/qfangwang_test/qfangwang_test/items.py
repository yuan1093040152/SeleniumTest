# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field


class QfangwangItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    image = Field()
    title = Field()
    house = Field()
    size = Field()
    fitment = Field()
    floor = Field()
    orientation = Field()
    year = Field()
    district = Field()
    location = Field()
    estate = Field()
    watch = Field()
    tags = Field()
    price = Field()
    unitprice = Field()

    
    
