
# from bs4 import BeautifulSoup
# from selenium import webdriver


# class Wsj:
#     """

#    # if mailing.box == 'wsj':   #대문자로 
#     #     summary = Wsj(url).summary()
#     #     enable_translate=False # contents에서 보내기 전에 볼러옴 
#     # else:
#     #     summary = None
#     #     enable_translate=False

#     # print(enable_translate)
#     # print(summary)


#     """
#     def __init__(self, url:str):
#         user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
#         chrome_options = webdriver.ChromeOptions()
#         chrome_options.add_argument('--headless')
#         chrome_options.add_argument('--no-sandbox')
#         chrome_options.add_argument('--disable-dev-shm-usage')
#         chrome_options.add_argument("--remote-debugging-port=9230")
#         chrome_options.add_argument('user-agent={0}'.format(user_agent))
#         chrome_options.add_argument('lang=ko_kr')

#         self._wd = webdriver.Chrome('chromedriver', options=chrome_options)
#         self._wd.get(url)# 웹페이지 가져 오기
#         pass



#     def summary(self):
#         html = self._wd.page_source
#         soup = BeautifulSoup(html, 'html.parser')
#         title = soup.title.text
#         sub_title = soup.find('h2').text
#         self._quit()
#         return f"{title}\n\n{sub_title}"



#     def _quit(self):
#         self._wd.quit()

        
# """
# pip install nltk
# python -m nltk.downloader all
# from nltk import sent_tokenize

# text = "Hello, David. I made some cookies. Do you want som?"
# tokenized_text = sent_tokenize(text)
# print(tokenized_text)

# # ['Hello, David.', 'I made some cookies.', 'Do you want som?']
# """

import time
import sys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import asyncio
import pickle
from bs4 import BeautifulSoup

sys.path.insert(0, '/usr/lib/chromium-browser/chromedriver')

user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'

class HkCookie:
    """
    hk에서 쿠키를 생성
    """
    def __init__(self):
        self._url = 'https://plus.hankyung.com/'
        pass
      
    def _initionalizer(self, url:str):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument("--remote-debugging-port=9230")
        chrome_options.add_argument('user-agent={0}'.format(user_agent))
        chrome_options.add_argument('lang=ko_kr')
        
        wd = webdriver.Chrome('chromedriver', options=chrome_options)
        wd.get(url)# 웹페이지 가져 오기
        return wd
        
    def get_cookie(self):
        wd = self._initionalizer(self._url)
        
        hk_login_btn = WebDriverWait(wd, 30).until(EC.element_to_be_clickable((By.XPATH , '//*[@id="header"]/div[1]/ul/li[1]/a')))
        hk_login_btn.click()
        
        member_login_btn = WebDriverWait(wd, 30).until(EC.element_to_be_clickable((By.XPATH , '//*[@id="container"]/div/div[1]/div[1]/a')))
        member_login_btn.click()

        #로그인 정보 입력
        input_id = WebDriverWait(wd, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="userid"]')))
        input_id.send_keys('taest12@naver.com') # 텍스트 입력,  텍스트의 가장 앞에는 더미 문자 추가해줘야 함
        time.sleep(1)
        
        input_pw = WebDriverWait(wd, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="userpw"]')))
        input_pw.send_keys('xowlsdl13!') # 텍스트 입력,  텍스트의 가장 앞에는 더미 문자 추가해줘야 함
        time.sleep(1)
        
        login_btn = WebDriverWait(wd, 30).until(EC.element_to_be_clickable((By.XPATH , '//*[@id="loginForm"]/div/div[2]/a')))
        login_btn.click()
        wd.implicitly_wait(10)
        
        cookies = wd.get_cookies()
        with open('hk_cookies.pkl','wb') as f:
             pickle.dump(cookies, f)
        wd.close()
        wd.quit()

class Wsj: 
    def __init__(self):
        self._url = 'https://plus.hankyung.com'
        pass
      
    def _initionalizer(self, url:str):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument("--remote-debugging-port=9230")
        chrome_options.add_argument('user-agent={0}'.format(user_agent))
        chrome_options.add_argument('lang=ko_kr')
        
        wd = webdriver.Chrome('chromedriver', options=chrome_options)
        wd.get(url)# 웹페이지 가져 오기
        wd = self._get_cookies(wd)
        self._to_wsj(wd)
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
        # time.sleep(30)
        wd.implicitly_wait(30)
        wd.switch_to.window(wd.window_handles[1])
        return None
        
        
    def summary(self, wsj_url='https://www.wsj.com/articles/hilton-sees-a-new-golden-age-of-travel-can-it-last-11671245615?mod=hp_lead_pos6'):
        wd = self._initionalizer(self._url)
        wd.get(wsj_url)

        html = wd.page_source
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.title.text
        sub_title = soup.find('h2').text
        paragraphes = soup.find_all('p', attrs={"data-type":"paragraph"})
        # for paragraph in paragraphes:
        #     print(paragraph.attrs)
        # print(paragraphes)
        # print('\n')
        paragraphes = " ".join([paragraph.text for paragraph in paragraphes])
        
        # ad_text ="Download for Free Today Enter your mobile number and we will send you a link to download the WSJ app. You are now subscribed. Manage your subscriptions at any time via https://wsj.com/newsletters. Please try again later. Manage your subscriptions at any time via https://wsj.com/newsletters. This copy is for your personal, non-commercial use only. Distribution and use of this material are governed by our Subscriber Agreement and by copyright law. For non-personal use or to order multiple copies, please contact Dow Jones Reprints at 1-800-843-0008 or visit www.djreprints.com."
        # paragraphes= paragraphes.replace(ad_text, "")

        # self._quit()
        summary =  f"{title}\n\n{sub_title}\n\n{paragraphes}"
        # print(summary)
        wd.close()
        wd.quit()
        return summary
    
    # def quit(self):
    #     self._wd.quit()
    
# HkCookie().get_cookie()
# Wsj().summary()









                    
    # def translate_tx(self, text="hello"):
    #         try:

    #             # 입력 언어 선택
    #             dropMenu = WebDriverWait(self._wd, 30).until(EC.element_to_be_clickable((By.XPATH , '//*[@id="ddSourceLanguageButton"]')))
    #             dropMenu.click() #언어 선택 메뉴
                
    #             selector_lang = WebDriverWait(self._wd, 30).until(EC.element_to_be_clickable((By.XPATH , self._get_dict_lang())))
    #             selector_lang.click() #언어 선택
        
    #             # 입력
    #             input_text = WebDriverWait(self._wd, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="sourceEditArea"]')))
                
    #             for txt in chunks(text,50):
    #                 input_text.send_keys('d'+txt) # 텍스트 입력,  텍스트의 가장 앞에는 더미 문자 추가해줘야 함
    #             # 출력 언어 선택
    #             # 구현 안함, 입력 언어와 동일한 방식으로 선택

    #             #번역하기 버튼 클릭
    #             trans_btn = WebDriverWait(self._wd, 30).until(EC.element_to_be_clickable((By.XPATH , '//*[@id="btnTranslate"]')))
    #             trans_btn.click()
    #             time.sleep(1)
              
                
    #             #번역된 결과 보기
    #             result = WebDriverWait(self._wd, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="targetEditArea"]'))).text
                
    #             # 세션 닫기
    #             self._wd.quit()
                
    #             return result
    #         except Exception as e:
    #             self._wd.quit()
    #             raise Exception(f"papago_error: {e}")
    #             # if self._tryCnt < 3:
    #             #     self._tryCnt += 1
    #             #     self.translate_tx(self._text)
    #             # print(f"papago_error: {e}")
    #             # return None
    