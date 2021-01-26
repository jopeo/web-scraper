
import json
import scrapy
from creepy.items import Article, SearchInfo
from scrapy.spiders import XMLFeedSpider
from urllib.parse import urljoin as uj
from time import sleep


# [
# "DUMMY_ZERO",
# 	"",  # "pg_number" added dynamically                                                                      # 1   "pg_number",
# 	".//*[@id='search-results']/section//*[@class='search-results-chunks']/div/@data-results-amount",         # 2   "num_art_avail",
# 	".//*[@id='search-results']/section//*[@class='search-results-chunks']/div/@data-pages-amount",           # 3   "pg_avail",
# 	".//*[@id='search-results']/section//*[@class='search-results-chunks']/div/@data-next-page-url",          # 4   "next_page",
# 	".//*[@id='search-results']/section//*[@class='search-results-chunks']/div/@data-page-number",            # 5   "this_pg_no",
# 	".//*[@id='search-results']/section//*[@class='search-results-chunks']/div/@data-chunk-ids",  # .getall() # 6   "art_on_sm_pg",
# 	".//article//h1/a//@data-ga-action",                                                                      # 7   "art_no",
# 	".//article//h1/a//@data-article-id",                                                                     # 8   "id",
# 	".//article//*[@class='full-view']//*[@class='cit']/text()",                                              # 9   "date",
# 	".//article//h1/a/text()",                                                                                # 10  "title",
# 	".//article//*[@class='full-view']//*[@class='publication-type']/text()",                                 # 11  "pub_type",
# 	".//article//*[@class='identifier doi']//*[@class='id-link']/text()",                                     # 12  "doi_num",
# 	".//article//*[@class='identifier doi']//*[@class='id-link']/@href",                                      # 13  "doi_lnk",
# 	"",  # "url2pub_pm" added dynamically                                                                     # 14  "url2pub_pm",
# 	".//article//*[@class='full-text-links-list']/a/@href",  # .getall()                                      # 15  "ful_txt_lnks",
# 	".//article//*[@class='full-view']//*[@class='full-name']/text()",  # .getall()                           # 16  "authors",
# 	".//article//*[(contains(@class,'abstract'))]//*[text()]/text()",                                         # 17  "abstract",
# 	# DIFFERENT SELECTOR FOR OUTSIDE OF ARTICLE ... OUTSIDE OF ARTICLE ONLY 1 ITERATION PER PAGE
# 	]


n = [
	"DUMMY_ZERO",
		"pg_number",
		"num_art_avail",
		"pg_avail",
		"next_page",
		"this_pg_no",
		
		"art_on_sm_pg",
		"art_no",
		"id",
		"date",
		"title",
		
		"pub_type",
		"doi_num",
		"doi_lnk",
		"url2pub_pm",
		"ful_txt_lnks",
		
		"authors",
		"abstract",
	]

tmp = [
	"DUMMY_ZERO",
		"pg_number",
		"num_art_avail",
		"pg_avail",
		"next_page",
		"this_pg_no",
		
		"art_on_sm_pg",
		"art_no",
		"id",
		"date",
		"title",
		
		"pub_type",
		"doi_num",
		"doi_lnk",
		"url2pub_pm",
		"ful_txt_lnks",
		
		"authors",
		"abstract",
	]

#  ".//*[@class='results-article']"  <--- start node

