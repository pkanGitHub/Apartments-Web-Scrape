# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags

def remove_dollar_symbol(value):
    return value.replace('$', '').strip()

class ApartmentsscraperItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = TakeFirst())
    pricing = scrapy.Field(input_processor = MapCompose(remove_tags, remove_dollar_symbol), output_processor = TakeFirst())
    bed = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = TakeFirst())
    rent = scrapy.Field(input_processor = MapCompose(remove_tags, remove_dollar_symbol), output_processor = TakeFirst())
    beds = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = TakeFirst())
