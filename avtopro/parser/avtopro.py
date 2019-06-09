from helper import func

import re
import urllib.parse
from bs4 import BeautifulSoup as bs
import requests


class Avtopro:

    def __init__(self, num=None, brand=None):
        self.domain = 'https://avto.pro'
        self.query_url = 'https://avto.pro/api/v1/search/query'
        self.region = 1 # Европа
        self.num = str(num)
        self.brand_ex = str(brand)

    def _json_response(self):
        return requests.put(self.query_url, {"Query": func.delete_sym(self.num), "RegionId": self.region}).json()

    def _get_url_adress(self ):

        for i in self._json_response().get('Suggestions'):
            if re.search(self.brand_ex, i.get('Title'), re.I):
                return re.search(r'uri=/\S+/', urllib.parse.unquote(i.get('Uri'))).group(0)[4::]

    def get_result(self):
        html_response = requests.get(self.domain + self._get_url_adress()).content
        soup = bs(html_response, 'html.parser')
        print(soup.title.string)


if __name__ == '__main__':
    a = Avtopro(num='1-23-4-5', brand='febi')
    a.get_result()


