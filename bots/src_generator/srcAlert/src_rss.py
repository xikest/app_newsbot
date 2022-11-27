from typing import Optional, Generator
import feedparser
from tools.telegram_bot.contents import Context
from bs4 import BeautifulSoup


class SrcRss:

    def __init__(self, rssList:Generator, ChatId:Optional[str]):
        self._ChatId:Optional[str]=ChatId
        self._rssList:Generator = rssList

    def generator(self)-> Context:
                try: 
                    for rss in self._rssList:
                        for feed in feedparser.parse(rss.url).entries:
                            if rss.src == 'googleAlert': 
                                yield Context( content=[feed.link.replace('https://www.google.com/url?rct=j&sa=t&url=','').split('&ct=ga&cd')[0]], label = f"{rss.name}", descr=None, botChatId=self._ChatId, dtype='msg') 
                            elif rss.src == 'rss': 
                                summary=BeautifulSoup(f'{feed.title}\n\n{feed.description}', 'html.parser').text
                                yield Context(content=[feed.link], label = f"{rss.name}", summary = [summary], enable_translate=rss.enable_translate, botChatId=self._ChatId, dtype='msg')    
                            # elif rss.src == 'rss_s': 
                            #     summary=BeautifulSoup(f'{feed.title}\n\n{feed.summary}', 'html.parser').text
                            #     yield Context(content=[feed.link], label = f"{rss.name}", summary = [summary],  enable_translate=rss.enable_translate, botChatId=self._ChatId, dtype='msg')                  
                                
                                                               
                except Exception as e:
                    print(f"rss error: {e}")
                    pass


