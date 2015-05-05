## coding=utf-8
#import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')

import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from tutorial.items import DmozItem


class MySpider(CrawlSpider):
    name = 'fashion_haibao_spider'
    allowed_domains = ['haibao.com']
    start_urls = ['http://fashion.haibao.com/fashion/%e6%b3%b3%e8%a3%85/1.htm']
    #start_urls = ['http://pic.haibao.com/pic/11943935.htm']

    rules = (
        # Extract links matching 'category.php' (but not matching 'subsection.php')
        # and follow links from them (since no callback means
        # follow=True by default).
        # Rule(
        # LinkExtractor(allow=('forumdisplay.php?fid=5.*', ))),

        # Rule(
        # LinkExtractor(allow=('fashion\/泳装\/\d\.htm', ))),

        Rule(
            LinkExtractor(allow=('fashion/%e6%b3%b3%e8%a3%85/\d*\.htm',))),
        Rule(LinkExtractor(
            allow=('pic/\d*\.htm',), restrict_xpaths=('//div[@class="m8"]')), callback='parse_item'),


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
        for sel in response.xpath('//img/@bigsrc'):
            item['image_urls'].append(sel.extract())
        return item
