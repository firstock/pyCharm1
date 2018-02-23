import scrapy
class gitlabSpider(scrapy.Spider):
    name= gitlab
    allowed_domains= ["https://about.gitlab.com"]
    start_urls= [
        "https://about.gitlab.com/handbook/"
    ]

    def parse(self, response):
        filename= response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)