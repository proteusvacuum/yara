import scrapy

class PressureCookRecipes(scrapy.Spider):
    name = "pressurecookrecipes.com"
    start_urls = ['https://www.pressurecookrecipes.com/pressure-cooker-recipes/']

    def parse(self, response):
        for article in response.css('article'):
            yield self._parse_article(article)

        next_page = response.css('.next.page-numbers::attr(href)').extract_first()
        if next_page:
            yield scrapy.Request(next_page, callback=self.parse)

    def _parse_article(self, article):
        return {
            'title': article.css('.cb-post-title > a::text').extract_first(),
            'link': article.css('.cb-post-title > a::attr(href)').extract_first(),
            'img': article.css('.cb-img-fw img::attr(src)').extract_first(),
            'description': article.css('.cb-excerpt::text').extract_first(),
        }
