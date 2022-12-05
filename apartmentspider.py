import scrapy
from items import ApartmentsscraperItem
from scrapy.loader import ItemLoader

class ApartmentSpider(scrapy.Spider):
    name = 'apartment'
    start_urls = ['https://www.apartments.com/columbia-mo/1']

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

        next_page = response.css('a.next').attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    # def run_spider(spider):
    #     process = CrawlerProcess(settings=
    #     {
    #         "FEEDS" : {
    #             'apartment.json': {'format': 'json', 'overwrite': True}
    #         },
    #     })
    #     process.crawl(ApartmentSpider)
    #     process.start()