import scrapy

class JumiaSpider(scrapy.Spider):

    name="Jumia"

    start_urls=[
        'https://www.jumia.dz/epicerie/'
    ]

    def parse(self, response, **kwargs):

        for product in response.css('article.prd._fb.col.c-prd'):
            infoPanel = product.css('div.info')
            yield{
                'name':infoPanel.css('h3.name::text').get(),
                'price': infoPanel.css('div.prc::text').get()
            }
        
        next_page = response.css('a.pg[aria-label="Page suivante"]').xpath('@href').get()

        if next_page != None:
            yield scrapy.Request(url='https://www.jumia.dz'+next_page, callback=self.parse)


