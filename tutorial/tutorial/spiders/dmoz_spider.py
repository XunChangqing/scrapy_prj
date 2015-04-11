import scrapy

from tutorial.items import DmozItem


class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["ifeng.com"]
    start_urls = [
        "http://news.ifeng.com/a/20150410/43524795_0.shtml"
    ]

    def parse(self, response):
        #item = DmozItem()
        #item['image_urls'] = {'http://y1.ifengimg.com/commonpage/0709/d_07.png'}
        #return item
        for sel in response.xpath('//img/@src'):
            item = DmozItem()
            item['image_urls'] = {sel.extract()}
            #print item['image_urls']
            #item['title'] = sel.xpath('a/text()').extract()
            #item['link'] = sel.xpath('a/@href').extract()
            #item['desc'] = sel.xpath('text()').extract()
            yield item
