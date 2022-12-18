from bs4 import BeautifulSoup
from urllib.request import urlopen
from typing import Optional, Generator
from tools.telegram_bot.contents import Context
import datetime
import feedparser

class SrcEnergy:
    def __init__(self, newsEnergy: Generator, ChatId:str=None):
        self._ChatId:Optional[str]=ChatId
        self._newsEnergy:Generator =  newsEnergy

    
    # async def generator(self)-> Context:
    def generator(self)-> Context:
            try:
                for news in self._newsEnergy:
                    print(f'news= {news}')
                    if news.src == 'web': 
                        webGenerator = self._get_from_web_with_starts(news.url, news.attr_key, news.prefix, news.startswith)
                        for content in webGenerator:
                            yield Context(label=f'{news.name}', content=[content],  botChatId=self._ChatId, dtype='msg')
                    elif news.src =='rss':
                        for feed in feedparser.parse(news.url).entries:
                            summary=BeautifulSoup(f'{feed.title}\n\n{feed.description}', 'html.parser').text
                            yield Context(label = f"{news.name}", content=[feed.link], summary = [summary], botChatId=self._ChatId, dtype='msg', enable_translate=news.enable_translate)    
                                        

                print(f'energy_src_fin:{ datetime.datetime.now()}\n')  
                
            except Exception as e:
                print(f'energy_src_err:{ datetime.datetime.now()}')  
                print(f"energy_src error: {e}\n")
                pass
                    
    def _get_from_web_with_starts(self, url, attr_key, prefix=None, startswith='http')-> str:
        headlines = BeautifulSoup(urlopen(url), 'html.parser').find_all(attrs={'class':f'{attr_key}'})  # name은 태그 추출
        for headline in headlines:  ## html의 속성 부분을 추출
            for link in headline.find_all('a'):
                if 'href' in link.attrs and link.attrs['href'].startswith(startswith):
                        if prefix is not None:
                            # print(link.attrs['href'])
                            yield prefix + link.attrs['href']
                        else: 
                            yield link.attrs['href']

            