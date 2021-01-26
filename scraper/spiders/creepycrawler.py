

import scrapy
import json
from creepy.items import Article, SearchInfo
from scrapy.selector import Selector
from urllib.parse import urljoin as uj
from time import sleep
from scrapy.utils.response import open_in_browser


l = [
    [
        "title",
        "authors",
        "pub_type",
        "date",
        "doi_num",
        "doi_lnk",
        "id",
        "ful_txt_lnks",
        "abstract",
        "fetch_tail",
        "articles_available",
        "pages_available",
        "page_number",
        "articles_on_page",
    ],
    [
        "//*[contains(@id,'full-view-heading')]/h1/a/text()",
        "//*[contains(@id,'full-view-heading')]/div[2]/div/div/span/a/text()",
        "//*[@class='publication-type']/text()",
        "//*[contains(@id,'full-view-heading')]/div[1]/div/span[2]/text()",
        "//*[@class='id-link']/text()",
        "//*[@class='id-link']/@href",
        "//*[@title='ID']/text()",
        "//*[@class='full-text-links-list']/a/@href",
        "//*[contains(@class,'abstract')]/p/text()",
        "//*[@id='search-results']/section[1]/div[1]/div/@data-next-page-url",
        "//*[@id='search-results']/section[1]/div[1]/div/@data-results-amount",
        "//*[@id='search-results']/section[1]/div[1]/div/@data-pages-amount",
        "//*[@id='search-results']/section[1]/div[1]/div/@data-page-number"
        "//*[@id='search-results']/section[1]/div[1]/div/@data-chunk-ids",
    ],
]


class CreepSpider(scrapy.Spider):
    name = 'creepycrawler'

    allowed_domains = ['domain.com']
    start_urls = ['http://website.com']

    custom_settings = {
        'FEED_URI': 'file:///OUT.jsonl',
        'FEED_FORMAT': 'jsonlines',
        'FEED_EXPORT_ENCODING': 'utf-8',
        'FEED_EXPORT_INDENT': 2,
        'DOWNLOAD_DELAY': 6,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 1,
        'CONCURRENT_REQUESTS_PER_IP': 1,
        'HTTPCACHE_ENABLED': True,
        'COOKIES_ENABLED': False,
    
    }
    
    def parse(self, response, **kwargs):
        
        p = response.xpath
        
        sr = SearchInfo()
        sr['tot_art_avail'] =   p(l[1][10]).get()
        sr['tot_pgs_avail'] =   p(l[1][11]).get()
        sr['Page_No'] =         p(l[1][11]).get()
        sr['Page_url'] =        response.url
        sr['ids_on_pg'] =    p(l[1][12]).getall()
        sr['fetch_tail'] =      p(l[1][9]).get()

        yield sr
        
        overview = "//*[@class='results-article']/article"
        article = "//*[@id='search-results']/section[1]/div"
        sel_lst = "//*[@id='search-results']/section[1]/div"
        for info in [p(overview) for article in p(sel_lst).getall()]:
        
            a = Article()
            a['title'] =        p(l[1][0]).get()
            a['authors'] =      p(l[1][1]).getall()
            a['pub_type'] =     p(l[1][2]).get()
            a['date'] =         p(l[1][3]).get()
            a['doi_num'] =      p(l[1][4]).get()
            a['doi_lnk'] =      p(l[1][5]).get()
            a['id'] =    p(l[1][6]).get()
            a['url'] =   uj(response.url, a['id'])
            a['ful_txt_lnks'] = p(l[1][7]).getall()
            a['abstract'] =     p(l[1][8]).get()
            a['Page_No'] =      p(l[1][12]).get()
            a['r_url'] =        response.url
            
            yield a
        

