import scrapy

class NomNomPaleo(scrapy.Spider):
    name = "nomnompaleo"
    start_urls = ['https://nomnompaleo.com/post/125878339293/my-top-paleo-pressure-cookerinstant-pot-recipes']

    def parse(self, response):
        # This site has one h3 node containing the title and link followed by 2
        # p nodes with the description and image
        articles = response.css('.entry-content h3')
        for article in articles:
            yield self._parse_article(response, article)

        next_page = response.css('.next.page-numbers::attr(href)').extract_first()
        if next_page:
            yield scrapy.Request(next_page, callback=self.parse)

    def _parse_article(self, response, article):
        #
        title = article.xpath('.//a//text()').extract_first()
        link = article.xpath('.//a/@href').extract_first()
        description = "".join(response.xpath(f"//h3[.//a//text() = '{title}']/following-sibling::p[1]//text()").extract())
        img = response.xpath(f"//h3[.//a//text() = '{title}']/following-sibling::p[2]/a/img/@src").extract_first()
        return {
            'source': self.name,
            'readable_source': 'Nom Nom Paleo',
            'title': title,
            'link': link,
            'img': f"https:{img}",
            'description': description,
        }
