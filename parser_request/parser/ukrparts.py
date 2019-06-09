from helper import func

import re
from bs4 import BeautifulSoup as bs
import requests


class Ukrparts:

    def __init__(self, num=None, brand=None):
        self.query_url = 'https://ukrparts.com.ua/search/'
        self.num = str(num)
        self.brand_ex = str(brand)

    def _html_response(self):
        try:
            if requests.get(self.query_url + func.delete_sym(self.num)).status_code == 200:
                return bs(requests.get(self.query_url + func.delete_sym(self.num) + '/' ).content, 'html.parser')
            return False
        except AttributeError:
            return False

    def _get_card_product_page(self):
        try:
            if self._html_response:
                return self._html_response().find('div', class_='part_brand', string=re.compile(self.brand_ex, re.I)).parent
            return False
        except AttributeError:
            return False

    def get_item(self):
        if self._get_card_product_page():
            card_product_page = self._get_card_product_page()
            price = card_product_page.find('div', class_='price_min').get_text()
            term = card_product_page.find('div', class_='limitation').get_text()
            return price, term
        else:
            return 'error'


if __name__ == '__main__':
    up = Ukrparts(num='1-23-4-5', brand='febi')
    print(up.get_item())