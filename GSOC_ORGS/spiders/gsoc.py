# -*- coding: utf-8 -*-
import scrapy



class GsocSpider(scrapy.Spider):
    name = 'gsoc'
    start_urls = ['https://summerofcode.withgoogle.com/archive/2018/organizations/']
    def parse(self, response):
        for href in response.css('li.organization-card__container a.organization-card__link::attr(href)'):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback = self.parse_org)
        
    def parse_org(self,response):
        tech=response.css("ul.org__tag-container li::text").extract()
        #if 'python' in tech:
        yield
        {
            'name':response.css('h3::text').extract()
            #'ideas_list':response.css('')
        }
        orgs=str(response.css('h3::text').extract_first())
        dict_stuff={}
        dict_stuff[orgs]=tech       
        for key,value in dict_stuff.items():
            f=open("final.txt","a")
            if "python" in value:
                f.write(key+"\n")
                
