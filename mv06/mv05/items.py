# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Mv05Item(scrapy.Item):
    """
    < div class ="items-list" id="list_videos_common_videos_list_items" >

    < div class ="item" >
    """
    # define the fields for your item here like:
    name = scrapy.Field()
    id = scrapy.Field() #<a data-rt="1:2c8d63ec93028cf593fa06c9ab7db742:0:164936:1:" >
    ipx = scrapy.Field() #
    url = scrapy.Field() #<a href="" >
    durat = scrapy.Field() #<span class="durat info">31:31</span>
    channel = scrapy.Field()  #<span class="channel info"><span>Digital Playground</span></span>
    rating = scrapy.Field()  #<span class="rating info">
    downloadurl = scrapy.Field()
    length = scrapy.Field()

