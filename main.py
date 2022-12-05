from apartmentspider import ApartmentSpider
from scrapy.crawler import CrawlerProcess

def run_spider(spider):
    process = CrawlerProcess(settings=
    {
        "FEEDS" : {
            'apartment.json': {'format': 'json', 'overwrite': True}
        },
    })
    process.crawl(spider)
    process.start()

def main():
    run_spider(ApartmentSpider)

main()