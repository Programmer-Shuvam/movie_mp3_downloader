import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser
from scrapy.crawler import CrawlerProcess
from time import sleep
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
	name = 'read'
	start_urls = ['https://www.pdfdrive.com'
				 ]
	x=''
	naam = []			 
	def parse(self,response):
		x = "Chetan Bhagat"
		#x = input('Please Input Book Name ::::::::::::::  ')
		return FormRequest.from_response(response,formdata={'q':x},callback=self.temp)
	def temp(self,response):
		n = 1
		links = []
		k = "start"
		while k!='stop':
			name = response.xpath('/html/body/div[3]/div[1]/div[1]/div[4]/ul/li['+str(n)+']/div/div/div[2]/a/h2/text()').extract_first()
			href = response.xpath('/html/body/div[3]/div[1]/div[1]/div[4]/ul/li['+str(n)+']/div/div/div[2]/a/@href').extract_first()
			if href == None:
				k = 'stop'
			else:
				links.append(href)
				getattr(Book,'naam').append(name)
				yield {'Name':name,'href':href}
				n+=1	 
		# x=int(input('Select Book('+str(len(links))+') == '))
		# x=3
		# Book.x=x-1
		# yield {'x':getattr(Mrjatt,'x'),'naam':getattr(Mrjatt,'naam'),'type':getattr(Mrjatt,'link_type'),}
		yield response.follow('https://www.pdfdrive.com'+links[3-1],callback=self.temper)
	def temper(self,response):
		download_link = response.xpath('//*[@id="download-button-link"]/@href').extract_first()				
		yield {'link':download_link}
		yield response.follow('https://www.pdfdrive.com'+download_link,callback=self.endgame)
	def endgame(self,response):
		# sleep(5)
		open_in_browser(response)
		download_link = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "btn-user", " " ))]/@href').extract()
		# while download_link	!= None:
				# download_link = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "btn-user", " " ))]/@href').extract()				
		yield {"here's your pdf waiting for you ":download_link}	
process = CrawlerProcess(settings=dict)	
process.crawl(Book)
process.start()
