import scrapy


class NecklaceBotSpider(scrapy.Spider):
    name = 'necklace_bot'
    
    start_urls = ['https://www.houseofindya.com/zyra/necklace-sets/cat']


    def parse(self,response):
        set_urls=response.css('li::attr(data-url)').extract()

        for url in set_urls:
            yield scrapy.Request(url, callback = self.parse_dir_contents)



    def parse_dir_contents(self, response):

        title=response.xpath('//*[@id="wrapper"]/div[4]/div/div[2]/div[2]/h1/text()').extract_first()
        price=response.xpath('//*[@id="wrapper"]/div[4]/div/div[2]/div[2]/h4//text()').extract()[3].strip()
        description=response.xpath('//*[@id="tab-1"]/p/text()').extract_first()
        image=response.xpath('//*[@id="productsections"]/ul/li[1]/a/@data-image').extract_first()

        necklace_detail={
                'title':title,
                'price':price,
                'description':description,
                'image':image
                }

        yield necklace_detail