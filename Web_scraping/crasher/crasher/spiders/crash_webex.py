import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser


class crash_webex(scrapy.Spider):
    name = 'crash_webex'
    url = 'https://meetingsapac33.webex.com/meet/pr1665791889'
    start_urls = [url, ]

    def parse(self, response):

        data = {
            'device': "Browser",
            'displayName': "thanos aven",
            'email': "ahil@gmail.com",
            'locale': "en_US",
            'meetingUUID': "9d6577941ea37e08fd4053a986629804",
            'tfsid': "1jsbyZeP48"}
        return FormRequest.from_response('https://meetingsapac33.webex.com/wbxappapi/v1/meetings/join?siteurl=meetingsapac33', formdata=data, callback=self.temp)

    def temp(self, response):
        open_in_browser(response)
