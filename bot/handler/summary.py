from bs4 import BeautifulSoup
from urllib.request import urlopen
from .webdriver import WebDriver

class WSJ_Scraper:
    def __init__(self):
        self._url = 'https://plus.hankyung.com'
        self.wait_time = 10
        self.web_driver = WebDriver()

    def summary(self, url='https://www.wsj.com/articles/hilton-sees-a-new-golden-age-of-travel-can-it-last-11671245615?mod=hp_lead_pos6'):
        driver = self.web_driver.get_chrome()
        driver.get(url)

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.title.text
        sub_title = soup.find('h2').text
        # paragraphes = soup.find_all('p', attrs={"data-type":"paragraph"})
        # paragraphes = " ".join([paragraph.text for paragraph in paragraphes])
        # summary =  f"{title}\n\n{sub_title}\n\n{paragraphes}"
        summary =  f"{title}\n\n{sub_title}"
        driver.close()
        driver.quit()
        return summary




class Iea:
    def __init__(self):
        pass


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
