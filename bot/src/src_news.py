from typing import Optional, Generator
from bot.handler.contents_hanlder import Context
import datetime
import asyncio
from bs4 import BeautifulSoup
from urllib.request import urlopen
from functools import wraps


class SrcNews:
    def __init__(self, newsStand: Generator, chat_id: str = None, verbose=False):
        self._chat_id: Optional[str] = chat_id
        self._newsStand: Generator = newsStand
        self.verbose = verbose

    async def generator(self) -> Context:
        for news in self._newsStand:
            try:
                print(f"Start getting the feed from the {news.name}'s: {datetime.datetime.now()}")
                if news.src == 'web':
                    webGenerator = WebScraper().get_links_general(url=news.url, class_key=news.class_key,
                                                                  condition=lambda href: href.startswith(
                                                                      'http') or href.startswith('www'))
                    for content in webGenerator:
                        yield Context(label=f'{news.name}', contents=[content], botChatId=self._chat_id, dtype='msg')
                print(f"Finished obtaining the feed from the {news.name}'s : {datetime.datetime.now()}")
            except Exception as e:
                time_sleep = datetime.datetime.now()
                if self.verbose:
                    print(f'Error description -> {e}')
                    print(f"Raised a feed error from the {news.name}'s @{time_sleep}")
                await asyncio.sleep(60 * 10)  # 다음 반복까지 대기 시간
                time_awake = datetime.datetime.now()
                if self.verbose:
                    print(f"Awakened a feed error from the {news.name}'s @{time_awake}")
                    print(f'Total sleep time{time_awake - time_sleep}')


class WebScraper:
    def __init__(self, base_url=None):
        self.base_url = base_url

    def get_links_general(self, url, class_key: str = None, prefix=None, condition=lambda href: True):
        full_url = self.base_url + url if self.base_url else url
        soup = BeautifulSoup(urlopen(full_url), 'html.parser')
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