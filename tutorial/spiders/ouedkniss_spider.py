import scrapy

class OuedknissSpider(scrapy.Spider):

    name="ouedkniss"

    start_urls=[
        'https://www.ouedkniss.com/telephones'
    ]

    def parse(self, response, **kwargs):
        for annonce in response.css('div.annonce'):
            rightPanel  = annonce.css('div.annonce_right')
            leftPanel = annonce.css('ul.annonce_left')
            yield {
                'auteur': rightPanel.css('p.annonce_client_name a::text').get(),
                'date': rightPanel.css('p.annonce_date::text').get(),
                'wilaya':rightPanel.css('p.annonce_wilaya span.titre_wilaya::text').get(),

                'titre':leftPanel.css('li.annonce_titre h2::text').get(),
                'description':leftPanel.css('li.annonce_text span annonce_get_description span.annonce_description_preview::text').get(),
                'productid': leftPanel.css('li.annonce_text span annonce_get_description span.annonce_numero::text').get()

            }