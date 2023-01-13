                   
from bs4 import BeautifulSoup
from urllib.request import urlopen
from typing import Optional, Generator
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from tools.telegram_bot.contents import Context
import datetime
import sys

sys.path.insert(0, '/usr/lib/chromium-browser/chromedriver')
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'

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
                            
                    elif news.src == 'webFromSnpglobalInsights':
                        webGenerator = self._get_from_web_snpGlobalInsights(news.url)
                        for title, p, link in webGenerator:                           
                            yield Context(label=f'{news.name}', content=[link], summary=[f'{title}\n\n{p}'], botChatId=self._ChatId, dtype='msg', enable_translate=news.enable_translate)
                  
                    elif news.src == 'webFromSnpglobalInfographics':
                        webGenerator = self._get_from_web_snpGlobalInfographics(news.url)
                        for title, link in webGenerator:                        
                            yield Context(label=f'{news.name}', content=[link], summary=[f'{title}\n\n'], botChatId=self._ChatId, dtype='msg', enable_translate=news.enable_translate)
                   
                    elif news.src == 'webFromDolBlog':
                        webGenerator = self._get_from_web_dolblog(news.url)
                        for title, p, link in webGenerator:                        
                            yield Context(label=f'{news.name}', content=[link], summary=[f'{title}\n\n{p}'], botChatId=self._ChatId, dtype='msg', enable_translate=news.enable_translate)
                            
                    elif news.src == 'webFromIEA_analysis':
                        webGenerator = self._get_from_web_IEA_analysis(news.url, news.attr_key)
                        for title, p, link in webGenerator:                        
                            yield Context(label=f'{news.name}', content=[link], summary=[f'{title}\n\n{p}'], botChatId=self._ChatId, dtype='msg', enable_translate=news.enable_translate)
                 
                            
                            
                print(f'news_src_fin:{ datetime.datetime.now()}\n')  
                
            except Exception as e:
                print(f'news_src_err:{ datetime.datetime.now()}')  
                print(f"news stand error: {e}\n")
                pass
            
            
    def _get_from_web_IEA_analysis(self, url:str='https://www.iea.org/flagship', attr_key:str='m-flagship-listing'):
        headlines = BeautifulSoup(urlopen(url), 'html.parser').find_all(attrs={'class':f'{attr_key}'})  # name은 태그 추출  
        for headline in headlines[-1:]:## html의 속성 부분을 추출
            link= 'https://www.iea.org'+headline.find('a').attrs['href']
            title=headline.h3.text.strip()
            p = headline.h4.text.strip()
            yield title, p, link

    
    
    
    def _get_from_web_dolblog(self, url:str):
        html = BeautifulSoup(urlopen(url), 'html.parser')
        contents = html.find_all(attrs={'class':'highlight-teaser'})
        for content in contents[-1:]:
            title = content.h3.text
            p = content.p.text
            link = "https://blog.dol.gov"+content.find('a').attrs['href']
            yield title, p, link



#===================================================
# snp global
#===================================================
      
    def _get_html_with_selenium(self, url:str):
        
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument("--remote-debugging-port=9230")
        chrome_options.add_argument('user-agent={0}'.format(user_agent))
        chrome_options.add_argument('lang=ko_kr')
        wd = webdriver.Chrome('chromedriver', options=chrome_options)
        try:
            
            wd.get(url)
            
            html = wd.page_source
            
            wd.close()
            wd.quit()
            return html
    
        except Exception as e:
            print(e)
            wd.close()
            wd.quit()
            
    
    def _get_from_web_snpGlobalInfographics(self, url):
        html = self._get_html_with_selenium(url)
        soup = BeautifulSoup(html, 'html.parser')
        contents = soup.find_all(attrs={'class':'modalimage card--inline js-gtm-tag'})
        for content in contents[::-1]:
            title = content['data-gtm-label']
            link = content['href']
            yield title, link
            
    
    def _get_from_web_snpGlobalInsights(self, url):
        html = self._get_html_with_selenium(url)
        soup = BeautifulSoup(html, 'html.parser')
        contents = soup.find_all(attrs={'class':'blog-excerpt__content'})    
        for content in contents[::-1]:
            title = content.h1.text
            p = content.p.text
            link = content.find('a').attrs['href']
            yield title, p, link
            
            


    def _get_labelTime_from_web(self, url)-> str:
        html = BeautifulSoup(urlopen(url), 'html.parser')
        return f'{html.h1.text}_{html.time.text}'



    def _get_from_web_with_starts(self, url, attr_key, prefix=None, startswith='http')-> str:
        headlines = BeautifulSoup(urlopen(url), 'html.parser').find_all(attrs={'class':f'{attr_key}'})  # name은 태그 추출
        for headline in headlines[-1:]:## html의 속성 부분을 추출
            for link in headline.find_all('a'):
                if 'href' in link.attrs and link.attrs['href'].startswith(startswith):
                        if prefix is not None:
                            # print(link.attrs['href'])
                            yield prefix + link.attrs['href']
                        else: 
                            yield link.attrs['href']

    def _get_from_web(self, url, attr_key, prefix=None)-> str:
        headlines = BeautifulSoup(urlopen(url), 'html.parser').find_all(attrs={'class':f'{attr_key}'})  # name은 태그 추출
        for headline in headlines[-1:]:## html의 속성 부분을 추출
            for link in headline.find_all('a'):
                if 'href' in link.attrs and (link.attrs['href'].startswith('http') or link.attrs['href'].startswith('www')):
                    if prefix is not None:
                        yield prefix + link.attrs['href']
                    else: 
                        yield link.attrs['href']
                
    def _get_from_web_with_selector(self, url, selector)-> str:
        headlines = BeautifulSoup(urlopen(url), 'html.parser').select(selector) 
        for headline in headlines[-1:]:## html의 속성 부분을 추출
            if 'href' in headline.attrs:  #속성 중 링크만 추출
                yield headline.attrs['href']
    
    def _get_from_web_without_http(self, url, attr_key, prefix=None)-> str:
        headlines = BeautifulSoup(urlopen(url), 'html.parser').find_all(attrs={'class':f'{attr_key}'})  # name은 태그 추출
        for headline in headlines[-1:]: ## html의 속성 부분을 추출
            for link in headline.find_all('a'):
                if 'href' in link.attrs:  #속성 중 링크만 추출
                    if prefix is not None: 
                        yield prefix + link.attrs['href']
                    else: 
                        yield link.attrs['href']
        
    def _get_from_web_link(self, url, class_key)-> str:
        links = BeautifulSoup(urlopen(url), 'html.parser').find_all('a')
        for link  in links[-1:]:
            if 'class' in link.attrs:  #속성 중 class만 추출
                if class_key in link.attrs['class']:
                    yield link.attrs['href']