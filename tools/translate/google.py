import time
import sys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import asyncio
# sys.path.insert(0, '/usr/lib/chromium-browser/chromedriver')
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'


class GoogleTranslate:
    """
    result = Papago('en').translate('what is this ?')
    print(result)

    """
    def __init__(self, lang:str='en'):
        self._lang=lang
        
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('user-agent={0}'.format(user_agent))
        chrome_options.add_argument('lang=ko_kr')
        
        self._wd = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver', options=chrome_options)
        self._wd.get('https://translate.google.co.kr/')# 웹페이지 가져 오기
        pass
        
   
        
    async   def eng2kor(self, text="hello"):

            selector_lang = WebDriverWait(self._wd, 20).until(EC.element_to_be_clickable((By.XPATH , self._get_dict_lang(self._lang))))
            selector_lang.click()
            # time.sleep(1)
    
            # 입력
            input_text = WebDriverWait(self._wd, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea')))
            input_text.send_keys(text) # 텍스트 입력,  텍스트의 가장 앞에는 더미 문자 추가해줘야 함
            # time.sleep(1)
            # 출력 언어 선택
            # 구현 안함, 입력 언어와 동일한 방식으로 선택

            await asyncio.sleep(1)
            #번역된 결과 보기
            result = WebDriverWait(self._wd, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[2]/div/div[8]/div/div[1]')))

            return result.text

    def _get_dict_lang(self, lang:str='auto') ->str: # 언어 선택
        dict_lang={'en':'//*[@id="i8"]'}
        return dict_lang.get(lang)
    
# result = Google('en').translate('what is this ?')
# print(result)
    