import scrapy
import time

class ServicestatusSpider(scrapy.Spider):
    name = "ServiceStatus"
    start_urls = ["https://yoururl"]

    def parse(self, response):
        status = {
            'latest_status': response.css('[id="statusbar_text"]::text').extract_first(),
            'updated_ago' : response.css('[id="updated_ago"]::text').extract_first()
        }
        print("{} :: {}".format(time.strftime("%Y-%m-%d %H:%M:%S"), status))
        time.sleep(15)
        yield response.follow(self.start_urls[0], callback = self.parse, dont_filter = True) 
        # yield scrapy.Request(url = self.start_urls[0], callback = self.parse, dont_filter=True)
