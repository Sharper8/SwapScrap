# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import scrapy

class SneakersSpider(scrapy.Spider):
    name = 'sneakers'
    start_urls = ['https://example.com/sneakers']

    def parse(self, response):
        for sneaker in response.css('h3.DropCard__CardBrandName-sc-1f2e4y6-5.fwtNMB'):
            yield {
                'nom': sneaker.css('::text').get()
            }
