import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser
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


class Mrjatt(scrapy.Spider):
    name = 'dance'
    link_type = []
    x = ''
    naam = []
    start_urls = ['https://www.songs-mp3.net']
    # apalam chaplam

    def parse(self, response):
        x = input('Please Input Song Name ::::::::::::::  ')
        # x='Andhadhun'
        return FormRequest.from_response(response, formdata={'search': x}, callback=self.temp)

    def temp(self, response):
        # global link_type,x,naam
        n = 1
        k = 'Start'
        links = []
        while k != 'stop':
            b_tag = response.xpath(
                '/html/body/div[2]/div[2]/div[2]/div[2]/div[' + str(n) + ']/div[1]/ul/li[1]/a/span/text()').extract_first()
            a_tag = response.xpath(
                '/html/body/div[2]/div[2]/div[2]/div[2]/div[' + str(n) + ']/div[1]/ul/li[1]/a/@href').extract_first()
            type = response.xpath(
                '/html/body/div[2]/div[2]/div[2]/div[2]/div[' + str(n) + ']/div[1]/ul/li[2]/span/text()').extract_first()
            if a_tag == [] or a_tag is None:
                k = 'stop'
            else:
                links.append(a_tag)
                getattr(Mrjatt, 'link_type').append(type)
                getattr(Mrjatt, 'naam').append(b_tag)
                yield {'a_tag': a_tag, 'b_tag': b_tag}
                n += 1
        x = int(input('Select Song Or the Movie Num(' + str(n) + ') == '))
        # x=3
        Mrjatt.x = x - 1
        # yield {'x':getattr(Mrjatt,'x'),'naam':getattr(Mrjatt,'naam'),'type':getattr(Mrjatt,'link_type'),}
        yield response.follow('https://www.songs-mp3.net' + links[x - 1], callback=self.temper)

    def temper(self, response):
        # return {'x':getattr(Mrjatt,'x'),'naam':getattr(Mrjatt,'naam'),'type':getattr(Mrjatt,'link_type'),}
        # global link_type,x,naam
        n = 1
        k = 'Start'
        link = []
        msc_nm = []
        while k != 'stop':
            b_tag = response.xpath(
                '/html/body/div[2]/div[2]/div/div[4]/div[2]/div/div[1]/div[' + str(n) + ']/div[2]/a/div/text()').extract_first()
            a_tag = response.xpath(
                '/html/body/div[2]/div[2]/div/div[4]/div[2]/div/div[1]/div[' + str(n) + ']/div[2]/a/@href').extract_first()
            if a_tag == [] or a_tag is None:
                k = 'stop'
                yield n
            else:
                link.append(a_tag)
                msc_nm.append(b_tag)
                # yield {'a_tag':a_tag,'b_tag':b_tag}
                n += 1
        print(getattr(Mrjatt, 'link_type')[getattr(Mrjatt, 'x')])
        if getattr(Mrjatt, 'link_type')[getattr(Mrjatt, 'x')] == 'Movies':
            for i in msc_nm:
                yield i
            x = int(input('Number of responses are ' + str(len(link) + 1) + ': '))
            yield response.follow('https://www.songs-mp3.net' + link[x - 1], callback=self.endgame)
        else:
            # print(True)
            for i in range(len(msc_nm)):
                # print(True,msc_nm[i])
                if msc_nm[i] + '.mp3' == getattr(Mrjatt, 'naam')[getattr(Mrjatt, 'x')]:
                    # print(True)
                    # yield c
                    # print('i am in')
                    yield response.follow('https://www.songs-mp3.net' + link[i], callback=self.endgame)

    def endgame(self, response):
        song_link = response.xpath(
            '/html/body/div[2]/div[2]/div/div[3]/div[2]/div[2]/div[2]/a/@href').extract_first()
        yield {'this_is_the_download_link': song_link}


process = CrawlerProcess(settings=dict)
process.crawl(Mrjatt)
process.start()
