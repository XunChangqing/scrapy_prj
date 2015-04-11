# -*- coding: utf-8 -*-

# Scrapy settings for tutorial project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'tutorial'

SPIDER_MODULES = ['tutorial.spiders']
NEWSPIDER_MODULE = 'tutorial.spiders'

ITEM_PIPELINES = {'scrapy.contrib.pipeline.images.ImagesPipeline': 1}
IMAGES_STORE = 'scrapy_pics'
IMAGES_EXPIRES = 90
IAGES_THUMBS = {
    'small': (50, 50),
    'big': (270, 270),
}
DOWNLOADER_MIDDLEWARE = [ 'scrapy.contrib.downloadermiddleware.httpauth.HttpAuthMiddleware']
#IMAGES_MIN_HEIGHT = 110
#IMAGES_MIN_WIDTH = 110
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tutorial (+http://www.yourdomain.com)'
