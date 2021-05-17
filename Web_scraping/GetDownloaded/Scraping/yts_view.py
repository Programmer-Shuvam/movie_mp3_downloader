import scrapy
# from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser
from scrapy.crawler import CrawlerProcess

# oggy = "Avengers"

dict = {
    # 'BOT_NAME' : 'hyper_scraping',
    # 'SPIDER_MODULES' : ['hyper_scraping.spiders'],
    # 'NEWSPIDER_MODULE' : 'hyper_scraping.spiders',
    'ROBOTSTXT_OBEY': False,
    'DOWNLOADER_MIDDLEWARES': {
        'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
        'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400, },

}


def thanos():
    if 5 == 2:
        pass
    else:
        from time import strptime
        oggy = "midway"

        dict = {
            # 'BOT_NAME' : 'hyper_scraping',
            # 'SPIDER_MODULES' : ['hyper_scraping.spiders'],
            # 'NEWSPIDER_MODULE' : 'hyper_scraping.spiders',
            'ROBOTSTXT_OBEY': False,
            'DOWNLOADER_MIDDLEWARES': {
                'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
                'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 500,
            },

        }

        class Yify(scrapy.Spider):
            name = 'Hollywood'
            t = ''
            x = oggy
            print(x)
            p = x.split(' ')
            list = []
            for i in range(len(p)):
                if i != (len(p) - 1):
                    temp = p[i] + '%20'
                    list.append(temp)
                else:
                    list.append(p[i])
            x = ''.join(list)
            # naam = []
            url = 'https://yts.mx/browse-movies/' + x + '/all/all/0/latest/0/all'
            start_urls = [url, ]
            data = {}
            mov_torr = []
            confidential = {}

            def parse(self, response):
                name = response.xpath(
                    '//*[contains(concat( " ", @class, " " ), concat( " ", "browse-movie-title", " " ))]/text()').extract()
                # Yify.naam = name
                links = response.xpath(
                    '//*[contains(concat( " ", @class, " " ), concat( " ", "browse-movie-title", " " ))]/@href').extract()
                print(name)
                print(links)
                for i in range(len(name)):
                    n = 1
                    while name.count(name[i]) > 1:
                        name[i] = name[i] + '__' + str(n)
                        n += 1
                for i in range(len(links)):
                    Yify.confidential[links[i]] = name[i]
                for i in links:
                    yield response.follow(i, callback=self.endgame)

            def endgame(self, response):
                # open_in_browser(response)
                # print("\n oggy ", str(response), "\n oggy ", end="\n")
                torrent_links = response.xpath(
                    '//*[(@id = "movie-info")]//*[contains(concat( " ", @class, " " ), concat( " ", "hidden-sm", " " ))]//a/@href').extract()
                Quality = response.xpath(
                    '//*[(@id = "movie-info")]//*[contains(concat( " ", @class, " " ), concat( " ", "hidden-sm", " " ))]//a/text()').extract()
                k = True
                n = 1
                t = {}

                while k:
                    size = response.xpath(
                        "/html/body/div[4]/div[3]/div[5]/div[" + str(n) + "]/div[1]/div[1]/text()").extract_first()

                    if size is None:
                        k = False
                    else:
                        t[Quality[n - 1]] = [torrent_links[n - 1], size]
                        n += 1

                t["cover"] = response.xpath(
                    "/html/body/div[4]/div[3]/div[1]/div[2]/img/@src").extract_first()
                t["screenshot"] = response.css(
                    'a[class*="screenshot-group"]').xpath("@href").extract()
                t["descrip"] = response.xpath(
                    "/html/body/div[4]/div[3]/div[4]/div[1]/p[2]/text()").extract_first()
                t["duration"] = response.xpath(
                    "/html/body/div[4]/div[3]/div[5]/div[1]/div[2]/div[3]/text()").extract()[1]
                t["imdb"] = float(response.css(
                    "span[itemprop='ratingValue']::text").extract_first())
                rel_date = response.css(
                    "span[itemprop='dateCreated']>em::text").extract_first().split(" at ")[0].split(" ")
                rel_date[2] = int(response.xpath(
                    '/html/body/div[4]/div[3]/div[1]/div[4]/div[1]/h2[1]/text()').extract_first())
                rel_date[1] = int(rel_date[1].split(",")[0])
                rel_date[0] = strptime(rel_date[0].split(",")[
                                       0][:3], '%b').tm_mon
                rel_date.reverse()
                rel_date[1], rel_date[2] = rel_date[2], rel_date[1]
                t["rel_date"] = rel_date
                temp = Yify.confidential[str(
                    response).split(" ")[-1].split(">")[0]]
                del Yify.confidential[str(response).split(
                    " ")[-1].split(">")[0]]
                Yify.confidential[temp] = t

        process = CrawlerProcess(settings=dict)
        process.crawl(Yify)
        process.start()
        print(Yify.confidential)
        month_name = "Jan"


# for i in Yify.confidential:
#     print(i + " : ", Yify.confidential[i], end="\n\n")


thanos()
