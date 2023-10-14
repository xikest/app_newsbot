                   
from bs4 import BeautifulSoup
from urllib.request import urlopen
from typing import Optional, Generator
from selenium import webdriver
from bot.handler.contents_hanlder import Context
import datetime
import sys

sys.path.insert(0, '/usr/lib/chromium-browser/chromedriver')
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'

class SrcNews:
    def __init__(self, newsStand: Generator, chat_id:str=None):
        self._chat_id:Optional[str]=chat_id
        self._newsStand:Generator =  newsStand
    async def generator(self)-> Context:
            try:
                for news in self._newsStand:
                    if news.src == 'web': 
                        webGenerator = self._get_from_web(news.url, news.attr_key)
                        for content in webGenerator:
                            yield Context(label=f'{news.name}', content=[content],  botChatId=self._chat_id, dtype='msg')
                    elif news.src == 'webWithSelector': 
                        pass
                        # content = self._get_from_web_with_selector(news.url, news.attr_key)
                    elif news.src == 'webWithoutHttp': 
                        webGenerator = self._get_from_web_without_http(news.url, news.attr_key, news.prefix)
                        for content in webGenerator:
                            yield Context(label=f'{news.name}', content=[content],  botChatId=self._chat_id, dtype='msg')
                        
                    elif news.src == 'webLink': 
                        webGenerator = self._get_from_web_link(news.url, news.class_key)
                        for content in webGenerator:
                            yield Context(label=f'{news.name}', content=[content],  botChatId=self._chat_id, dtype='msg')
                            
                    elif news.src == 'webWithStarts': 
                        webGenerator = self._get_from_web_with_starts(news.url, news.attr_key, news.prefix, news.startswith)
                        for content in webGenerator:
                            yield Context(label=f'{news.name}', content=[content],  botChatId=self._chat_id, dtype='msg')

                    elif news.src == 'webWithStarts_labelTime': 
                        webGenerator = self._get_from_web_with_starts(news.url, news.attr_key, news.prefix, news.startswith)
                        label = self._get_labelTime_from_web(news.url)
                        for content in webGenerator:
                            yield Context(label=f'{news.name} {label}', content=[content],  botChatId=self._chat_id, dtype='msg')

                    elif news.src == 'webFromDolBlog':
                        webGenerator = self._get_from_web_dolblog(news.url)
                        for title, p, link in webGenerator:                        
                            yield Context(label=f'{news.name}', content=[link],  botChatId=self._chat_id, dtype='msg')
                            
                    elif news.src == 'webFromIEA_analysis':
                        webGenerator = self._get_from_web_IEA_analysis(news.url, news.attr_key)
                        for title, link in webGenerator:                        
                            yield Context(label=f'{news.name}', content=[link], botChatId=self._chat_id, dtype='msg')
                print(f'news_src_fin:{ datetime.datetime.now()}\n')
            except Exception as e:
                print(f'news_src_err:{ datetime.datetime.now()}')  
                print(f"news stand error {e}\n")
                pass

#===================================================
# IEA
#===================================================         
    def _get_from_web_IEA_analysis(self, url:str='https://www.iea.org/flagship', attr_key:str='m-flagship-listing'):
        headlines = BeautifulSoup(urlopen(url), 'html.parser').find_all(attrs={'class':f'{attr_key}'})  # name은 태그 추출  
        for headline in headlines[::-1]:## html의 속성 부분을 추출
            url= 'https://www.iea.org'+headline.find('a').attrs['href']
            title=headline.h3.text.strip()
            yield title,  url
            
#===================================================
# dol
#===================================================    
    
    def _get_from_web_dolblog(self, url:str):
        html = BeautifulSoup(urlopen(url), 'html.parser')
        contents = html.find_all(attrs={'class':'highlight-teaser'})
        for content in contents[::-1]:
            title = content.h3.text
            p = content.p.text
            url = "https://blog.dol.gov"+content.find('a').attrs['href']
            yield title, p, url


#===================================================
# web
#===================================================
    def _get_labelTime_from_web(self, url)-> str:
        html = BeautifulSoup(urlopen(url), 'html.parser')
        return f'{html.h1.text}_{html.time.text}'



    def _get_from_web_with_starts(self, url, attr_key, prefix=None, startswith='http')-> str:
        headlines = BeautifulSoup(urlopen(url), 'html.parser').find_all(attrs={'class':f'{attr_key}'})  # name은 태그 추출
        for headline in headlines[::-1]:## html의 속성 부분을 추출
            for link in headline.find_all('a'):
                if 'href' in link.attrs and link.attrs['href'].startswith(startswith):
                        if prefix is not None:
                            # print(link.attrs['href'])
                            url = prefix + link.attrs['href']
                        else:
                            url = link.attrs['href']
                        yield url

    def _get_from_web(self, url, attr_key, prefix=None)-> str:
        headlines = BeautifulSoup(urlopen(url), 'html.parser').find_all(attrs={'class':f'{attr_key}'})  # name은 태그 추출
        for headline in headlines[::-1]:## html의 속성 부분을 추출
            for link in headline.find_all('a'):
                if 'href' in link.attrs and (link.attrs['href'].startswith('http') or link.attrs['href'].startswith('www')):
                    if prefix is not None:
                        url = prefix + link.attrs['href']
                    else:
                        url = link.attrs['href']
                    yield url

    def _get_from_web_with_selector(self, url, selector)-> str:
        headlines = BeautifulSoup(urlopen(url), 'html.parser').select(selector) 
        for headline in headlines[::-1]:## html의 속성 부분을 추출
            if 'href' in headline.attrs:  #속성 중 링크만 추출
                url = headline.attrs['href']
                yield url

    def _get_from_web_without_http(self, url, attr_key, prefix=None)-> str:
        headlines = BeautifulSoup(urlopen(url), 'html.parser').find_all(attrs={'class':f'{attr_key}'})  # name은 태그 추출
        for headline in headlines[::-1]: ## html의 속성 부분을 추출
            for link in headline.find_all('a'):
                if 'href' in link.attrs:  #속성 중 링크만 추출
                    if prefix is not None:
                        url = prefix + link.attrs['href']
                    else:
                        url = link.attrs['href']
                    yield url

    def _get_from_web_link(self, url, class_key)-> str:
        links = BeautifulSoup(urlopen(url), 'html.parser').find_all('a')
        for link  in links[::-1]:
            if 'class' in link.attrs:  #속성 중 class만 추출
                if class_key in link.attrs['class']:
                    url = link.attrs['href']
                    yield url
