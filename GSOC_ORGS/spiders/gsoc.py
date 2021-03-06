# -*- coding: utf-8 -*-
import scrapy

import csv

class GsocSpider(scrapy.Spider):
    name = 'gsoc'
    start_urls = ['https://summerofcode.withgoogle.com/archive/2018/organizations/']
    def parse(self, response):
        for href in response.css('li.organization-card__container a.organization-card__link::attr(href)'):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback = self.parse_org)
        
    def parse_org(self,response):
        techno=getattr(self,'techno',None)
        tech=response.css("ul.org__tag-container li::text").extract()
        #if 'python' in tech:
        yield
        {
            'name':response.css('h3::text').extract()
            #'ideas_list':response.css('')
        }
        orgs=str(response.css('h3::text').extract_first())
        idea_list=response.css("md-button::attr(href)").extract_first()
        dict_stuff1={}
        dict_stuff2={}        
        dict_stuff2[orgs]=(idea_list)        
        dict_stuff1[orgs]=(tech)
        org_list=[]

        for x,y in dict_stuff1.items():
           if techno in y:
               org_list.append(x) 
        f=open("test.txt","w")
        for org in org_list:
           print(org,dict_stuff2[org])
