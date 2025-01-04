from typing import AsyncGenerator
import datetime
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import logging
import requests
from bs4 import BeautifulSoup
from bot.definition_obj import Context


class NEWS:
    def __init__(self, chat_id:str, src:str, name:str, url:str, class_key:str, verbose:bool=False, *args, **kwargs):
        
        self.chat_id = chat_id
        self.src = src
        self.verbose = verbose
        self.name = name
        self.url = url
        self.class_key = class_key
        pass

    async def generator(self) -> AsyncGenerator:
            try:
                logging.info(f"Start getting the feed from the {self.name}'s: {datetime.datetime.now()}")
                if self.src == 'web':
                    web_generator = WebScraper().get_links_general(url=self.url, class_key=self.class_key,
                                                                  condition=lambda href: href.startswith(
                                                                      'http') or href.startswith('www'))
                    for article_link in web_generator:
                        title = get_page_title(article_link)
                        yield Context(label=f'{self.name}', title=title, link=article_link, bot_chat_id=self.chat_id, dtype='msg')
                logging.info(f"Finished obtaining the feed from the {self.name}'s : {datetime.datetime.now()}")
            except Exception as e:
                if self.verbose:
                    logging.error(f'Error description -> {e}')


class WebScraper:
    def __init__(self, base_url=None):
        self.base_url = base_url

    def get_links_general(self, url, class_key: str = None, prefix=None, condition=lambda href: True):
        full_url = self.base_url + url if self.base_url else url
        request = Request(full_url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urlopen(request).read()
        soup = BeautifulSoup(response, 'html.parser')
        elements = soup.find_all(attrs={'class': f'{class_key}'})
        for element in elements[::-1]:
            for link in element.find_all('a'):
                result = self.link_filter(link, prefix, condition)
                if result:
                    yield result

    def link_filter(self, link, prefix=None, condition=lambda x: True):
        href = link.attrs.get('href', '')
        if condition(href):
            return prefix + href if prefix else href

    def starts_with_condition(self, href, startswith='http'):
        return href.startswith(startswith)
    
def get_page_title( url):
    """
    주어진 URL에서 웹 페이지의 제목을 추출합니다.

    Args:
        url (str): 웹 페이지 URL.

    Returns:
        str: 페이지 제목. 오류 시 None 반환.
    """
    try:
        # HTTP 요청
        response = requests.get(url)
        response.raise_for_status()  # 상태 코드 확인

        # HTML 파싱
        soup = BeautifulSoup(response.text, 'html.parser')

        # 타이틀 추출
        title = soup.find('title').text
        return title
    except requests.exceptions.RequestException as e:
        print(f"오류 발생: {e}")
        return url