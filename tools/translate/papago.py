import time
import sys
import asyncio
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from nltk import sent_tokenize

sys.path.insert(0, '/usr/lib/chromium-browser/chromedriver')

# pip install nltk
# python -m nltk.downloader all

USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'

class Papago:
    """
    from tools.translate.papago import Papago
    papago = Papago('en')
    result = papago.translate('hello, today is a good day')
    papago.quit()
    print(result)
    """

    def __init__(self, lang:str='en'):
        self._url = 'https://papago.naver.com/'
        self._lang=lang

    def _get_dict_lang(self, lang:str='auto') ->str: # 언어 선택
        dict_lang={'auto':'//*[@id="ddSourceLanguage"]/div[2]/ul/li[1]/a',
                   'kr':'//*[@id="ddSourceLanguage"]/div[2]/ul/li[2]/a',
                   'en':'//*[@id="ddSourceLanguage"]/div[2]/ul/li[3]/a',
                   'jp':'//*[@id="ddSourceLanguage"]/div[2]/ul/li[4]/a',
                   'cn':'//*[@id="ddSourceLanguage"]/div[2]/ul/li[3]/a'}
        return dict_lang.get(lang)  

    async def translate(self, text="hello"):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('user-agent={0}'.format(USER_AGENT))
        options.add_argument('lang=ko_kr')
        wd = webdriver.Chrome('chromedriver', options=options)

        try:
            # 입력 언어 선택
            dropMenu = WebDriverWait(wd, 30).until(EC.element_to_be_clickable((By.XPATH , '//*[@id="ddSourceLanguageButton"]')))
            dropMenu.click() #언어 선택 메뉴
            await asyncio.sleep(1)  # 결과 대기

            selector_lang = WebDriverWait(wd, 30).until(EC.element_to_be_clickable((By.XPATH , self._get_dict_lang())))
            selector_lang.click() #언어 선택
            await asyncio.sleep(1)  # 결과 대기

            # 입력
            input_text = WebDriverWait(wd, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="sourceEditArea"]')))
            for txt in chunks(text,50): input_text.send_keys('d'+txt) # 텍스트 입력,  텍스트의 가장 앞에는 더미 문자 추가해줘야 함

            # 출력 언어 선택
            # 구현 안함, 입력 언어와 동일한 방식으로 선택

            #번역하기 버튼 클릭
            trans_btn = WebDriverWait(wd, 30).until(EC.element_to_be_clickable((By.XPATH , '//*[@id="btnTranslate"]')))
            trans_btn.click()

            await asyncio.sleep(2)
