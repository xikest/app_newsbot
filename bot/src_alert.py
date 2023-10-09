import asyncio
from typing import Generator

from bot.src import SrcMail, SrcRss, SrcNews
from info.feeder import Feeder
from info.definition_obj import Context


class Src_Alert:
    def __init__(self):
        self.category:dict = {
            'news':'news',
            'mail': 'mail',
            'rss': 'rss'
        }
        pass
    def feed_generators(self) -> Generator:
        feeder = Feeder()
        for category in self.category.keys():
            if category == 'news':
                yield from [SrcNews(feeder.get_feeds(source), feeder.get_chatId(source)).generator() for source in feeder.get_keylist(category)]
            elif category == 'mail':
                yield from [SrcMail(feeder.get_feed_ids(), mailings=feeder.get_feeds(source), chatId=feeder.get_chatId(source)).generator() for source in feeder.get_keylist(category)]
            elif category == 'rss':
                yield from [SrcRss(feeder.get_feeds(source), feeder.get_chatId(source)).generator() for source in feeder.get_keylist(category)]

    async def generator(self) -> Context:
        async def run_generator(generator):
            async for context in generator():
                yield context

        tasks = [run_generator(feed_generator) for feed_generator in self.feed_generators()]
        for task in asyncio.as_completed(tasks):
            async for context in task:
                yield context


    # async def generator(self) -> Context:
    #     async def run_generator(generator):
    #         async for context in generator():
    #             yield context
    #
    #     tasks = [run_generator(generator) for generator in self.generators()]
    #     for task in asyncio.as_completed(tasks):
    #         async for context in task:
    #             yield context


