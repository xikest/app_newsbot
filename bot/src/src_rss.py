from typing import Optional, Generator
import feedparser
from bot.handler.contents_hanlder import Context
from bs4 import BeautifulSoup
import datetime

class SrcRss:

    def __init__(self, rssList:Generator, ChatId:Optional[str]):
        self._ChatId:Optional[str]=ChatId
        self._rssList:Generator = rssList

    async def generator(self)-> Context:
                try: 
                    for rss in self._rssList():
                        for feed in feedparser.parse(rss.url).entries[::-1]:
                            if rss.src == 'googleAlert': 
                                yield Context(label = f"{rss.name}", content=[feed.link.replace('https://www.google.com/url?rct=j&sa=t&url=','').split('&ct=ga&cd')[0]], botChatId=self._ChatId, dtype='msg') 
                            elif rss.src == 'rss': 
                                summary=BeautifulSoup(f'{feed.title}\n\n{feed.description}', 'html.parser').text
                                yield Context(label = f"{rss.name}", content=[feed.link], summary = [summary], botChatId=self._ChatId, dtype='msg', enable_translate=rss.enable_translate)    
                            # elif rss.src == 'rss_s': 
                            #     summary=BeautifulSoup(f'{feed.title}\n\n{feed.summary}', 'html.parser').text
                            #     yield Context(content=[feed.link], label = f"{rss.name}", summary = [summary],  enable_translate=rss.enable_translate, botChatId=self._ChatId, dtype='msg')                  
                    print(f'rss_src_fin:{ datetime.datetime.now()}\n')  
                                                               
                except Exception as e:
                    print(f'rss_src_err:{ datetime.datetime.now()}')  
                    print(f"rss error: {e}\n")
                    pass


