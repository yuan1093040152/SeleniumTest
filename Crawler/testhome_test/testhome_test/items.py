# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field,Item


class TesthomeItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = Field()
    ranking = Field()
    date = Field()
    company = Field()
    address = Field()
    post = Field()
    Respon = Field()
    attention = Field()
    concerned = Field()
    collect = Field()

