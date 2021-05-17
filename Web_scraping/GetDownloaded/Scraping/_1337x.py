import scrapy
# from scrapy.http import FormRequest
# from scrapy.utils.response import open_in_browser
from scrapy.crawler import CrawlerProcess
dict = {
    # 'BOT_NAME' : 'hyper_scraping',
    # 'SPIDER_MODULES' : ['hyper_scraping.spiders'],
    # 'NEWSPIDER_MODULE' : 'hyper_scraping.spiders',
    'ROBOTSTXT_OBEY': False,
    'DOWNLOADER_MIDDLEWARES': {
        'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
        'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400, },

}


class _1337x_(scrapy.Spider):
    name = 'yes'
    href = []
    # x=input('Please type the Torrent name : ')
    # x = input("Bolo chahi: ")
    x='USS Indianapolis: Men of Courage'
    p = x.split(' ')
    list = []
    for i in range(len(p)):
        if i == 0 and len(p) >= 2:
            temp = p[i] + '%20'
            list.append(temp)
        elif i != (len(p) - 1):
            temp = p[i] + '%20'
            list.append(temp)
        else:
            list.append(p[i])
# print(p,list)
    x = ''.join(list)
    lin = []
    nim = []
    naam = []
    url = 'https://www.1377x.to/search/' + x + '/1/'
    # https://1337x.gd/search/call+of+duty/1/
    start_urls = [url,
                  ]

    def parse(self, response):
        names = response.css('.icon+ a::text').extract()
        links = response.css('.icon+ a')
        for i in range(len(links)):
            links[i] = links[i].xpath('@href').extract_first()
        yield {"y": names}
        _1337x_.lin = links
        _1337x_.nim = names
        for i in range(len(names)):
            yield response.follow(links[i], callback=self.inside)
            # yield {'name':names[i],'link':links[i],
            # 'magnet':getattr(_1337x_,'href')[i],}
            # print(getattr(_1337x_,'href'))
        # yield {'name':names[i],'link':links[i],
        # 	'magnet':getattr(_1337x_,'href')[i],}

    def inside(self, response):
        magnet = response.xpath(
            '/html/body/main/div/div/div/div[2]/div[1]/ul[1]/li[1]/a/@href').extract_first()
        getattr(_1337x_, 'href').append(magnet)
        print(getattr(_1337x_, 'href'))

        # print(magnet)


process = CrawlerProcess(settings=dict)
process.crawl(_1337x_)
process.start()
