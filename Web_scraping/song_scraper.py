import scrapy
# from ..items import QuotetutorialItem
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser
class QuoteSpider(scrapy.Spider):
	name = 'dance'
	start_urls = ['https://www.songs-mp3.net'
				 ]
	def parse(self,response):
		# x = input('Please Input Song Name ::::::::::::::  ')
		x='Andhadhun'
		return FormRequest.from_response(response,formdata={'search':x},callback=self.temp)

	def temp(self,response):
		n = 1
		k='Start'
		links=[]
		link_type=[]
		name = []
		while k!='stop':
			b_tag = response.xpath('/html/body/div[2]/div[2]/div[2]/div[2]/div['+ str(n) +']/div[1]/ul/li[1]/a/span/text()').extract_first()
			a_tag = response.xpath('/html/body/div[2]/div[2]/div[2]/div[2]/div['+ str(n) +']/div[1]/ul/li[1]/a/@href').extract_first()
			type = response.xpath('/html/body/div[2]/div[2]/div[2]/div[2]/div[4]/div[1]/ul/li[2]/span/text()').extract_first()
			if a_tag == [] or a_tag==None :
				k='stop'
			else:
				links.append(a_tag)
				link_type.append(type)
				name.append(b_tag)
				yield {'a_tag':a_tag,'b_tag':b_tag}
				n+=1	
		x=int(input('Select Song Or the Movie Num('+str(n)+') == '))
		
		yield response.follow('https://www.songs-mp3.net'+links[x],callback=self.temper)
	def temper(self,response):
		if link_type[x]== 'Movies':
			n = 1
			k='Start'
			link = []
			while k!='stop':
				b_tag = response.xpath('/html/body/div[2]/div[2]/div/div[4]/div[2]/div/div[1]/div['+str(n)+']/div[2]/a/div/text()').extract_first()
				a_tag = response.xpath('/html/body/div[2]/div[2]/div/div[4]/div[2]/div/div[1]/div['+str(n)+']/div[2]/a/@href').extract_first()
				if a_tag == [] or a_tag==None :
						k='stop'
						yield n
					else:
						link.append(a_tag)
						yield {'a_tag':a_tag,'b_tag':b_tag}
						n+=1
				else :
					b_tag = response.xpath('/html/body/div[2]/div[2]/div/div[4]/div[2]/div/div[1]/div['+str(n)+']/div[2]/a/div/text()').extract_first()
					a_tag = response.xpath('/html/body/div[2]/div[2]/div/div[4]/div[2]/div/div[1]/div['+str(n)+']/div[2]/a/@href').extract_first()		