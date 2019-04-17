import scrapy

from e15_meiju.items import MeijuItem

class MeijuSpider(scrapy.Spider):

    name = "meiju"
    start_urls = ['https://www.meijutt.com/new100.html']

    def parse(self,response):

        movies = response.xpath('//ul[@class="top-list  fn-clear"]/li')
        print("mov:{0}".format(len(movies)))
        for movie in movies:

            item = MeijuItem()
            item['name'] = movie.xpath('./h5/a/@title').extract()[0]
            item['href'] = "https://www.meijutt.com" + movie.xpath('./h5/a/@href').extract()[0]
            item['tv'] = movie.xpath('./span[@class="mjtv"]/text()').extract()[0]
            item['state'] = movie.xpath('./span[@class="state1 new100state1"]/font/text()').extract()[0]
            item['mjjq'] = movie.xpath('./span[@class="mjjq"]/text()').extract()[0]
            yield item
            # print('name:{0}'.format(item['name']))
            # print('href:{0}'.format(item['href']))
            # print('tv:{0}'.format(item['tv']))
            # print('state:{0}'.format(item['state']))



