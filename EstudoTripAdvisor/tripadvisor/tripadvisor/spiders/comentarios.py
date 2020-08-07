import scrapy
from tripadvisor.items import TripadvisorItem

class ComentariosSpider(scrapy.Spider):
    name = 'comentarios'
    allowed_domains = ['https://www.tripadvisor.com.br/']
    start_urls = ['https://www.tripadvisor.com.br/Attraction_Review-g303441-d553398-Reviews-Parque_Barigui-Curitiba_State_of_Parana.html']

    def parse(self, response):
        item = TripadvisorItem()
        quadros_de_comentarios = response.xpath("//div[@class='Dq9MAugU T870kzTX LnVzGwUB']")
        
        for quadro in quadros_de_comentarios:
            item['autor_comentario'] = quadro.xpath(".//span/a[@class='ui_header_link _1r_My98y']/text()").get()
            item['autor_endereco'] = quadro.xpath('.//span[@class="default _3J15flPT small"]/text()').get()
            item['comentario_titulo'] = quadro.xpath('.//div[@class="glasR4aX"]/a//span/text()').get()
            item['comentario_corpo'] = quadro.xpath('.//q[@class="IRsGHoPm"]/span/text()').get()
            item['comentario_data'] = quadro.xpath('.//span[@class="_34Xs-BQm"]/text()').get()

            yield item

        next_page = response.xpath('//a[@class="ui_button nav next primary " and text() = "Próximas"]/@href').get()
        if next_page:
            yield response.follow(url=next_page, callback = self.parse)    


        
