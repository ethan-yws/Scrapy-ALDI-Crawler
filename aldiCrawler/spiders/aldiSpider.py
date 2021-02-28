import scrapy

class AldiSpider(scrapy.Spider):
    name = "aldi"
    start_urls = ['https://www.aldi.com.au/en/groceries/']

    ## Retrieve all submenu urls
    def parse(self, response):
        submenu_urls = response.xpath('//div[@class="productworld--list-item ym-gl ym-g16"]/a/@href').extract()
        
        # These 4 categories have no products displayed on their root page.
        # Hence we have to retrieve all the Sub-Subpages in order to crawl products info successfully
        special_cases = ['baby', 'laundry-household', 'liquor', 'pantry']
        
        for submenu_url in submenu_urls:
            if any(case in submenu_url for case in special_cases):
                yield response.follow(submenu_url, callback=self.crawl_page_special)
            else:
                yield response.follow(submenu_url, callback=self.crawl_page)

    
    # Function to crawl Sub-Subpages under special cases
    def crawl_page_special(self, response):
        sub_sub_urls = response.xpath('//div[contains(@class, "csc-textpic-imagecolumn")]/a/@href').extract()
        yield from response.follow_all(sub_sub_urls, callback=self.crawl_page)


    # Function to crawl products info on a page
    def crawl_page(self, response):
        # Crawl product info
        product_title = response.xpath('//div[@class="box--description--header"]/text()').extract()
        product_img = response.xpath('//div[@class="box m-text-image"]/div/div/img/@src').extract()
        price_value = response.xpath('//span[@class="box--value"]/text()').extract()
        price_decimal = response.xpath('//span[@class="box--decimal"]/text()').extract()
        price_per_unit = response.xpath('//span[@class="box--baseprice"]/text()').extract()

        # Create product info list
        for x in zip(product_title, product_img, price_value, price_decimal, price_per_unit):
            product_info = {
                'Product Title': x[0].strip(),
                'Product Image': x[1],
                'Pack Size': x[0].strip().split()[-1],
                'Price': x[2] + x[3],
                'Price Per Unit': x[4]
            }

            yield product_info