from typing import Optional, Generator
import feedparser
from bot.handler.contents_hanlder import Context
from bs4 import BeautifulSoup
import datetime

class SrcRss:

    def __init__(self, rssList:Generator, chat_id:Optional[str]):
        self._chat_id:Optional[str]=chat_id
        self._rssList:Generator = rssList

    async def generator(self)-> Context:
                try: 
                    for rss in self._rssList:
                        for feed in feedparser.parse(rss.url).entries[::-1]:
                            if rss.src == 'googleAlert': 
                                yield Context(label = f"{rss.name}", content=[feed.link.replace('https://www.google.com/url?rct=j&sa=t&url=','').split('&ct=ga&cd')[0]], botChatId=self._chat_id, dtype='msg')
                            elif rss.src == 'rss':
                                yield Context(label = f"{rss.name}", content=[feed.link], botChatId=self._chat_id, dtype='msg')
                    print(f'rss_src_fin:{ datetime.datetime.now()}\n')
                except Exception as e:
                    print(f'rss_src_err:{ datetime.datetime.now()}')  
                    print(f"rss error: {e}\n")
                    pass


