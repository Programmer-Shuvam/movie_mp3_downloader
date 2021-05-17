import scrapy
from time import strptime
from datetime import date
from ..items import yts_django


class Yify(scrapy.Spider):
    name = 'yts_django'
    yts_db = yts_django()

    def __init__(self, *args, **kwargs):
        x = kwargs.get('url')
        p = x.split(' ')
        list = []
        for i in range(len(p)):
            if i != (len(p) - 1):
                temp = p[i] + '%20'
                list.append(temp)
            else:
                list.append(p[i])
        x = ''.join(list)
        url = 'https://yts.mx/browse-movies/' + x + '/all/all/0/latest/0/all'
        self.start_urls = [url, ]

    confidential = {}

    def parse(self, response):
        name = response.xpath(
            '//*[contains(concat( " ", @class, " " ), concat( " ", "browse-movie-title", " " ))]/text()').extract()
        links = response.xpath(
            '//*[contains(concat( " ", @class, " " ), concat( " ", "browse-movie-title", " " ))]/@href').extract()
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
        yts_db = yts_django()

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

        yts_db["links"] = str(t)

        yts_db["cover"] = response.xpath(
            "/html/body/div[4]/div[3]/div[1]/div[2]/img/@src").extract_first()

        yts_db["screenshot"] = str(response.css(
            'a[class*="screenshot-group"]').xpath("@href").extract())

        yts_db["desc"] = response.xpath(
            "/html/body/div[4]/div[3]/div[4]/div[1]/p[2]/text()").extract_first()

        yts_db["duration"] = response.xpath(
            "/html/body/div[4]/div[3]/div[5]/div[1]/div[2]/div[3]/text()").extract()[1]

        yts_db["imdb"] = float(response.css(
            "span[itemprop='ratingValue']::text").extract_first())

        rel_date = response.css(
            "span[itemprop='dateCreated']>em::text").extract_first()

        if rel_date is not None:

            rel_date = rel_date.split(" at ")[0].split(" ")
            rel_date[2] = int(response.xpath(
                '/html/body/div[4]/div[3]/div[1]/div[4]/div[1]/h2[1]/text()').extract_first())
            rel_date[1] = int(rel_date[1].split(",")[0])
            rel_date[0] = strptime(rel_date[0].split(",")[
                                   0][:3], '%b').tm_mon
            rel_date.reverse()
            rel_date[1], rel_date[2] = rel_date[2], rel_date[1]
            rel_date[1], rel_date[2] = rel_date[2], rel_date[1]
            yts_db["rel_date"] = date(
                rel_date[0], rel_date[2], rel_date[1])

        else:

            rel_date = date.today()
            yts_db["rel_date"] = rel_date

        temp = Yify.confidential[str(
            response).split(" ")[-1].split(">")[0]]

        del Yify.confidential[str(response).split(
            " ")[-1].split(">")[0]]

        yts_db["name"] = temp

        yield yts_db
