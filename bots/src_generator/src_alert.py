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
        self._chatId_tweetsConcensus = BotProfiles.get_botAlert().channels.get('twt_consensus_chat_id')
        self._chatId_energy = BotProfiles.get_botAlert().channels.get('energy_chat_id')
        self._chatId_cn = BotProfiles.get_botAlert().channels.get('teat_cn_chat_id')
        self._chatId_agri = BotProfiles.get_botAlert().channels.get('teat_agri_chat_id')
        self._chatId_stats = BotProfiles.get_botAlert().channels.get('teat_stats_chat_id')
        
    def set_chatId_wsj(self, ChatId):
        self._chatId_wsj = ChatId
 
    def set_chatId_news(self, ChatId):
        self._chatId_news = ChatId
        
    def set_chatId_tweetsMacro(self, ChatId):
        self._chatId_tweetsMacro = ChatId  
        
    def set_chatId_tweetsConcensus(self, ChatId):
        self._chatId_tweetsConcensus = ChatId  
        
    def set_chatId_energy(self, ChatId):
        self._chatId_energy = ChatId  
        
    def set_chatId_cn(self, ChatId):
        self._chatId_cn = ChatId  
        
    def set_chatId_agri(self, ChatId):
        self._chatId_agri = ChatId  
        
    def set_chatId_stats(self, ChatId):
        self._chatId_stats = ChatId  
        
    async def generator(self)-> Context:

            #web: WSJ 뉴스
            generatorFromWSJ = SrcMailBox(usr=InfoNav.get_usr(), 
                                            pid=InfoNav.get_pid(), 
                                            mailings=FeedWeb.get_WSJ,
                                            ChatId=self._chatId_wsj).generator

            #web: 뉴스 한경, 연합인포맥스
            generatorFromWebNews = SrcNews(FeedWeb.get_news, self._chatId_news).generator
            
            #web: 뉴스 중국
            generatorFromWebNews = SrcNews(FeedWeb.get_news_cn, self._chatId_cn).generator
            
            
            #web: 에너지
            generatorFromWebEnergy= SrcNews(FeedWeb.get_energy, self._chatId_energy).generator
            
            
            #RSS 뉴스  
            generatorFromRssNews = SrcRss(FeedRss.get_rss_news, self._chatId_news).generator
            
            #RSS 에너지
            generatorFromRssEnergy = SrcRss(FeedRss.get_rss_energy, self._chatId_energy).generator
            
            #RSS 중국
            # generatorFromRssCn = SrcRss(FeedRss.get_rss_cn, self._chatId_cn).generator
            
            #트위터: 뉴스
            generatorFromTwitterMacro = SrcTweets(BEARERTOKEN = InfoTwitter.get_twitter_BEARERTOKEN(), 
                                                    screenNames = FeedTweets.get_screenNames_news,
                                                    ChatId = self._chatId_news).generator
            
            #트위터: 매크로
            generatorFromTwitterMacro = SrcTweets(BEARERTOKEN = InfoTwitter.get_twitter_BEARERTOKEN(), 
                                                    screenNames = FeedTweets.get_screenNames_macro,
                                                    ChatId = self._chatId_tweetsMacro).generator
            #트위터: 컨센서스
            generatorFromTwitterConcensus = SrcTweets(BEARERTOKEN = InfoTwitter.get_twitter_BEARERTOKEN(), 
                                                        screenNames = FeedTweets.get_screenNames_concensus,
                                                        ChatId = self._chatId_tweetsConcensus).generator
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
            
            #   await asyncio.sleep(1)
            for generator in [generatorFromTwitterMacro, generatorFromTwitterEnergy, generatorFromTwitterConcensus, generatorFromTwitterCn,
                              generatorFromWSJ, generatorFromWebNews, generatorFromWebEnergy, generatorFromTwitterAgriculture, generatorFromTwitterStats,
                              generatorFromRssNews, generatorFromRssEnergy]:
                async for context in generator():
                    # print(f"gen: {context}")
                    yield context 












  # # ============================================
  # # 네이버 메일 WSJ
  # # ============================================


  # # ============================================
  # # 한국 경제 신문
  # # ============================================
  # class HanKyungEconomy:
  #   _ChatId:str=None
    
  #   @classmethod
  #   def getChatId(cls):
  #     if cls._ChatId is None:cls.setChatId(SrcNews.getChatId())
  #     return cls._ChatId
    
  #   @classmethod
  #   def setChatId(cls, ChatId:str):
  #     cls._ChatId = ChatId
    
  #   @staticmethod
  #   def hk_global_hot_stocks(): ## 한경 글로벌 마켓 핫 스탁
  #       url = 'https://www.hankyung.com/globalmarket/news/hot-stock'
  #       attr_key='list_top_thumb'
  #       return SrcGenerator.HTML.get_from_web(url, attr_key, botChatId=SrcNews.HanKyungEconomy.getChatId())
    
  #   @staticmethod
  #   def hk_wallstreet_now():  ## 한경 월스리트 나우
  #       url = 'https://www.hankyung.com/globalmarket/news/wallstreet-now'
  #       attr_key='list_thumb_rowtype'
  #       return SrcGenerator.HTML.get_from_web(url, attr_key, botChatId=SrcNews.HanKyungEconomy.getChatId())

  #   @staticmethod
  #   def hk_economy_top(): ## 한경 경제 탑기사
  #       url = 'https://www.hankyung.com/economy'
  #       attr_key='main-headline'
  #       return SrcGenerator.HTML.get_from_web(url, attr_key, botChatId=SrcNews.HanKyungEconomy.getChatId())
    
  #   @staticmethod
  #   def hk_finanace_top(): #한경 금융 탑기사
  #       url = 'https://www.hankyung.com/financial-market'
  #       attr_key='main-headline'
  #       return SrcGenerator.HTML.get_from_web(url, attr_key, botChatId=SrcNews.HanKyungEconomy.getChatId())

  #   @staticmethod
  #   def hk_global_video_top():  #한경 글로벌 마켓 탑 비디오
  #       url = 'https://www.hankyung.com/globalmarket/global-tv'
  #       selector= '#container > div > div.vod-top > div.txt-cont > h3 > a'
  #       return SrcGenerator.HTML.get_from_web_with_selector(url, selector, botChatId=SrcNews.HanKyungEconomy.getChatId())

  #   @staticmethod
  #   def hk_jipconomy_top():  #한경 집코노미 탑기사
  #       url = 'https://www.hankyung.com/realestate'
  #       attr_key='main-headline'
  #       return SrcGenerator.HTML.get_from_web(url, attr_key, botChatId=SrcNews.HanKyungEconomy.getChatId())

  #   @staticmethod
  #   def hk_jipconomy_video():  #한경 집코노미 탑기사
  #       url = 'https://www.hankyung.com/realestate'
  #       attr_key='main-jipconomy'
  #       return SrcGenerator.HTML.get_from_web(url, attr_key, botChatId=SrcNews.HanKyungEconomy.getChatId())

  # # ============================================
  # # 브릿지 워터 인사이트
  # # https://www.bridgewater.com/research-and-insights
  # # ============================================
  # class BridgeWater:
  #   _ChatId:str=None
    
  #   @classmethod
  #   def getChatId(cls):
  #     if cls._ChatId is None:cls.setChatId(SrcNews.getChatId())
  #     return cls._ChatId
  #   @classmethod
  #   def setChatId(cls, ChatId:str):
  #     cls._ChatId = ChatId
    
  #   @staticmethod
  #   def bridgewater_insight():  #브릿지 워터 인사이트
  #     url = 'https://www.bridgewater.com/research-and-insights'
  #     attr_key = 'MasonryList'
  #     return SrcGenerator.HTML.get_from_web(url, attr_key, botChatId=SrcNews.BridgeWater.getChatId())

  # # ============================================
  # # 연합 인포 맥스 신문
  # # ============================================
  # class EinFoMax:
  #   _ChatId:str=None
    
  #   @classmethod
  #   def getChatId(cls):
  #     if cls._ChatId is None:cls.setChatId(SrcNews.getChatId())
  #     return cls._ChatId
    
  #   @classmethod
  #   def setChatId(cls, ChatId:str):
  #     cls._ChatId = ChatId
    
  #   @staticmethod
  #   def efmax_top():  #연포 인포 맥스 많이 본 뉴스
  #     url = 'https://news.einfomax.co.kr/'
  #     attr_key='auto-article auto-db01'
  #     return SrcGenerator.HTML.get_from_web_without_http(url, attr_key, prefix='https://news.einfomax.co.kr/', botChatId=SrcNews.EinFoMax.getChatId())

  #   @staticmethod
  #   def efmax_politics_finance(): 
  #     url = 'https://news.einfomax.co.kr/news/articleList.html?sc_section_code=S1N15&view_type=sm'
  #     attr_key='auto-article auto-db01'
  #     return SrcGenerator.HTML.get_from_web_without_http(url, attr_key, prefix='https://news.einfomax.co.kr/', botChatId=SrcNews.EinFoMax.getChatId())

  #   @staticmethod
  #   def efmax_fx_bond(): 
  #     url ='https://news.einfomax.co.kr/news/articleList.html?sc_section_code=S1N16&view_type=sm'
  #     attr_key='auto-article auto-db01'
  #     return SrcGenerator.HTML.get_from_web_without_http(url, attr_key, prefix='https://news.einfomax.co.kr/', botChatId=SrcNews.EinFoMax.getChatId())

  #   @staticmethod
  #   def efmax_f_stocks(): 
  #     url ='https://news.einfomax.co.kr/news/articleList.html?sc_section_code=S1N21&view_type=sm'
  #     attr_key='auto-article auto-db01'
  #     return SrcGenerator.HTML.get_from_web_without_http(url, attr_key, prefix='https://news.einfomax.co.kr/', botChatId=SrcNews.EinFoMax.getChatId())

  #   @staticmethod
  #   def efmax_g_economy(): 
  #     url ='https://news.einfomax.co.kr/news/articleList.html?sc_section_code=S1N4&view_type=sm'
  #     attr_key='auto-article auto-db01'
  #     return SrcGenerator.HTML.get_from_web_without_http(url, attr_key, prefix='https://news.einfomax.co.kr/', botChatId=SrcNews.EinFoMax.getChatId())
    
  #   @staticmethod
  #   def efmax_cn_economy(): 
  #     url ='https://news.einfomax.co.kr/news/articleList.html?sc_section_code=S1N18&view_type=sm'
  #     attr_key='auto-article auto-db01'
  #     return SrcGenerator.HTML.get_from_web_without_http(url, attr_key, prefix='https://news.einfomax.co.kr/', botChatId=SrcNews.EinFoMax.getChatId())

  # # ============================================
  # # 구글알리미 RSS
  # # ============================================
  # class RssGoogle:
  #   _ChatId:str=None
    
  #   @classmethod
  #   def getChatId(cls):
  #     if cls._ChatId is None:cls.setChatId(SrcNews.getChatId())
  #     return cls._ChatId
    
  #   @classmethod
  #   def setChatId(cls, ChatId:str):
  #     cls._ChatId = ChatId
    
  #   @staticmethod
  #   def cnhk_news_google_rss(): 
  #     rss_url= 'https://www.google.co.kr/alerts/feeds/11305193269230284098/15091211705036215232'
  #     return SrcGenerator.Rss.get_from_rss_feed_by_google(rss_url, botChatId=SrcNews.RssGoogle.getChatId())

  #   @staticmethod
  #   def cen_east_news_google_rss(): 
  #     rss_url = 'https://www.google.co.kr/alerts/feeds/11305193269230284098/10207016080645967575'
  #     return SrcGenerator.Rss.get_from_rss_feed_by_google(rss_url, botChatId=SrcNews.RssGoogle.getChatId())

  # # ============================================
  # # RSS feed
  # # ============================================
  # class Rss:
  #   _ChatId:str=None
    
  #   @classmethod
  #   def getChatId(cls):
  #     if cls._ChatId is None:cls.setChatId(SrcNews.getChatId())
  #     return cls._ChatId
    
  #   @classmethod
  #   def setChatId(cls, ChatId:str):
  #     cls._ChatId = ChatId
      
  #   @staticmethod
  #   def pf_damodaran_rss(): 
  #     rss_url = 'https://aswathdamodaran.blogspot.com/feeds/posts/default' #다모다란 교수 블로그
  #     return SrcGenerator.Rss.get_from_rss_feed(rss_url, botChatId=SrcNews.Rss.getChatId())

  #   @staticmethod
  #   def gdpnow_fed_of_atlanta_rss(): 
  #     rss_url = 'https://www.atlantafed.org/rss/GDPNow' #GDP NOW
  #     return SrcGenerator.Rss.get_from_rss_feed(rss_url, botChatId=SrcNews.Rss.getChatId())

  #   @staticmethod
  #   def eia_today_energy_rss(): 
  #     rss_url = 'https://www.eia.gov/rss/todayinenergy.xml' # EIA today energy
  #     return SrcGenerator.Rss.get_from_rss_feed(rss_url, botChatId=SrcNews.Rss.getChatId())

  #   @staticmethod
  #   def eia_thisweek_petroleum_rss(): 
  #     rss_url = 'https://www.eia.gov/petroleum/weekly/includes/week_in_petroleum_rss.xml' # EIA thisweek_petroleum
  #     return SrcGenerator.Rss.get_from_rss_feed(rss_url, botChatId=SrcNews.Rss.getChatId())

  # # ============================================
  # # NBER economic 일정
  # # ============================================
  # class NBER:
  #   _ChatId:str=None
    
  #   @classmethod
  #   def getChatId(cls):
  #     if cls._ChatId is None:cls.setChatId(SrcNews.getChatId())
  #     return cls._ChatId
    
  #   @classmethod
  #   def setChatId(cls, ChatId:str):
  #     cls._ChatId = ChatId
      
  #   @staticmethod
  #   def nber_economic_indicators_releases(): 
  #     rss_url = 'https://back.nber.org/rss/releases.xml' # NBER economic
  #     return SrcGenerator.Rss.get_from_rss_NBER_schedule(rss_url, botChatId=SrcNews.NBER.getChatId())

  # # ============================================
  # # IMF 블로그
  # # ============================================
  # class IMF:
  #   _ChatId:str=None
    
  #   @classmethod
  #   def getChatId(cls):
  #     if cls._ChatId is None:cls.setChatId(SrcNews.getChatId())
  #     return cls._ChatId
    
  #   @classmethod
  #   def setChatId(cls, ChatId:str):
  #     cls._ChatId = ChatId
      
  #   @staticmethod
  #   def imf_blog_chart():  #imf 블로그 차트
  #     url ='https://www.imf.org/en/News/Chart-of-the-week'
  #     attr_key ='date'
  #     return SrcGenerator.HTML.get_from_web(url, attr_key, botChatId=SrcNews.IMF.getChatId())
    
    
