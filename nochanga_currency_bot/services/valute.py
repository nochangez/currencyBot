# coding: utf-8

import requests
from bs4 import BeautifulSoup as soupy


class Valute():
    def __init__(self):
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 YaBrowser/20.9.3.136 Yowser/2.5 Safari/537.36"}
        self.url = "https://www.banki.ru/products/currency/"

        self.request = requests.get(url=self.url, headers=self.headers)
        self.soup = soupy(self.request.content, 'html.parser')

    def get_dollar(