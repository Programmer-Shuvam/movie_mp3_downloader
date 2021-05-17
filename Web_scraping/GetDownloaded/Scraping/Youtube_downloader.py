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
class Yify(scrapy.Spider):
	name = 'Hollywood'
	t=''
	# x = 'Avengers'
	x=input('Please type the movie name : ')
	p=x.split(' ')
	list=[]
	for i in range(len(p)):
		if i != (len(p)-1) :
			temp=p[i]+'%20'
			list.append(temp)
		else:
 			list.append(p[i])
# print(p,list)
	x=''.join(list)
	naam = []	
	url  = 'https://yts.mx/browse-movies/'+x+'/all/all/0/latest/0/all'
	start_urls = [url,
				 ]
	def parse(self,response):
		# open_in_browser(response)
		name = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "browse-movie-title", " " ))]/text()').extract()	
		links = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "browse-movie-title", " " ))]/@href').extract()	
		yield {'name':name,'links':links}
		x=int(input('Please select the total movies are '+str(len(links))+' :  '))
		# x=1
		yield response.follow(links[x-1],callback=self.endgame)
	def endgame(self,response):
			# open_in_browser(response)
			torrent_links = response.xpath('//*[(@id = "movie-info")]//*[contains(concat( " ", @class, " " ), concat( " ", "hidden-sm", " " ))]//a/@href').extract()
			Quality = response.xpath('//*[(@id = "movie-info")]//*[contains(concat( " ", @class, " " ), concat( " ", "hidden-sm", " " ))]//a/text()').extract()
			# subtitle = 	response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "hidden-sm", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "button", " " ))]/@href').extract_first()
			yield {'Quality':Quality}
			yield {'torrent_links':torrent_links}
			# yield {'subtitle':subtitle}
process = CrawlerProcess(settings=dict)	
process.crawl(Yify)
process.start()
# https://r1---sn-4g5e6nzl.googlevideo.com/videoplayback?expire=1592590538&ei=aqzsXvHGGIrBsALs0KawCA&ip=5.180.220.11&id=o-AOmDoIH6NmTsMTntOcoMO8JWoq4kAmdl9a_dwQIX17_y&itag=137&aitags=133%2C134%2C135%2C136%2C137%2C160%2C242%2C243%2C244%2C247%2C248%2C278%2C298%2C299%2C302%2C303&source=youtube&requiressl=yes&vprv=1&mime=video%2Fmp4&gir=yes&clen=339492377&dur=629.000&lmt=1592559844908374&fvip=1&keepalive=yes&c=WEB&txp=5516222&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIhAOq2rv6MQAa_wHVyk3nb8AckxoADQVQTg33toL-0h2TlAiAEgbZMowuqtxquSVScn2Btt5nVBIu_ZW8JJCoQ9VJQBQ%3D%3D&video_id=kCvQYCdH9Uw&title=I+have+found+the+SECOND+iFerg+in+COD+Mobile...&rm=sn-aiges67e&req_id=a1b652c10682a3ee&ipbypass=yes&redirect_counter=2&cm2rm=sn-c0qlr7e&cms_redirect=yes&mh=Oi&mip=89.238.178.198&mm=34&mn=sn-4g5e6nzl&ms=ltu&mt=1592568988&mv=m&mvi=0&pl=24&lsparams=ipbypass,mh,mip,mm,mn,ms,mv,mvi,pl&lsig=AG3C_xAwRQIgbm8SHuQ-lk_jFFqrzkUxf3flIE2P6kbsG1jlNdlqPHgCIQCZoqy8Ky4l1npKt6wV7rBQO-zmhbnQUC_Wk6vXVme9Ag%3D%3D
# https://r1---sn-4g5e6nzl.googlevideo.com/videoplayback?expire=1592590538&ei=aqzsXvHGGIrBsALs0KawCA&ip=5.180.220.11&id=o-AOmDoIH6NmTsMTntOcoMO8JWoq4kAmdl9a_dwQIX17_y&itag=137&aitags=133%2C134%2C135%2C136%2C137%2C160%2C242%2C243%2C244%2C247%2C248%2C278%2C298%2C299%2C302%2C303&source=youtube&requiressl=yes&vprv=1&mime=video%2Fmp4&gir=yes&clen=339492377&dur=629.000&lmt=1592559844908374&fvip=1&keepalive=yes&c=WEB&txp=5516222&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIhAOq2rv6MQAa_wHVyk3nb8AckxoADQVQTg33toL-0h2TlAiAEgbZMowuqtxquSVScn2Btt5nVBIu_ZW8JJCoQ9VJQBQ%3D%3D&video_id=oxrSZoQDaTU&title=BYN+:+Video+Call+Gone+Wrong+Feat.+Sahil+Khan,+Dolly+Singh&rm=sn-aiges67e&req_id=a1b652c10682a3ee&ipbypass=yes&redirect_counter=2&cm2rm=sn-c0qlr7e&cms_redirect=yes&mh=Oi&mip=89.238.178.198&mm=34&mn=sn-4g5e6nzl&ms=ltu&mt=1592568988&mv=m&mvi=0&pl=24&lsparams=ipbypass,mh,mip,mm,mn,ms,mv,mvi,pl&lsig=AG3C_xAwRQIgbm8SHuQ-lk_jFFqrzkUxf3flIE2P6kbsG1jlNdlqPHgCIQCZoqy8Ky4l1npKt6wV7rBQO-zmhbnQUC_Wk6vXVme9Ag%3D%3D
