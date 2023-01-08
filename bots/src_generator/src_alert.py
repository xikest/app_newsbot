from typing import Optional

from tools.telegram_bot import Context
from .srcAlert import SrcMailBox, SrcRss, SrcNews, SrcTweets

from info.bot_ids import InfoNav, InfoTwitter
from info.bot_profiles import BotProfiles
from info.feeds import FeedWeb, FeedRss, FeedTweets
    
      
class SrcAlert:
    def __init__(self, ChatId:str=None):
        self._ChatId:Optional[str]=ChatId
        self._chatId_wsj = BotProfiles.get_botAlert().channels.get('teat_w_chat_id')
        self._chatId_news = BotProfiles.get_botAlert().channels.get('teat_news_id')
        self._chatId_tweetsMacro = BotProfiles.get_botAlert().channels.get('twt_macro_id')
        self._chatId_concensus = BotProfiles.get_botAlert().channels.get('consensus_chat_id')
        self._chatId_energy = BotProfiles.get_botAlert().channels.get('energy_chat_id')
        self._chatId_cn = BotProfiles.get_botAlert().channels.get('teat_cn_chat_id')
        self._chatId_agri = BotProfiles.get_botAlert().channels.get('teat_agri_chat_id')
        self._chatId_stats = BotProfiles.get_botAlert().channels.get('teat_stats_chat_id')
        self._chatId_insight = BotProfiles.get_botAlert().channels.get('teat_insight_chat_id')
        self._chatId_bok = BotProfiles.get_botAlert().channels.get('teat_bok_chat_id')
        
        
    def set_chatId_wsj(self, ChatId):
        self._chatId_wsj = ChatId
 
    def set_chatId_news(self, ChatId):
        self._chatId_news = ChatId
        
    def set_chatId_tweetsMacro(self, ChatId):
        self._chatId_tweetsMacro = ChatId  
        
    def set_chatId_concensus(self, ChatId):
        self._chatId_concensus = ChatId  
        
    def set_chatId_energy(self, ChatId):
        self._chatId_energy = ChatId  
        
    def set_chatId_cn(self, ChatId):
        self._chatId_cn = ChatId  
        
    def set_chatId_agri(self, ChatId):
        self._chatId_agri = ChatId  
        
    def set_chatId_stats(self, ChatId):
        self._chatId_stats = ChatId  
        
    def set_chatId_insight(self, ChatId):
        self._chatId_insight = ChatId  
        
    def set_chatId_bok(self, ChatId):
        self._chatId_bok = ChatId  
        
    async def generator(self)-> Context:

            #web: WSJ 뉴스
            generatorFromWSJ = SrcMailBox(usr=InfoNav.get_usr(), 
                                            pid=InfoNav.get_pid(), 
                                            mailings=FeedWeb.get_WSJ,
                                            ChatId=self._chatId_wsj).generator

            #web: 뉴스 한경, 연합인포맥스
            generatorFromWebNews = SrcNews(FeedWeb.get_news, self._chatId_news).generator
            
            #web: 뉴스 중국
            # generatorFromWebNews_cn = SrcNews(FeedWeb.get_news_cn, self._chatId_cn).generator
            
            
            #web: 에너지
            generatorFromWebEnergy = SrcNews(FeedWeb.get_energy, self._chatId_energy).generator
            
            #web: 인사이트: 브릿지워터
            generatorFromWebInsight =  SrcNews(FeedWeb.get_insight, self._chatId_insight).generator
            
            #web: 식량: USDA
            generatorFromWebUSDA =  SrcNews(FeedWeb.get_USDA_report, self._chatId_agri).generator
            
            #RSS 컨센서스  
            generatorFromRssConcensus = SrcRss(FeedRss.get_rss_concensus, self._chatId_concensus).generator
            
            #RSS 인사이트  
            generatorFromRssinsight = SrcRss(FeedRss.get_rss_insight, self._chatId_insight).generator
            
            #RSS 에너지
            generatorFromRssEnergy = SrcRss(FeedRss.get_rss_energy, self._chatId_energy).generator
            
            #RSS 한국은행
            generatorFromRssBok = SrcRss(FeedRss.get_rss_bok, self._chatId_bok).generator


            #트위터: 뉴스
            generatorFromTwitterNews = SrcTweets(BEARERTOKEN = InfoTwitter.get_twitter_BEARERTOKEN(), 
                                                    screenNames = FeedTweets.get_screenNames_news,
                                                    ChatId = self._chatId_wsj).generator
            
            #트위터: 매크로
            generatorFromTwitterMacro = SrcTweets(BEARERTOKEN = InfoTwitter.get_twitter_BEARERTOKEN(), 
                                                    screenNames = FeedTweets.get_screenNames_macro,
                                                    ChatId = self._chatId_tweetsMacro).generator
            #트위터: 컨센서스
            generatorFromTwitterConcensus = SrcTweets(BEARERTOKEN = InfoTwitter.get_twitter_BEARERTOKEN(), 
                                                        screenNames = FeedTweets.get_screenNames_concensus,
                                                        ChatId = self._chatId_concensus).generator
            #트위터: 에너지
            generatorFromTwitterEnergy = SrcTweets(BEARERTOKEN = InfoTwitter.get_twitter_BEARERTOKEN(), 
                                                                screenNames = FeedTweets.get_screenNames_energy,
                                                                ChatId = self._chatId_energy).generator
            
            #트위터: 농업
            generatorFromTwitterAgriculture = SrcTweets(BEARERTOKEN = InfoTwitter.get_twitter_BEARERTOKEN(), 
                                                                screenNames = FeedTweets.get_screenNames_agriculture,
                                                                ChatId = self._chatId_agri).generator
            
            #트위터: 차이나
            generatorFromTwitterCn = SrcTweets(BEARERTOKEN = InfoTwitter.get_twitter_BEARERTOKEN(), 
                                                                screenNames = FeedTweets.get_screenNames_cn,
                                                                ChatId = self._chatId_cn).generator
              
            #트위터: 통계
            generatorFromTwitterStats = SrcTweets(BEARERTOKEN = InfoTwitter.get_twitter_BEARERTOKEN(), 
                                                                screenNames = FeedTweets.get_screenNames_stats,
                                                                ChatId = self._chatId_stats).generator
            
            #트위터: 인사이트
            generatorFromTwitterInsight = SrcTweets(BEARERTOKEN = InfoTwitter.get_twitter_BEARERTOKEN(), 
                                                                screenNames = FeedTweets.get_screenNames_insight,
                                                                ChatId = self._chatId_insight).generator
            
            
            #   await asyncio.sleep(1)
            for generator in [generatorFromTwitterNews, generatorFromTwitterMacro, generatorFromTwitterConcensus, generatorFromTwitterEnergy, generatorFromTwitterAgriculture, generatorFromTwitterCn, generatorFromTwitterStats,
                              generatorFromWSJ, generatorFromWebNews, generatorFromWebEnergy, generatorFromWebInsight, generatorFromWebUSDA, generatorFromTwitterInsight,
                              generatorFromRssConcensus, generatorFromRssinsight, generatorFromRssEnergy, generatorFromRssBok
                              ]:
                async for context in generator():
                    # print(f"gen: {context}")
                    yield context 

