import scrapy


class QuotesSpider(scrapy.Spider):
    name = "price"

    def start_requests(self):
        urls = [
            'https://www.amazon.com/Trijicon-Illuminated-Chevron-Rifle-Combat/dp/B0010PR0QG/',
            #'https://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'amazon-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')