#
# class SrcAlert:
#     def __init__(self, ChatId:str=None):
#         self._ChatId:Optional[str]=ChatId
#         self._chatId_wsj = BotProfiles.get_botAlert().channels.get('teat_w_chat_id')
#         self._chatId_wisdom = BotProfiles.get_botAlert().channels.get('teat_wisdom_chat_id')
#         self._chatId_news = BotProfiles.get_botAlert().channels.get('teat_news_id')
#         self._chatId_concensus = BotProfiles.get_botAlert().channels.get('consensus_chat_id')
#         self._chatId_energy = BotProfiles.get_botAlert().channels.get('energy_chat_id')
#         self._chatId_cn = BotProfiles.get_botAlert().channels.get('teat_cn_chat_id')
#         self._chatId_agri = BotProfiles.get_botAlert().channels.get('teat_agri_chat_id')
#         self._chatId_stats = BotProfiles.get_botAlert().channels.get('teat_stats_chat_id')
#         self._chatId_insight = BotProfiles.get_botAlert().channels.get('teat_insight_chat_id')
#         self._chatId_bok = BotProfiles.get_botAlert().channels.get('teat_bok_chat_id')
#
#
#     def set_chatId_wsj(self, ChatId):
#         self._chatId_wsj = ChatId
#
#     def set_chatId_news(self, ChatId):
#         self._chatId_news = ChatId
#
#     def set_chatId_wisdom(self, ChatId):
#         self._chatId_wisdom = ChatId
#
#     def set_chatId_concensus(self, ChatId):
#         self._chatId_concensus = ChatId
#
#     def set_chatId_energy(self, ChatId):
#         self._chatId_energy = ChatId
#
#     def set_chatId_cn(self, ChatId):
#         self._chatId_cn = ChatId
#
#     def set_chatId_agri(self, ChatId):
#         self._chatId_agri = ChatId
#
#     def set_chatId_stats(self, ChatId):
#         self._chatId_stats = ChatId
#
#     def set_chatId_insight(self, ChatId):
#         self._chatId_insight = ChatId
#
#     def set_chatId_bok(self, ChatId):
#         self._chatId_bok = ChatId
#
#     async def generator(self) -> Context:
#         async def run_generator(generator):
#             async for context in generator():
#                 yield context
#
#             generators = [
#                 SrcMailBox(usr=InfoNav.get_usr(),
#                            pid=InfoNav.get_pid(),
#                            mailings=FeedWeb.get_WSJ,
#                            ChatId=self._chatId_wsj).generator,  #web: WSJ 뉴스
#                 SrcMailBox(usr=InfoNav.get_usr(),
#                            pid=InfoNav.get_pid(),
#                            mailings=FeedWeb.get_WISDOM,
#                            ChatId=self._chatId_wisdom).generator,  #web: WISDOM 뉴스
#                 SrcNews(FeedWeb.get_news, self._chatId_news).generator,  #web: 뉴스 한경, 연합인포맥스
#                 SrcNews(FeedWeb.get_insight, self._chatId_insight).generator, #web: 인사이트: 브릿지워터
#                 SrcNews(FeedWeb.get_USDA_report, self._chatId_agri).generator, #web: 식량: USDA
#                 SrcRss(FeedRss.get_rss_concensus, self._chatId_concensus).generator, #RSS 컨센서스
#                 SrcRss(FeedRss.get_rss_insight, self._chatId_insight).generator, #RSS 인사이트
#                 SrcRss(FeedRss.get_rss_energy, self._chatId_energy).generator, #RSS 에너지
#                 SrcRss(FeedRss.get_rss_bok, self._chatId_bok).generator, #RSS 한국은행
#             ]
#
#             tasks = [run_generator(generator) for generator in generators]
#             for task in asyncio.as_completed(tasks):
#                 async for context in task:
#                     yield context
#
#
#
#


            #
            #         # web: WSJ 뉴스
            # generatorFromWSJ = SrcMailBox(usr=InfoNav.get_usr(),
            #                               pid=InfoNav.get_pid(),
            #                               mailings=FeedWeb.get_WSJ,
            #                               ChatId=self._chatId_wsj).generator
            #
            # # web: WISDOM 뉴스
            # generatorFromWISDOM = SrcMailBox(usr=InfoNav.get_usr(),
            #                                  pid=InfoNav.get_pid(),
            #                                  mailings=FeedWeb.get_WISDOM,
            #                                  ChatId=self._chatId_wisdom).generator
            #
            # # web: 뉴스 한경, 연합인포맥스
            # generatorFromWebNews = SrcNews(FeedWeb.get_news, self._chatId_news).generator
            #
            # # web: 뉴스 중국
            # # generatorFromWebNews_cn = SrcNews(FeedWeb.get_news_cn, self._chatId_cn).generator
            #
            # # web: 에너지
            # # generatorFromWebEnergy = SrcNews(FeedWeb.get_energy, self._chatId_energy).generator
            #
            # # web: 인사이트: 브릿지워터
            # generatorFromWebInsight = SrcNews(FeedWeb.get_insight, self._chatId_insight).generator
            #
            # # web: 식량: USDA
            # generatorFromWebUSDA = SrcNews(FeedWeb.get_USDA_report, self._chatId_agri).generator
            #
            # # RSS 컨센서스
            # generatorFromRssConcensus = SrcRss(FeedRss.get_rss_concensus, self._chatId_concensus).generator
            #
            # # RSS 인사이트
            # generatorFromRssinsight = SrcRss(FeedRss.get_rss_insight, self._chatId_insight).generator
            #
            # # RSS 에너지
            # generatorFromRssEnergy = SrcRss(FeedRss.get_rss_energy, self._chatId_energy).generator
            #
            # # RSS 한국은행
            # generatorFromRssBok = SrcRss(FeedRss.get_rss_bok, self._chatId_bok).generator

#             #   await asyncio.sleep(1)
# # generatorFromTwitterNews,generatorFromTwitterEnergy, generatorFromTwitterCn, generatorFromTwitterMacro
#             for generator in [
#                               # generatorFromTwitterConcensus,  generatorFromTwitterAgriculture, generatorFromTwitterStats,
#                               generatorFromWISDOM, generatorFromWSJ, generatorFromWebNews, generatorFromWebUSDA, generatorFromWebInsight,
#                               # generatorFromWebEnergy,
#                               generatorFromRssConcensus, generatorFromRssinsight, generatorFromRssEnergy, generatorFromRssBok
#                               ]:
#                 async for context in generator():
#                     # print(f"gen: {context}")
#                     yield context
