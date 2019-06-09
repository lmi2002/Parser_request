from helper import func

import re
from bs4 import BeautifulSoup as bs
import requests


class Autoklad:

    def __init__(self, num=None, brand=None):
        self.domain = 'https://www.autoklad.ua/'
        self.query_url = 'https://www.autoklad.ua/poisk/'
        self.num = str(num)
        self.brand_ex = str(brand)

    def _html_response(self):
        try:
            if requests.get(self.query_url + func.delete_sym(self.num)).status_code == 200:
                return bs(requests.get(self.query_url + func.delete_sym(self.num)).content, 'html.parser')
            return False
        except AttributeError:
            return False

    def _get_url_adress(self):
        if self._html_response:
            return self._html_response().find('span', class_='o-autocomplete-brand',
                                                string=re.compile(self.brand_ex, re.I)).parent['href']
        return False

    def _get_card_product_page(self):
        try:
            if self._get_url_adress():
                if requests.get(self.domain + self._get_url_adress()).status_code == 200:
                    return bs(requests.get(self.domain + self._get_url_adress()).content, 'html.parser')
            else:
                return False
        except AttributeError:
            return False

    def get_item(self):
        if self._get_card_product_page():
            card_product_page = self._get_card_product_page()
            price = card_product_page.find('span', class_='o-price-code').strong.get_text()
            term = card_product_page.find('span', class_='o-big-term').get_text()
            return price, term
        else:
            return 'error'


if __name__ == '__main__':
    ad = Autoklad(num='1-23-4-5', brand='febi')
    print(ad.get_item())