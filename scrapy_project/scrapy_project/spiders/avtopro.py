# -*- coding: utf-8 -*-

import scrapy

import csv


class ExistSpider(scrapy.Spider):
    name = "exist_tenty_nakidki"



    def parse(self, response):

        print(scrapy.Request('https://avto.pro/api/v1/search/query', method='PUT', body={"Query": "12345", "RegionId": "1"}, callback=self.parse_product_page, encoding="utf-8"))


    def parse_product_page(self, response):
        pass
