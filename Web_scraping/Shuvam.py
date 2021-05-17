import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser
from scrapy.crawler import CrawlerProcess
dict = {
	# 'BOT_NAME' : 'hyper_scraping',
	# 'SPIDER_MODULES' : ['hyper_scraping.spiders'],
	# 'NEWSPIDER_MODULE' : 'hyper_scraping.spiders',
	'ROBOTSTXT_OBEY' : False,
	'DOWNLOADER_MIDDLEWARES' : {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,},

	}
class Book(scrapy.Spider):
	name = 'dance'
	start_urls = ['https://fotofox.live/wp-admin/admin-ajax.php','https://fotofox.live/mr-teen-odisha-2020/?contest=photo-detail&photo_id=3959'
				 ]
	link_type=[]
	x=''
	naam = []			 
	def parse(self,response):
		# x = input('Please Input Song Name ::::::::::::::  ')
		dic = {'action':'vote_for_photo',
				'photo_id':'3959',
				'nonce_id': '3fa868e2ea',
				'option_id' : 'basic',
				}
		elses = {'contest': 'photo-detail','photo_id': '3959','vote': 'ok'}		

		
		return FormRequest.from_response(response,formdata=dic,callback=self.temp)
	def temp(self,response):
		open_in_browser(response)	
process = CrawlerProcess(settings=dict)	
process.crawl(Vote)
process.start()