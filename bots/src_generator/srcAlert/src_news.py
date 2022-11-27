from bs4 import BeautifulSoup
from urllib.request import urlopen
from typing import Optional, Generator
from tools.telegram_bot.contents import Context



class SrcNews:
    def __init__(self, newsStand: Generator, ChatId:str=None):
        self._ChatId:Optional[str]=ChatId
        self._newsStand:Generator =  newsStand

    
    async def generator(self)-> Context:
            try:
                for news in self._newsStand:
                    if news.src == 'web': 
                        webGenerator = self._get_from_web(news.url, news.attr_key)
                        for content in webGenerator:
                            yield Context(content=[content], label=f'{news.name}', botChatId=self._ChatId, dtype='msg')
                        
                    elif news.src == 'webWithSelector': 
                        pass
                        # content = self._get_from_web_with_selector(news.url, news.attr_key)
                    elif news.src == 'webWithoutHttp': 
                        webGenerator = self._get_from_web_without_http(news.url, news.attr_key, news.prefix)
                        for content in webGenerator:
                            yield Context(content=[content], label=f'{news.name}', botChatId=self._ChatId, dtype='msg')
                        
                    elif news.src == 'webLink': 
                        webGenerator = self._get_from_web_link(news.url, news.class_key)
                        for content in webGenerator:
                            yield Context(content=[content], label=f'{news.name}', botChatId=self._ChatId, dtype='msg')
            except Exception as e:
                print(f"news stand error: {e}")
                pass



    def _get_from_web(self, url, attr_key, prefix=None)-> Context:
        headlines = BeautifulSoup(urlopen(url), 'html.parser').find_all(attrs={'class':f'{attr_key}'})  # name은 태그 추출
        for headline in headlines:  ## html의 속성 부분을 추출
            for link in headline.find_all('a'):
                if 'href' in link.attrs and (link.attrs['href'].startswith('http') or link.attrs['href'].startswith('www')):
                    if prefix is not None:
                        yield prefix + link.attrs['href']
                    else: 
                        yield link.attrs['href']
                
    def _get_from_web_with_selector(self, url, selector)-> Context:
        headlines = BeautifulSoup(urlopen(url), 'html.parser').select(selector) 
        for headline in headlines:  ## html의 속성 부분을 추출
            if 'href' in headline.attrs:  #속성 중 링크만 추출
                yield headline.attrs['href']
    
    def _get_from_web_without_http(self, url, attr_key, prefix=None)-> Context:
        headlines = BeautifulSoup(urlopen(url), 'html.parser').find_all(attrs={'class':f'{attr_key}'})  # name은 태그 추출
        for headline in headlines:  ## html의 속성 부분을 추출
            for link in headline.find_all('a'):
                if 'href' in link.attrs:  #속성 중 링크만 추출
                    if prefix is not None: 
                        yield prefix + link.attrs['href']
                    else: 
                        yield link.attrs['href']
        
    def _get_from_web_link(self, url, class_key)-> Context:
        links = BeautifulSoup(urlopen(url), 'html.parser').find_all('a')
        for link  in links:
            if 'class' in link.attrs:  #속성 중 class만 추출
                if class_key in link.attrs['class']:
                    yield link.attrs['href']