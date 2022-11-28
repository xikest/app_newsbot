
from bs4 import BeautifulSoup
from selenium import webdriver


class Wsj:
    """

   # if mailing.box == 'wsj':   #대문자로 
    #     summary = Wsj(url).summary()
    #     enable_translate=False # contents에서 보내기 전에 볼러옴 
    # else:
    #     summary = None
    #     enable_translate=False

    # print(enable_translate)
    # print(summary)


    """
    def __init__(self, url:str):
        user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument("--remote-debugging-port=9230")
        chrome_options.add_argument('user-agent={0}'.format(user_agent))
        chrome_options.add_argument('lang=ko_kr')

        self._wd = webdriver.Chrome('chromedriver', options=chrome_options)
        self._wd.get(url)# 웹페이지 가져 오기
        pass



    def summary(self):
        html = self._wd.page_source
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.title.text
        sub_title = soup.find('h2').text
        self._quit()
        return f"{title}\n\n{sub_title}"



    def _quit(self):
        self._wd.quit()
