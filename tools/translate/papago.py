import time
import sys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import asyncio
# sys.path.insert(0, '/usr/lib/chromium-browser/chromedriver')
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'


class Papago:
    """
    result = Papago('en').translate('what is this ?')
    print(result)

    """
    def __init__(self, lang:str='en'):
        self._lang=lang
        self._tryCnt =0
        
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument("--remote-debugging-port=9230")
        chrome_options.add_argument('user-agent={0}'.format(user_agent))
        chrome_options.add_argument('lang=ko_kr')
        
        self._wd = webdriver.Chrome('chromedriver', options=chrome_options)
        self._wd.get('https://papago.naver.com/')# 웹페이지 가져 오기
        pass
      
    
        
    def translate(self, text="hello"):
            self._text = text
            try:

                # 입력 언어 선택
                dropMenu = WebDriverWait(self._wd, 20).until(EC.element_to_be_clickable((By.XPATH , '//*[@id="ddSourceLanguageButton"]')))
                dropMenu.click() #언어 선택 메뉴
                
                selector_lang = WebDriverWait(self._wd, 20).until(EC.element_to_be_clickable((By.XPATH , self._get_dict_lang())))
                selector_lang.click() #언어 선택
        
                # 입력
                input_text = WebDriverWait(self._wd, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="sourceEditArea"]')))
                
                for txt in chunks(text,50):
                    input_text.send_keys('d'+txt) # 텍스트 입력,  텍스트의 가장 앞에는 더미 문자 추가해줘야 함
                # 출력 언어 선택
                # 구현 안함, 입력 언어와 동일한 방식으로 선택

                #번역하기 버튼 클릭
                trans_btn = WebDriverWait(self._wd, 20).until(EC.element_to_be_clickable((By.XPATH , '//*[@id="btnTranslate"]')))
                trans_btn.click()
                time.sleep(1)
                # await asyncio.sleep(1)  # 번역 결과 대기
                
                #번역된 결과 보기
                result = WebDriverWait(self._wd, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="targetEditArea"]')))
                return result.text
            except Exception as e:
                self._wd.quit()
                if self._tryCnt < 3:
                    self._tryCnt += 1
                    self.translate(self._text)
                print(f"papago_error: {e}")
                
                
    def quit(self):
        self._wd.quit()
            

    def _get_dict_lang(self, lang:str='auto') ->str: # 언어 선택
        dict_lang={'auto':'//*[@id="ddSourceLanguage"]/div[2]/ul/li[1]/a',
                   'kr':'//*[@id="ddSourceLanguage"]/div[2]/ul/li[2]/a',
                   'en':'//*[@id="ddSourceLanguage"]/div[2]/ul/li[3]/a',
                   'jp':'//*[@id="ddSourceLanguage"]/div[2]/ul/li[4]/a',
                   'cn':'//*[@id="ddSourceLanguage"]/div[2]/ul/li[3]/a'}
        return dict_lang.get(lang)
    
def chunks(l, n):
    # Yield successive n-sized chunks from l
    for i in range(0, len(l), n):
        yield l[i:i + n]


