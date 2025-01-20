from typing import AsyncGenerator
import feedparser
import datetime
from bs4 import BeautifulSoup
from urllib.parse import urlsplit
import logging
from bot.definition_obj import Context

class RSS:

    def __init__(self, chat_id:str, src:str, name:str, url:str, verbose:bool=False, *args, **kwargs):
        self.chat_id = chat_id
        self.src = src
        self.verbose = verbose
        self.name = name
        self.url = url
        self.enable_translate = kwargs.get("enable_translate", False)
        self.extract_url:str = kwargs.get("extract_url", None)
        self.url_skips:list = kwargs.get("url_skips", [])
        self.enable_script_from_video_yt = kwargs.get("enable_script_from_video_yt", False)
        self.verbose = verbose
        
    async def generator(self) -> AsyncGenerator:
        try:
            logging.info(f"Start getting the feed from the {self.name}'s: {datetime.datetime.now()}")
            for feed in feedparser.parse(self.url).entries[:5]:
                if self.src == 'googleAlert':
                    article_link = feed.link.replace('https://www.google.com/url?rct=j&sa=t&url=', '').split('&ct=ga&cd')[0]
                    title = clean_title(feed.title)
                elif self.src == 'rss':
                    article_link = feed.link
                    title = feed.get("title", '') 
                    title = title.strip().lower()
                if self.extract_url == "extract":
                    article_link = urlsplit(article_link)._replace(query="").geturl()
                logging.info(f"{title} : {article_link}")  
                if not any(url_skip in article_link for url_skip in self.url_skips):                    
                    yield Context(label=f"{self.name}", title=title, link=article_link, bot_chat_id=self.chat_id, dtype='msg', 
                                  enable_translate=self.enable_translate, 
                                  enable_script_from_video_yt=self.enable_script_from_video_yt)
            logging.info(f"Finished obtaining the feed from the {self.name}'s : {datetime.datetime.now()}")
        except Exception as e:
            if self.verbose:
                logging.error(f'Error description -> {e}')


def clean_title(title):
    soup = BeautifulSoup(title, 'html.parser')
    clean_title = soup.get_text()

    # HTML 엔티티 변환
    clean_title = clean_title.replace('&quot;', '"').replace('&#39;', "'")
    return clean_title