x = [
"DUMMY_ZERO",
	"",  # "pg_number" added dynamically                                                                                     # 1   "pg_number",
	"..//@data-results-amount",                                                                # 2   "num_art_avail",
	"..//@data-pages-amount",                                                                  # 3   "pg_avail",
	"..//@data-next-page-url",                                                                 # 4   "next_page",
	"..//@data-page-number",                                                                   # 5   "this_pg_no",
	"..//@data-chunk-ids",  # .getall()                                                        # 6   "art_on_sm_pg",
	".//article/.//*[@class='full-view']/h1/a//@data-ga-action",                                                       # 7   "art_no",
	".//article/.//*[@class='full-view']/h1/a//@data-article-id",                                                      # 8   "_id",
	".//article/.//*[@class='full-view']//*[@class='cit']/text()",                               # 9   "date",
	".//article/.//*[@class='full-view']/h1/a/text()",                                                                 # 10  "title",
	".//article/.//header/.//*[@class='full-view']//*[@class='publication-type']/text()",      # 11  "pub_type",
	".//article/.//*[@class='full-view']/.//ul/.//*[@class='identifier doi']/*[@class='id-link']/text()",                      # 12  "doi_num",
	".//article/.//*[@class='full-view']/.//ul/.//*[@class='identifier doi']//*[@class='id-link']/@href",                       # 13  "doi_lnk",
	"",  # "url2pub_pm" added dynamically                                                                                    # 14  "url2pub_pm",
	".//article/.//*[@class='full-text-links-list']/a/@href",  # .getall()                       # 15  "ful_txt_lnks",
	".//article/.//*[@class='full-view']//*[@class='full-name']/text()",  # .getall()            # 16  "authors",
	".//article/.//*[(contains(@class,'abstract'))]//*[text()]/text()",                          # 17  "abstract",
	# DIFFERENT SELECTOR FOR OUTSIDE OF ARTICLE ... OUTSIDE OF ARTICLE ONLY 1 ITERATION PER PAGE
	] \
	


class ElliSpider(scrapy.Spider):
	name = 'elli'
	allowed_domains = ['domain.com']  # TODO: DON'T FORGET TO FORMAT THE SEARCH CRITERIA  "
	s_url = "http://website.com"
	# delimiter = ';'
	# quotechar = '"'
	# headers = []
	
	custom_settings = {
		#  file:///
		'FEED_FORMAT': 'csv',
		# 'FEED_URI': 'e5_Ces.jsonl',
		'FEED_EXPORT_ENCODING': 'utf-8',
		'FEED_EXPORT_FIELDS': ["pg_number", "num_art_avail", "pg_avail", "next_page", "this_pg_no", "art_on_sm_pg", "art_no", "_id", "date", "title", "pub_type", "doi_num", "doi_lnk", "url2pub_pm", "ful_txt_lnks", "authors", "abstract"],
		# 'FEED_EXPORT_INDENT': 2,
		'DOWNLOAD_DELAY': 4,
		'CONCURRENT_REQUESTS_PER_DOMAIN': 1,
		'CONCURRENT_REQUESTS_PER_IP': 1,
		# 'HTTPCACHE_ENABLED': True,
		'COOKIES_ENABLED': False,
		
	}
	
	# iterator = "html"
	# itertag = "//*[@class='results-article']"
	
	def start_requests(self):
		yield scrapy.Request(self.s_url, self.parse)
		
		urls = (self.s_url + f"&{d}" for d in range(1, 21))
		for url in urls:
			yield scrapy.Request(url, self.parse)
	
	# noinspection PyTypeChecker
	def parse(self, response, **kwargs):
		f1 = lambda z: response.xpath(z)
		f2 = lambda z, y: z.xpath(y)
		
		for node in f1("//*[@class='results-article']"):
			
			a = Article()
			
			try:
				a['pg_number'] = int(str(response.url.rsplit('=', maxsplit=1)[1]))
			except Exception:
				a['pg_number'] = '1'
			
			a['num_art_avail']     =    f2(node, x[2]).get()
			a['pg_avail']          =    f2(node, x[3]).get()
			a['next_page']         =    f2(node, x[4]).get()
			a['this_pg_no']        =    f2(node, x[5]).get()
			a['art_on_sm_pg']      =    f2(node, x[6]).get()
			
			a['art_no']            =  f2(node, x[7]).get()
			a['id']         =  f2(node, x[8]).get()
			a['date']              =  f2(node, x[9]).get()
			a['title']             =  f2(node, x[10]).get()
			a['pub_type']          =  f2(node, x[11]).get()
			a['doi_num']           =  f2(node, x[12]).get()
			a['doi_lnk']           =  f2(node, x[13]).get()
			
			a['url2pub_pm']        =    uj(response.url, tmp[4])
			
			a['ful_txt_lnks']      =    list((nod.strip() for nod in f2(node, x[15]).getall() if nod is not None))
			a['authors']           =    list((nod.strip() for nod in f2(node, x[16]).getall() if nod is not None))
			a['abstract']          =    list((nod.strip() for nod in f2(node, x[17]).getall() if nod is not None))

			try:
				for v in (v for k, v in a.items()):
					if v is None:
						v = 'None'
					elif type(v) != list:
						v = v.strip()
			except Exception as e2:
				print(e2)
		
			yield a