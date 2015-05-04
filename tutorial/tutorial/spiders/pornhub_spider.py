## coding=utf-8
#import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')

import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from tutorial.items import DmozItem


class MySpider(CrawlSpider):
    name = 'pornhub_spider'
    allowed_domains = ['pornhub.com']
    #start_urls = ['http://www.pornhub.com/albums?page=1']
    start_urls = ['http://www.pornhub.com/album/5785431']

    rules = (
        # Extract links matching 'category.php' (but not matching 'subsection.php')
        # and follow links from them (since no callback means
        # follow=True by default).
        # Rule(
        # LinkExtractor(allow=('forumdisplay.php?fid=5.*', ))),

        # Rule(
        Rule(
            LinkExtractor(allow=('http://www\.pornhub\.com/albums\?page=\d*',))),

        Rule(LinkExtractor(
            allow=('/album/\d*',), restrict_xpaths=('//div[@class="photoAlbumListBlock"]'))),

        Rule(LinkExtractor(
            allow=('/photo/\d*',), restrict_xpaths=('//div[@class="photoAlbumListBlock"]/a')), callback='parse_item'),
        #Rule(LinkExtractor(
            #allow=('/photo/\d*',), restrict_xpaths=('//div[@class="photoAlbumListBlock"]/a'))),

        #Rule(LinkExtractor(
            #allow=('pic/\d*\.htm',), restrict_xpaths=('//div[@class="m8"]')), callback='parse_item'),


        # Extract links matching 'item.php' and parse them with the
        # spider's method parse_item
        # Rule(
        # LinkExtractor(allow=('viewthread.*', )), callback='parse_item'),
        # Rule(
        # LinkExtractor(allow=('viewthread\.php\?tid=.*',)),
        # callback='parse_item'),
    )

    # def start_requests(self):
    # return [scrapy.FormRequest("http://www.mayawell.com:8000/logging.php?action=login",
    # callback=self.login)]

    # def login(self, response):
    # here you would extract links to follow and return Requests for
    # each of them, with another callback
    #self.log('Hi, log in!')
    # return scrapy.FormRequest.from_response(response,
    # formdata={
    #'name': 'login', 'username': 'fuckmeyes', 'password': '123456'},
    # callback=self.check_login_response)

    # def check_login_response(self, response):
    # """Check the response returned by a login request to see if we are
    # successfully logged in.
    # """
    # if "fuckmeyes" in response.body:
    #self.log("Successfully logged in. Let's start crawling!")
    # return self.make_requests_from_url('http://www.mayawell.com:8000/forumdisplay.php?fid=5')
    # Now the crawling can begin..
    # self.initialized()
    # else:
    # self.log(
    #"Bad times, Something went wrong, we couldn't log in, so nothing happens.")
    # exit(1)

    def parse_item(self, response):
        self.log('Hi, this is an thread! %s' % response.url)
        item = DmozItem()
        item['image_urls'] = []
        for sel in response.xpath('//div[@class=\"thumbImage float-left\"]/a/img/@src'):
            item['image_urls'].append(sel.extract())
        return item
