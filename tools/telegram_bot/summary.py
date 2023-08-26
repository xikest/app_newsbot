

import time
import sys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import asyncio
import pickle
from bs4 import BeautifulSoup
from urllib.request import urlopen

sys.path.insert(0, '/usr/lib/chromium-browser/chromedriver')

user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'

class Wsj: 
    def __init__(self):
        self._url = 'https://plus.hankyung.com'
        pass
      
    def _initionalizer(self, url:str):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        # chrome_options.add_argument("--remote-debugging-port=9230")
        chrome_options.add_argument('user-agent={0}'.format(user_agent))
        chrome_options.add_argument('lang=ko_kr')
        
        wd = webdriver.Chrome('chromedriver', options=chrome_options)
        # wd.get(url)# 웹페이지 가져 오기
        # wd = self._get_cookies(wd)
        # self._to_wsj(wd)
        return wd
        
    def _get_cookies(self, wd):
        """
        사전에 생성한 쿠기를 불러온다
        """
        with open('hk_cookies.pkl','rb') as f:
            cookies= pickle.load(f)
        for cookie in cookies: wd.add_cookie(cookie)
        return wd
        
    def _to_wsj(self, wd):
        """
        WSJ  페이지로 이동
        """
        wsj_btn = WebDriverWait(wd, 30).until(EC.element_to_be_clickable((By.XPATH , '//*[@id="header"]/div[2]/ul/li[2]/a')))
        wsj_btn.click()
        wd.implicitly_wait(30)
        wd.switch_to.window(wd.window_handles[1])
        return None
        
        
    def summary(self, url='https://www.wsj.com/articles/hilton-sees-a-new-golden-age-of-travel-can-it-last-11671245615?mod=hp_lead_pos6'):
        wd = self._initionalizer(self._url)
        wd.get(url)

        html = wd.page_source
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.title.text
        sub_title = soup.find('h2').text
        # paragraphes = soup.find_all('p', attrs={"data-type":"paragraph"})
        # paragraphes = " ".join([paragraph.text for paragraph in paragraphes])
        # summary =  f"{title}\n\n{sub_title}\n\n{paragraphes}"
        summary =  f"{title}\n\n{sub_title}"
        # print(summary)
        wd.close()
        wd.quit()
        return summary
    



class Iea: 
    def __init__(self):
        pass
      
    # def _initionalizer(self):
    #     chrome_options = webdriver.ChromeOptions()
    #     chrome_options.add_argument('--headless')
    #     chrome_options.add_argument('--no-sandbox')
    #     chrome_options.add_argument('--disable-dev-shm-usage')
    #     # chrome_options.add_argument("--remote-debugging-port=9230")
    #     chrome_options.add_argument('user-agent={0}'.format(user_agent))
    #     chrome_options.add_argument('lang=ko_kr')
        
    #     wd = webdriver.Chrome('chromedriver', options=chrome_options)

    #     return wd
        


    def summary(self, url='https://www.iea.org/news/global-government-spending-on-clean-energy-transitions-rises-to-usd-1-2-trillion-since-the-start-of-the-pandemic-spurred-by-energy-security-concerns'):
        # wd = self._initionalizer()
        # wd.get(iea_url)
        
        soup = BeautifulSoup(urlopen(url), 'html.parser')
        title = soup.title.text
        sub_title = soup.find('h4').text
        # main_texts=soup.find(attrs={'class': 'm-block m-block--text'})
            
        # paragraphes = main_texts.find_all('p')
        # paragraphes = " ".join([paragraph.text for paragraph in paragraphes])
        # summary =  f"""{title}\n\n{sub_title}\n\n{paragraphes}"""
        summary =  f"{title}\n\n{sub_title}"
        # wd.close()
        # wd.quit()
        return summary


class Wisdom: 
    def __init__(self):
        pass
        


    def summary(self, url='https://whalewisdom.com/filing/robbins-charles-4-2023-08-23-173606-0400-blk'):
        # wd = self._initionalizer()
        # wd.get(iea_url)
        
        soup = BeautifulSoup(urlopen(url), 'html.parser')
        title = soup.title.text
        sub_title = soup.find('h1').text
        # main_texts=soup.find(attrs={'class': 'm-block m-block--text'})
            
        # paragraphes = main_texts.find_all('p')
        # paragraphes = " ".join([paragraph.text for paragraph in paragraphes])
        # summary =  f"""{title}\n\n{sub_title}\n\n{paragraphes}"""
        summary =  f"{title}\n\n{sub_title}"
        # wd.close()
        # wd.quit()
        return summary