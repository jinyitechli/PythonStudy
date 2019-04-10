import scrapy
from urllib import request
from bs4 import BeautifulSoup
from yiren.items import ManhuaItem


class ManhuaSprder(scrapy.Spider):
    name = 'manhua'
    allowed_domains = ['www.tohomh123.com']
    start_url = ['https://www.tohomh123.com/yirenzhixia/']

    def parse(self, response):

        bookmarks = response.xpath('//div[@id="chapterlistload"]')

        for bm in bookmarks:
            item = ManhuaItem()

            title = bm.xpath('.//ul/li/a/text()').extract()[0]
            href = bm.xpath('.//ul/li/a@href').extract()[0]
            src = bm.xpath('.//ul/li')

            item['title'] = title
















# url = 'https://www.tohomh123.com/yirenzhixia/'
#
# rsp = request.urlopen(url)
# content =rsp.read()
#
# soup = BeautifulSoup(content,'lxml')
#
# print(soup.prettify())
#
# print('#' * 20)
#
# a = soup.select("a[rel='nofollow'],a[target='_blank']")
#
# print(a)



