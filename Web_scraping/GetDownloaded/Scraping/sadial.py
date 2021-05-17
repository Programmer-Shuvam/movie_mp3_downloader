import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser
from scrapy.crawler import CrawlerProcess

# oggy = "Avengers"

dict = {
    # 'BOT_NAME' : 'hyper_scraping',
    # 'SPIDER_MODULES' : ['hyper_scraping.spiders'],
    # 'NEWSPIDER_MODULE' : 'hyper_scraping.spiders',
    'ROBOTSTXT_OBEY': False,
    'DOWNLOAD_DELAY': 5,
    'CONCURRENT_REQUESTS': 1,
    # 'handle_httpstatus_list': [401],
    'USER_AGENT': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36",
    # 'DOWNLOADER_MIDDLEWARES': {
    #     'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    #     'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400, },

}

# http://164.100.141.199:2222/api/student/student_profile/saveStudent
# Request Method: POST


class Masti(scrapy.Spider):
    name = 'masti'
    handle_httpstatus_list = [401]
    url = 'http://164.100.141.199:2222/api/student/student_profile/saveStudent'
    start_urls = ['http://emisosepa.odisha.gov.in/', ]

    def parse(self, response):
        open_in_browser(response)
        form_d = {
            'username': '21171302973-1',
            'password': 'Osepa@123',
            'grant_type': 'password',
            'ipaddress': '192.168.1.2',
        }
        api = "http://164.100.141.199:2222/api/auth/oauth/token"
        yield scrapy.FormRequest(api, callback=self.parse_2, method='POST', formdata=form_d)

    def parse_2(self, response):
        open_in_browser(response)
        params = {
            "actionStatus": "",
            "adharIdOrVidOrEid": "",
            "studentId": "",
            "schoolId": "21171302973",
            "previousSchoolId": "",
                                "dateOfAdm": "01-04-2019",
                                "sessionId": '3',
                                "admClassId": "11",
                                "sectionId": "1",
                                "admNo": "2019-20/0610",
                                "dob": "09-08-2002",
                                "fatherTitle": "Mr.",
                                "fatherName": "FAKIR MOHAN SAHOO",
                                "isFatherGuardian": "0",
                                "isFatherGuardian1": 'false',
                                "motherTitle": "Mrs.",
                                "motherName": "RASHMI REKHA PANDA",
                                "gender": "2",
                                "motherTongueId": '28',
                                "religionId": '2',
                                "socialCategoryId": '1',
                                "disabilityId": '2',
                                "isBPL": "0",
                                "isChildHomeless": "2",
                                "mobileNo": "8908920750",
                                "email": "debasmithmishra@yahoo.com",
                                "studentOptedId": "0",
                                "bankACNumber": "",
                                "branchIFSCCode": "",
                                "prevYearClassStatus": "",
                                "prevYearClassId": '10',
                                "mediumInstructionId": '19',
                                "streamId": '1',
                                "isActive": "1",
                                "createdByUserID": "24117",
                                "createdDate": "",
                                "updatedByUserID": "24117",
                                "updatedDate": "",
                                "uniqueStudentNumber": "",
                                "reasonIdForNotHavingAdhar": "123",
                                "studentFirstName": "DEBASMIT",
                                "studentMiddleName": "",
                                "studentLastName": "MISHRA",
                                "studentSubCategoryId": "",
                                "priorStatusId": "",
                                "stateId": "",
                                "habitationId": "71881",
                                "districtId": "406",
                                "blockId": "1032",
                                "parentAddress": "ANANTA VIHAR ,POKARIPUT",
                                "isQuickFill": "0",
                                "isDublicate": "0",
                                "currentSchoolType": "3",
                                "schoolType": "",
                                "eyeScreening": "2",
                                "diseaseDetected": "null",
                                "spectaclesSupplied": "null",
                                "schDistCode": '2117'
        }
        print("BINOD BINOD")
        yield scrapy.FormRequest(self.url, callback=self.endgame, method='POST', formdata=params)

    def endgame(self, response):
        yield response.follow('http://emisosepa.odisha.gov.in/', callback=self.parse)


process = CrawlerProcess(settings=dict)
process.crawl(Masti)
process.start()
