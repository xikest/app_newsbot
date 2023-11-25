from bs4 import BeautifulSoup
from urllib.request import urlopen
from .webdriver import WebDriver
import time

class Summary_scraper:
    def __init__(self):
        self.wait_time = 1
        self.web_driver = WebDriver()

    def wsj_summary(self, url:str):
        driver = self.web_driver.get_chrome()
        driver.get(url)
        time.sleep(self.wait_time)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.title.text
        sub_title = soup.find('h2').text
        summary =  f"{title}\n\n{sub_title}"
        driver.close()
        driver.quit()
        return summary
    
    
    def summary(self, url:str):
        driver = self.web_driver.get_chrome()
        driver.get(url)
        time.sleep(self.wait_time)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        # title = soup.title.text
        sub_title = soup.find('h1').text
        summary =  f"{sub_title}"
        driver.close()
        driver.quit()
        return summary

    # def summary(self, url:str):
    #     driver = self.web_driver.get_chrome()
    #     driver.get(url)
    #     time.sleep(self.wait_time)
    #     html = driver.page_source
    #     soup = BeautifulSoup(html, 'html.parser')
    #     title = soup.title.text
    #     summary =  f"{title}"
    #     driver.close()
    #     driver.quit()
    #     return summary

