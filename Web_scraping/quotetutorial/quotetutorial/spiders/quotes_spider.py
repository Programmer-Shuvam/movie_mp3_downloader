import scrapy
from ..items import QuotetutorialItem

class QuoteSpider(scrapy.Spider):
	name = 'quotes'
	start_urls = ['http://quotes.toscrape.com/',]
	def parse(self,response):
		items = QuotetutorialItem()
		all_div_quotes = response.css('div.quote')
		for i in all_div_quotes:
			title = i.css('span.text::text').extract()
			author = i.css('.author::text').extract()
			tag = i.css('.tag::text').extract()
			items['title'] = title
			items['author'] = author
			items['tag'] = tag
			# yield items