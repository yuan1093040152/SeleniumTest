# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field,Item


class ExampleItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    National_flag = Field()
    Area = Field()
    Population = Field()
    Iso = Field()
    Country = Field()
    Capital = Field()
    Continent = Field()
    Tld = Field()
    Currency_code = Field()
    Currency_name = Field()
    Phone = Field()
    Postal_code_format = Field()
    Postal_code_regex  = Field()
    Languages = Field()
    Neighbours = Field()
