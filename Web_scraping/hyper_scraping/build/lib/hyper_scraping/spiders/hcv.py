import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser
class hcv(scrapy.Spider):
	name = 'crackit'
	start_urls = ['https://booksforum4u.blogspot.com/2019/07/hc-verma-best-book-to-prepare-for-jee_9.html'
				 ]
	pdf = []
	solns = []
	Names = []	
	def parse(self,response):
		data = response.xpath('/html/body/div[2]/div/div[5]/div[1]/div[1]/div[1]/div[1]/div/div[1]/article/div/div/div[4]/div/div[7]/span[1]/a/@href').extract_first()
		soln = response.xpath('/html/body/div[2]/div/div[5]/div[1]/div[1]/div[1]/div[1]/div/div[1]/article/div/div/div[4]/div/div[7]/span[1]/a/@href').extract_first()
		k = 1
		while data != None :
			name = response.xpath('/html/body/div[2]/div/div[5]/div[1]/div[1]/div[1]/div[1]/div/div[1]/article/div/div/div[4]/div/div[7]/span['+str(k)+']/a/span/text()').extract_first()
			data = response.xpath('/html/body/div[2]/div/div[5]/div[1]/div[1]/div[1]/div[1]/div/div[1]/article/div/div/div[4]/div/div[7]/span['+str(k)+']/a/@href').extract_first()
			soln = response.xpath('/html/body/div[2]/div/div[5]/div[1]/div[1]/div[1]/div[1]/div/div[1]/article/div/div/div[4]/div/div[7]/span['+str(k+1)+']/a/@href').extract_first()
			if data != None :
				getattr(hcv,'pdf').append(data)
				getattr(hcv,'Names').append(name)
				getattr(hcv,'solns').append(soln)
				k+=2
		for i in range(len(getattr(hcv,'solns'))):
			yield {'Name':getattr(hcv,'Names')[i]}
			yield {'chapter':getattr(hcv,'pdf')[i]}
			yield {'soln':getattr(hcv,'solns')[i]}
			print('\n')


