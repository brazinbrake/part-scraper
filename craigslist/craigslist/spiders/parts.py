# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request


class PartsSpider(scrapy.Spider):
    #name to pass to crawl command
    name = 'parts'
    #ensures no unintended external links crawled
    allowed_domains = ['craigslist.org']
    #point to start crawling
    start_urls = ['https://jacksonville.craigslist.org/search/pta']

    def parse(self, response):
        #list keywords to search for
        kws = ['mustang', 'S197', 's197']
        #declare temp storage for urls already caught by a keyword
        urls = []
        #information wrapper
        parts = response.xpath('//p[@class="result-info"]')
        #get the desired info from each link's wrapper
        for part in parts:
            title = part.xpath('a/text()').extract_first()
            price = part.xpath('span[@class="result-meta"]/span[@class="result-price"]/text()').extract_first()
            url = part.xpath('a/@href').extract_first()
            #find out if the info matches what we want
            for kw in kws:
                if kw in title:
                    #if matching url is note a dupe, add it and yield
                    #useful if you have keywords like vw AND volkswagen for ex
                    if url not in urls:
                        urls.append(url)
                        yield{'Title': title, 'Price': price, 'URL': url}
        #do the parse on the next page
        relative_next_url = response.xpath('//a[@class="button next"]/@href').extract_first()
        absolute_next_url = response.urljoin(relative_next_url)

        yield Request(absolute_next_url, callback = self.parse)
