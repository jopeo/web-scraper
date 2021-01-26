# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class Article(Item):
    
    pg_number = Field()
    num_art_avail = Field()
    pg_avail = Field()
    next_page = Field()
    this_pg_no = Field()
    
    art_on_sm_pg = Field()
    art_no = Field()
    id = Field()
    date = Field()
    title = Field()
    
    pub_type = Field()
    doi_num = Field()
    doi_lnk = Field()
    url2pub_pm = Field()
    ful_txt_lnks = Field()
    
    authors = Field()
    abstract = Field()


# not used by elli
class SearchInfo(Item):
    tot_art_recorded = Field()
    tot_no_pgs_vis = Field()
    tot_art_avail = Field()
    tot_pgs_avail = Field()
    pgs_visited = Field()
    Page_No = Field()
    Page_url = Field()
    ids_on_pg = Field()
    fetch_tail = Field()