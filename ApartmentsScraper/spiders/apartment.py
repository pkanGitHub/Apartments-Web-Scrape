import scrapy

from ApartmentsScraper.items import ApartmentsscraperItem

class ApartmentSpider(scrapy.Spider):
    name = 'apartment'
    # allowed_domains = ['www.apartments.com/columbia-mo/']
    start_urls = ['https://www.apartments.com/columbia-mo/']

    def parse(self, response):
        item = ApartmentsscraperItem()
        # apartments = response.css('div.placardContainer')
        apartments = response.css('li.mortar-wrapper')
        # apartments = response.css('li.mortar-wrapper').xpath('./')
        # apartments = response.xpath('//li')
        for apartment in apartments:
            # response.css('div.property-title::attr(title)').get()
            item['name'] = apartment.css('span.title::text').get()
            item['pricing'] = apartment.css('p.property-pricing::text').get()
            item['bed'] = apartment.css('p.property-beds::text').get()
            yield item