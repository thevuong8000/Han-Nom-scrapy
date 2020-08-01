import scrapy

class han_nom_spider(scrapy.Spider):
    name = "Han_Nom"

    start_urls = [
        'https://hvdic.thivien.net/pop-nom'
    ]

    def parse(self, response):
        words = response.xpath('//a[@class="hv-word-item"]')

        for word in words:
            yield {
                'word': word.xpath('span/text()').get(),
                'meaning': word.xpath('@data-tippy-content').get()
            }