from typing import Optional, Generator
import feedparser
import datetime
import asyncio

from bot.handler.contents_hanlder import Context

class SrcRss:

    def __init__(self, rssList:Generator, chat_id:Optional[str]):
        self._chat_id:Optional[str]=chat_id
        self._rssList:Generator = rssList

    async def generator(self)-> Context:
                url = None
                for rss in self._rssList:
                    try:
                        print(f"Start getting the feed from the {rss.name}'s: {datetime.datetime.now()}") 
                        for feed in feedparser.parse(rss.url).entries[-10:]:
                            if rss.src == 'googleAlert':
                                url = feed.link.replace('https://www.google.com/url?rct=j&sa=t&url=','').split('&ct=ga&cd')[0]
                            elif rss.src == 'rss':
                                url = feed.link
                            if not rss.exceptions or all(exception not in url for exception in rss.exceptions):
                                yield Context(label = f"{rss.name}", content=[url], botChatId=self._chat_id, dtype='msg')
                                
                        print(f"Finished obtaining the feed from the {rss.name}'s : {datetime.datetime.now()}")     
                    except Exception as e:
                        time_sleep = datetime.datetime.now()
                        print(f'Error description -> {e}')
                        print(f"Raised a feed error from the {rss.name}'s @{time_sleep}")
                        await asyncio.sleep(60 * 10)  #다음 반복까지 대기 시간
                        time_awake = datetime.datetime.now()
                        print(f"Awakened a feed error from the {rss.name}'s @{time_awake}")
                        print(f'Total sleep time{time_awake - time_sleep}')

