import scrapy
# from ..items import QuotetutorialItem
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser

class QuoteSpider(scrapy.Spider):
	name = 'piracy'
	start_urls = ['https://www1.thepiratebay3.to/',
				  'https://piratebaylive.com/',
				  'https://thepiratebay.zone/',
				 ]
	def parse(self,response):
		return FormRequest.from_response(response,formdata={'q':'gta v'},callback=self.temp)

	def temp(self,response):
		open_in_browser(response)
		# yield {'KAAAAAAAAAM KARRRRRRR RAHA HAI':'KAAAAAAAAAM KARRRRRRR RAHA HAI'}
		po = response.xpath('/html/body/main/div/section/ol/li[2]/span[4]/a/').extract()
		yo = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "alt", " " )) and (((count(preceding-sibling::*) + 1) = 4) and parent::*)]//*+[contains(concat( " ", @class, " " ), concat( " ", "vertTh", " " ))]//td').extract()
		# /html/body/main/div/section/ol/li[2]/span[4]/a
		yield {'whats this oggy':yo,'whats this jack':po}