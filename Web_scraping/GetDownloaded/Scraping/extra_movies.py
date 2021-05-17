import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser
from scrapy.crawler import CrawlerProcess
dict = {
    # 'BOT_NAME' : 'hyper_scraping',
    # 'SPIDER_MODULES' : ['hyper_scraping.spiders'],
    # 'NEWSPIDER_MODULE' : 'hyper_scraping.spiders',
    'ROBOTSTXT_OBEY': False,
    'CONCURRENT_REQUESTS': 1,
    'DOWNLOAD_DELAY': 12,
    'PROXY_POOL_ENABLED': True,
    'COOKIES_ENABLED': True,
    'USER_AGENT': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Mobile Safari/537.36',
    'DOWNLOADER_MIDDLEWARES': {
        'scrapy_proxy_pool.middlewares.ProxyPoolMiddleware': 610,
        'scrapy_proxy_pool.middlewares.BanDetectionMiddleware': 600, },

}


class extramovies(scrapy.Spider):
    name = 'extramovies'
    start_urls = ['http://extramovies.casa',
                  ]

    def parse(self, response):
        # x = input('Enter the Movie you are searching : ')
        x = "money heist season 4"
        return FormRequest.from_response(response, formdata={'s': x}, callback=self.temp)
        # open_in_browser(response)

    def temp(self, response):
        n = 2
        # html/body/div[1]/div[4]/div/div[1]/div[2]/div[2]/a/img
        k = 'Start'
        links = []
        link_type = []
        name = []
        # item = HyperScrapingItem()
        while k != 'stop':
            Name = response.xpath(
                '/html/body/div[1]/div[4]/div/div[1]/div[' + str(n) + ']/article/h2/a/text()').extract_first()
            href = response.xpath(
                '/html/body/div[1]/div[4]/div/div[1]/div[' + str(n) + ']/div[2]/a/@href').extract_first()
            image_url = response.xpath(
                '/html/body/div[1]/div[4]/div/div[1]/div[' + str(n) + ']/div[2]/a/img/@src').extract_first()
            if href == [] or href is None:
                k = 'stop'
                if n != 2:
                    for i in links:
                        yield response.follow(i, callback=self.temper)
            else:
                links.append(href)
                link_type.append(type)
                name.append(Name)
                # item['image_urls']=image_url
                yield {'Name': Name, 'href': href, 'img': image_url}
                n += 1
        # open_in_browser(response)

    def temper(self, response):
        # open_in_browser(response)
        # <a class="buttn torrent" href="/torrent.php?id=N2Y3YjY4ZWYxNzkyNzk3N2E3YzI4ODI2MmE2YzExNmRkZTc4NDUzNw==" target="_blank" rel="noopener noreferrer">Torrent Download</a>
        torrent_id = response.xpath(
            '/html/body/div[1]/div[4]/div/div[1]/article/div[2]/div[5]/p[2]/a/@href').extract_first()
        #                            /html/body/div[1]/div[4]/div/div[1]/article/div[2]/div[5]/p[2]/a
        # yield {'torrent':torrent_id}
        screen_shot = []
        n = 1
        k = True
        descrip = response.xpath(
            '/html/body/div[1]/div[4]/div/div[1]/article/div[2]/p[6]/text()').extract_first()
        imdb = response.xpath(
            '/html/body/div[1]/div[4]/div/div[1]/article/div[2]/div[1]').extract_first()
        # while k :
        #   screen_pic = response.xpath('/html/body/div[1]/div[4]/div/div[1]/article/div[2]/div[3]/div[2]/img['+str(n)+']/@src').extract_first()
        #   if screen_pic == None:
        #       k = False
        #   else:
        #       screen_shot.append(screen_pic)
        # yield {'screen_pic':screen_pic,'description':descrip,}
        yield response.follow('http://extramovies.casa' + torrent_id, callback=self.temperer)

        # quit()
        # http://extramovies.casa/
    def temperer(self, response):
        gate = response.xpath('/html/body/div[3]/a[1]/@href').extract_first()
        yield response.follow(gate, callback=self.endgame)
        yield {}
        # open_in_browser(response)
        # count+=1

    def endgame(self, response):
        open_in_browser(response)
        magnet = response.xpath(
            '/html/body/div[2]/div/div[2]/div/div/div[2]/ul/div[2]/a/@href').extract_first()
        torrent_file = response.xpath(
            '/html/body/div[2]/div/div[2]/div/div/div[2]/ul/div[1]/a/@href').extract_first()
        yield {'magnet': magnet, }
        yield {'torrent_file': torrent_file}

        # open_in_browser(response)
process = CrawlerProcess(settings=dict)
process.crawl(extramovies)
process.start()
