from typing import Generator
import time
from bot.src import SrcMail, SrcRss, SrcNews
from info.feeder import Feeder
from info.definition_obj import Context

class Src_Alert:
    def __init__(self):
        self.category:dict = {
            'mail': 'mail',
            'rss': 'rss',
            'news': 'news',
             
        }
        pass

    def feed_generators(self, combine_interval:int=5) -> Generator:
        feeder = Feeder()
        combined_generators = []
        for category in self.category.keys():
            if category == 'news':
                for source in feeder.get_keylist(category):
                    combined_generators.append(SrcNews(newsStand=feeder.get_feeds(source), chat_id=feeder.get_chatId(source)).generator)
                    time.sleep(combine_interval)
            elif category == 'mail':
                for source in feeder.get_keylist(category):
                    combined_generators.append(SrcMail(pid=feeder.get_feed_ids('pid'), usr=feeder.get_feed_ids('usr'),
                                      mailings=feeder.get_feeds(source), chat_id=feeder.get_chatId(source)).generator)
                    time.sleep(combine_interval)
            elif category == 'rss':
                for source in feeder.get_keylist(category):
                    combined_generators.append(SrcRss(rssList=feeder.get_feeds(source), chat_id=feeder.get_chatId(source)).generator)
                    time.sleep(combine_interval)
                    
        return combined_generators
    
    async def generator(self) -> Context:
        for feed_generator in self.feed_generators():
            async for context in feed_generator():
                yield context