import scrapy

from ApartmentsScraper.items import ApartmentsscraperItem
from scrapy.loader import ItemLoader


class ApartmentSpider(scrapy.Spider):
    name = 'apartment'
    # allowed_domains = ['www.apartments.com/columbia-mo/']
    start_urls = ['https://www.apartments.com/columbia-mo/']

    def parse(self, response):
        apartments = response.css('li.mortar-wrapper')
        for apartment in apartments:
            loader = ItemLoader(item = ApartmentsscraperItem(), selector = apartment)
            loader.add_css('name', 'span.title')
            loader.add_css('pricing', 'p.property-pricing')
            loader.add_css('rent', 'span.property-rents')
            loader.add_css('bed', 'p.property-beds')
            loader.add_css('beds', 'span.property-beds')
            # loader.add_css('address', 'div.property-address')
            # item['name'] = apartment.css('span.title::text').get()
            # item['pricing'] = apartment.css('p.property-pricing::text').get()
            # item['bed'] = apartment.css('p.property-beds::text').get()
            yield loader.load_item()

        # next_page = response.css('a.next::attr(href)').extract_first()
        next_page = response.css('a.next').attrib['href']
        if next_page is not None:
            # next_page_url = f""
            yield response.follow(next_page, callback=self.parse)
