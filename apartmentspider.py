import scrapy
from items import ApartmentsscraperItem
from scrapy.loader import ItemLoader

class ApartmentSpider(scrapy.Spider):
    name = 'apartment'
    # start_urls = ['https://www.apartments.com/columbia-mo/']

    # def start_requests(self):   
    #     yield scrapy.Request(f'https://www.apartments.com/{self.location}', self.parse)     

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
            yield loader.load_item()

        next_page = response.css('a.next').attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)