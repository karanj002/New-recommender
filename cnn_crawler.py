import scrapy

class CNNSpider(scrapy.Spider):

    name = "cnn"

    def start_requests(self):
        urls = {"world-news": 'https://www.nytimes.com/section/world'
                , "sports": 'https://www.nytimes.com/section/sports',
                "politics": 'https://www.nytimes.com/section/politics'}  # create a dictionary for categories here

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        data = response.selector.xpath("//h2[@class = 'css-14g652u e1y0a3kv0']//a/@href").extract()

        list_cnn = []
        for l in data:
            sub_link = "https://edition.cnn.com" + l

            list_cnn.append(sub_link)
        print(list_cnn)