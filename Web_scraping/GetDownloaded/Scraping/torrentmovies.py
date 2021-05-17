import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.response import open_in_browser
from scrapy.http import FormRequest
dict = {
    # 'BOT_NAME' : 'hyper_scraping',
    # 'SPIDER_MODULES' : ['hyper_scraping.spiders'],
    # 'NEWSPIDER_MODULE' : 'hyper_scraping.spiders',
    'ROBOTSTXT_OBEY': False,
    'DOWNLOADER_MIDDLEWARES': {
        'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
        'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 40,
    },

}


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'https://torrentmovies.co/?s=lootcase&ixsl=1',
    ]

    '''def parse(self, response):
        for quote in response.css('.imag'):
            yield {
                'name': quote.css('.search-live-field::attr("title")').get(),
                'image': quote.css('.thumbnail img::attr("src")').get(),
            }'''

    def parse(self, response):
        open_in_browser(response)

    def parsjje(self, response):
        x = input('Enter the Movie you are searching : ')
        return FormRequest.from_response(response, formdata={'s': x}, callback=self.temp)

        '''next_page = response.css('.a-last a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)'''


process = CrawlerProcess(settings=dict)
process.crawl(QuotesSpider)
process.start()
