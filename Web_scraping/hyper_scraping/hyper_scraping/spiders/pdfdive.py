import scrapy
# from ..items import QuotetutorialItem
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser

class QuoteSpider(scrapy.Spider):
	name = 'pdfs'
	start_urls = ['https://www.pdfdrive.com/',
				 ]
				 
	def parse(self,response):
		x=input('Enter the Book you are searching : \n (If it is possible will definitely help you provide that book)')
		return FormRequest.from_response(response,formdata={'q': x},callback=self.temp)
		# /html/body/div[3]/div[1]/div[1]/div[4]/ul/li[1]/div/div/div[1]/a/img
		# /html/body/div[3]/div[1]/div[1]/div[4]/ul/li[1]/div/div/div[2]/a/h2
		# /html/body/div[3]/div[1]/div[1]/div[4]/ul/li[1]/div/div/div[2]/div