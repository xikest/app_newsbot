from typing import Optional, Generator
import feedparser
import datetime

from bot.handler.contents_hanlder import Context

class SrcRss:

    def __init__(self, rssList:Generator, chat_id:Optional[str]):
        self._chat_id:Optional[str]=chat_id
        self._rssList:Generator = rssList

    async def generator(self)-> Context:
                try:
                    url = None
                    for rss in self._rssList:
                        for feed in feedparser.parse(rss.url).entries[-10:]:
                            if rss.src == 'googleAlert':
                                url = feed.link.replace('https://www.google.com/url?rct=j&sa=t&url=','').split('&ct=ga&cd')[0]
                            elif rss.src == 'rss':
                                url = feed.link
                            if not rss.exceptions or all(exception in url for exception in rss.exceptions):
                                yield Context(label = f"{rss.name}", content=[url], botChatId=self._chat_id, dtype='msg')
                    print(f'rss_src_fin:{ datetime.datetime.now()}\n')
                except Exception as e:
                    print(f'rss_src_err:{ datetime.datetime.now()}')  
                    print(f"rss error {e}\n")
                    pass
