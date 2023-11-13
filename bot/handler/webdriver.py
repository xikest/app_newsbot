from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


class WebDriver:
    def __init__(self, executable_path:str=None, browser_path:str=None, headless=True):
        if executable_path is None:
            self.executable_path = "/workspace/research-market-tv/chromedriver/chromedriver"
        else:
            self.executable_path = executable_path
        if browser_path is None:
            self.browser_path = "/workspace/research-market-tv/chrome/chrome"
        else:
            self.browser_path = browser_path
        self.headless= headless

        pass
    def get_chrome(self):

        chrome_options = Options()
        chrome_options.binary_location=self.browser_path
        chrome_options.add_argument(
            "--user-agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36'")# 에이전트 우회
        # chrome_options.page_load_strategy = 'none'
        if self.headless:
            chrome_options.add_argument('--headless=chrome')  # 헤드리스 모드로 실행
            chrome_options.add_argument('--disable-gpu')  # 헤드리스 모드로 실행
        # --headless = chrome
        chrome_options.add_argument('--no-sandbox')  # 헤드리스 크롬 브라우저를 "사용자 네임스페이스" 옵션 없이 실행하도록 설정
        chrome_options.add_argument('--disable-dev-shm-usage')

        # chrome_options.add_argument('lang=ko_kr')  # 브라우저 언어
        service = Service(executable_path = self.executable_path)  # 크롬 드라이버 경로 설정
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        return self.driver




