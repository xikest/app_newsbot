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
                        print(f'start get feed from rss of "{rss.name}": {datetime.datetime.now()}\n') 
                        for feed in feedparser.parse(rss.url).entries[-10:]:
                            if rss.src == 'googleAlert':
                                url = feed.link.replace('https://www.google.com/url?rct=j&sa=t&url=','').split('&ct=ga&cd')[0]
                            elif rss.src == 'rss':
                                url = feed.link
                            if not rss.exceptions or all(exception not in url for exception in rss.exceptions):
                                yield Context(label = f"{rss.name}", content=[url], botChatId=self._chat_id, dtype='msg')
                        print(f'finish to get feed from rss of "{rss.name}": {datetime.datetime.now()}\n')            
                    except Exception as e:
                        time_sleep = datetime.datetime.now()
                        print(f'raised feed error from rss of "{rss.name}" @{time_sleep}')
                        print(f'error description -> {e}')
                        await asyncio.sleep(30 * 60)
                        time_awake = datetime.datetime.now()
                        print(f'awaked feed error of rss of "{rss.name} @{time_awake}\n')
                        print(f'total sleep time{time_awake - time_sleep}')


