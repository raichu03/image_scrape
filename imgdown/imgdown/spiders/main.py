import scrapy


class imageSpider(scrapy.Spider):
    name = "imgdown"
    page = 2
    # start_urls = ['https://www.123rf.com/stock-photo/wild_elephants.html?page=1']
    start_urls = ['https://www.istockphoto.com/search/2/image?phrase=tigers%20india&page=1']

    def parse(self, response):
        # raw_image_urls = response.css('.ImageThumbnail__link img::attr(src)').getall()
        raw_image_urls = response.css('a picture img::attr(src)').getall()

        clean_image_urls = []

        for img_url in raw_image_urls:
            clean_image_urls.append(response.urljoin(img_url))


        yield{
            'image_urls' : clean_image_urls
        }

        # next_page = 'https://www.123rf.com/stock-photo/wild_elephants.html?page=' + str(imageSpider.page)
        next_page = 'https://www.istockphoto.com/search/2/image?phrase=tigers%20india&page=' + str(imageSpider.page)
        if imageSpider.page <= 100:
            imageSpider.page += 1
            yield response.follow(next_page, callback=self.parse)