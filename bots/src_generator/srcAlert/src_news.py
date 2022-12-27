                   
from bs4 import BeautifulSoup
from urllib.request import urlopen
from typing import Optional, Generator
from tools.telegram_bot.contents import Context
import datetime


class SrcNews:
    def __init__(self, newsStand: Generator, ChatId:str=None):
        self._ChatId:Optional[str]=ChatId
        self._newsStand:Generator =  newsStand

    
    async def generator(self)-> Context:
            try:
                for news in self._newsStand():
                    if news.src == 'web': 
                        webGenerator = self._get_from_web(news.url, news.attr_key)
                        for content in webGenerator:
                            yield Context(label=f'{news.name}', content=[content],  botChatId=self._ChatId, dtype='msg')
                        
                    elif news.src == 'webWithSelector': 
                        pass
                        # content = self._get_from_web_with_selector(news.url, news.attr_key)
                    elif news.src == 'webWithoutHttp': 
                        webGenerator = self._get_from_web_without_http(news.url, news.attr_key, news.prefix)
                        for content in webGenerator:
                            yield Context(label=f'{news.name}', content=[content],  botChatId=self._ChatId, dtype='msg')
                        
                    elif news.src == 'webLink': 
                        webGenerator = self._get_from_web_link(news.url, news.class_key)
                        for content in webGenerator:
                            yield Context(label=f'{news.name}', content=[content],  botChatId=self._ChatId, dtype='msg')
                            
                    elif news.src == 'webWithStarts': 
                        webGenerator = self._get_from_web_with_starts(news.url, news.attr_key, news.prefix, news.startswith)
                        for content in webGenerator:
                            yield Context(label=f'{news.name}', content=[content],  botChatId=self._ChatId, dtype='msg', enable_summary=True)
                    elif news.src == 'webWithStarts_labelTime': 
                        webGenerator = self._get_from_web_with_starts(news.url, news.attr_key, news.prefix, news.startswith)
                        label = self._get_labelTime_from_web(news.url)
                        for content in webGenerator:
                            yield Context(label=f'{news.name} {label}', content=[content],  botChatId=self._ChatId, dtype='msg')
  
                            
                print(f'news_src_fin:{ datetime.datetime.now()}\n')  
                
            except Exception as e:
                print(f'news_src_err:{ datetime.datetime.now()}')  
                print(f"news stand error: {e}\n")
                pass

    def _get_labelTime_from_web(self, url)-> str:
        html = BeautifulSoup(urlopen(url), 'html.parser')
        return f'{html.h1.text}_{html.time.text}'



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

    def _get_from_web(self, url, attr_key, prefix=None)-> str:
        headlines = BeautifulSoup(urlopen(url), 'html.parser').find_all(attrs={'class':f'{attr_key}'})  # name은 태그 추출
        for headline in headlines:  ## html의 속성 부분을 추출
            for link in headline.find_all('a'):
                if 'href' in link.attrs and (link.attrs['href'].startswith('http') or link.attrs['href'].startswith('www')):
                    if prefix is not None:
                        yield prefix + link.attrs['href']
                    else: 
                        yield link.attrs['href']
                
    def _get_from_web_with_selector(self, url, selector)-> str:
        headlines = BeautifulSoup(urlopen(url), 'html.parser').select(selector) 
        for headline in headlines:  ## html의 속성 부분을 추출
            if 'href' in headline.attrs:  #속성 중 링크만 추출
                yield headline.attrs['href']
    
    def _get_from_web_without_http(self, url, attr_key, prefix=None)-> str:
        headlines = BeautifulSoup(urlopen(url), 'html.parser').find_all(attrs={'class':f'{attr_key}'})  # name은 태그 추출
        for headline in headlines:  ## html의 속성 부분을 추출
            for link in headline.find_all('a'):
                if 'href' in link.attrs:  #속성 중 링크만 추출
                    if prefix is not None: 
                        yield prefix + link.attrs['href']
                    else: 
                        yield link.attrs['href']
        
    def _get_from_web_link(self, url, class_key)-> str:
        links = BeautifulSoup(urlopen(url), 'html.parser').find_all('a')
        for link  in links:
            if 'class' in link.attrs:  #속성 중 class만 추출
                if class_key in link.attrs['class']:
                    yield link.attrs['href']