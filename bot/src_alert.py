from typing import Generator

from bot.src import SrcMail, SrcRss, SrcNews
from info.feeder import Feeder
from info.definition_obj import Context


class Src_Alert:
    def __init__(self):
        self.category:dict = {
            'news': 'news',
            'mail': 'mail',
             'rss': 'rss'
        }
        pass

    def feed_generators(self) -> Generator:
        feeder = Feeder()
        combined_generators = []
        for category in self.category.keys():
            if category == 'news':
                generators = [SrcNews(newsStand=feeder.get_feeds(source), chat_id=feeder.get_chatId(source)).generator
                              for source in feeder.get_keylist(category)]
            elif category == 'mail':
                generators = [SrcMail(pid=feeder.get_feed_ids('pid'), usr=feeder.get_feed_ids('usr'),
                                      mailings=feeder.get_feeds(source), chat_id=feeder.get_chatId(source)).generator
                              for source in feeder.get_keylist(category)]
            elif category == 'rss':
                generators = [SrcRss(rssList=feeder.get_feeds(source), chat_id=feeder.get_chatId(source)).generator
                              for source in feeder.get_keylist(category)]
            combined_generators.extend(generators)
        return combined_generators
    async def generator(self) -> Context:
        for feed_generator in self.feed_generators():
            async for context in feed_generator():
                yield context