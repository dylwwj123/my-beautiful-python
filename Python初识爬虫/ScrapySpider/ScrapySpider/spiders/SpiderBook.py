import re
import os
import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request
from ScrapySpider.items import ScrapyspiderItem

r'''
class MySpider(scrapy.Spider):

    name = "ScrapySpider"

    allowed_domains = ['23wx.cc']

    url = 'http://www.23wx.cc/class'

    def start_requests(self):

        for index in range(1,9):
            yield Request(self.url + r"/%s_1.html" %(index), self.parse)

    def parse(self, response):

        soup = BeautifulSoup(response.text, 'lxml')

        print(soup)

        li_book = soup.select(".l > ul > li")

        li_book.insert(0, "111")

        print(li_book)

        for book in li_book:
            aa = book.select_one('.s2 > a')
            bb = re.search(r'href="(.*?)"', r'%s' %(book.select_one('.s2 > a')))

            # pathUrl = "%s%s" % (os.path.abspath('.'), "/book1.txt")
            # with open(pathUrl, "a") as f:
            #     f.write('书名: %s\t目录: %s \n' %(aa.get_text(), 'http://www.23wx.cc/'+bb.group(1)))
'''

class MySpider(scrapy.Spider):

    name = "ScrapySpider"

    allowed_domains = ['bbs.hupu.com']

    url = 'https://bbs.hupu.com/22354603.html'

    def start_requests(self):

        yield Request(self.url, self.parse)

    def parse(self, response):

        soup = BeautifulSoup(response.text, 'lxml')

        # s1 = BeautifulSoup(re.search(r'<form action="(.*?)</form>', r'%s' %(soup.select_one(r".hidden")), re.S).group(0),'lxml')

        # s2 = s1.select('.floor').

        s1 = soup.find_all('form', method = 'post', action = '/masingle.php?action=delatc')

        print(s1)
