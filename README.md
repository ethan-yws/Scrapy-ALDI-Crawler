# Scrapy ALDI Crawler
 Python Scrapy Crawler for aldi.com.au
 
 ##### Spider code: [aldiSpider.py](https://github.com/ethan-yws/Scrapy-ALDI-Crawler/blob/main/aldiCrawler/spiders/aldiSpider.py)
 ##### Output CSV: [aldi_products.csv](https://github.com/ethan-yws/Scrapy-ALDI-Crawler/blob/main/aldi_products.csv)
 
### Note
 This crawler collects the products infomation under Groceries category on aldi.com.au  
 Most products item can be found on the first-level subpages i.e. https://www.aldi.com.au/en/groceries/super-savers/  
 But for the submenu like "Baby" and "Liquor" etc, the product items are on the second-level subpages, thus, we need extract subsubmenu urls firstly  
 i.e. https://www.aldi.com.au/en/groceries/baby/ has no product items but https://www.aldi.com.au/en/groceries/baby/nappies-and-wipes/ etc.
 
### How to Run
```scrapy crawl aldi -O aldi_products.csv```  
This will generate an "aldi_products.csv" file in root path
