# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyspiderItem(scrapy.Item):

    #小说的名字
    name = scrapy.Field()

    #小说的作者
    author = scrapy.Field()

    #小说的地址
    address = scrapy.Field()

