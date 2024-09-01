from typing import Optional, Generator
import feedparser
import datetime
import asyncio
from bs4 import BeautifulSoup

from bot.handler.contents_hanlder import Context


class SrcRss:

    def __init__(self, rssList: Generator, chat_id: Optional[str], verbose=True):
        self._chat_id: Optional[str] = chat_id
        self._rssList: Generator = rssList
        self.verbose = verbose

    async def generator(self) -> Context:
        url = None
        for rss in self._rssList:
            try:
                print(f"Start getting the feed from the {rss.name}'s: {datetime.datetime.now()}")
                print(feedparser.parse(rss.url))
                for feed in feedparser.parse(rss.url).entries[:5]:
                    
                    if rss.src == 'googleAlert':
                        
                        if rss.url_original:
                            url = feed.link
                        else:
                            url = feed.link.replace('https://www.google.com/url?rct=j&sa=t&url=', '').split('&ct=ga&cd')[0]
                        title = clean_title(feed.title)
                        # title = self.get_title(url)
                    elif rss.src == 'rss':
                        url = feed.link
                        title = feed.get("title", '')
                    if not rss.exceptions or all(exception not in url for exception in rss.exceptions):
                        yield Context(label=f"{rss.name}", summary=title,contents=[url], botChatId=self._chat_id, dtype='msg', enable_translate=rss.enable_translate)
                print(f"Finished obtaining the feed from the {rss.name}'s : {datetime.datetime.now()}")

            except Exception as e:
                time_sleep = datetime.datetime.now()
                if self.verbose:
                    print(f'Error description -> {e}')
                    print(f"Raised a feed error from the {rss.name}'s @{time_sleep}")
                await asyncio.sleep(60 * 10)  # 다음 반복까지 대기 시간
                time_awake = datetime.datetime.now()
                if self.verbose:
                    print(f"Awakened a feed error from the {rss.name}'s @{time_awake}")
                    print(f'Total sleep time{time_awake - time_sleep}')

def clean_title(title):
    # BeautifulSoup을 사용하여 HTML 태그 제거
    soup = BeautifulSoup(title, 'html.parser')
    clean_title = soup.get_text()

    # HTML 엔티티 변환
    clean_title = clean_title.replace('&quot;', '"').replace('&#39;', "'")
    
    return clean_title