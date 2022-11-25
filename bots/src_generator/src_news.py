from xml.etree.ElementInclude import default_loader
from ..src_generator.src_generator import SrcGenerator
from typing import Optional, List
import time
import tweepy
from tools.telegram_bot.contents import Context
from info.ids import Ids
from info.twt_following import TweetsFlw
from .src_tweet import Tweets
from .translate import KakaoTranslate
from .papago import Papago


class SrcNews:
  _defaultChatID:Optional[str] =None
  
  @classmethod
  def getChatId(cls) -> Optional[str]:
    return cls._defaultChatID
  
  @classmethod
  def setChatId(cls, defaultChatID:str):
    cls._defaultChatID = defaultChatID
  
  @staticmethod
  def gen_news()-> List[Context]: 
      list_news =list()
      mail_gen = [SrcNews.Mailbox.naver_mailbox_wsj]
      hke_gen = [SrcNews.HanKyungEconomy.hk_economy_top,
              SrcNews.HanKyungEconomy.hk_finanace_top,
              SrcNews.HanKyungEconomy.hk_global_hot_stocks,
              SrcNews.HanKyungEconomy.hk_jipconomy_top,
              SrcNews.HanKyungEconomy.hk_wallstreet_now,
              SrcNews.HanKyungEconomy.hk_global_video_top,
              SrcNews.HanKyungEconomy.hk_jipconomy_video]
      # bw_gen = [SrcNews.BridgeWater.bridgewater_insight]
      efm_gen = [SrcNews.EinFoMax.efmax_cn_economy,
              SrcNews.EinFoMax.efmax_f_stocks,
              SrcNews.EinFoMax.efmax_fx_bond,
              # SrcNews.EinFoMax.efmax_f_stocks,
              SrcNews.EinFoMax.efmax_g_economy,    
              # SrcNews.EinFoMax.efmax_politics_finance,
              SrcNews.EinFoMax.efmax_top]
      rss_gen = [SrcNews.Rss.eia_thisweek_petroleum_rss,
              SrcNews.Rss.eia_today_energy_rss,
              # SrcNews.Rss.gdpnow_fed_of_atlanta_rss,
              # SrcNews.Rss.pf_damodaran_rss
              ]
      rss_google = [SrcNews.RssGoogle.cen_east_news_google_rss, 
                  SrcNews.RssGoogle.cnhk_news_google_rss
                  ]
      rss_nber = [SrcNews.NBER.nber_economic_indicators_releases]
      # rss_imf = [SrcNews.IMF.imf_blog_chart]
      
      twt_gen = [SrcNews.Tweets.gen_twt]  
      twt_consensus_gen = [SrcNews.Consensus.gen_twt]  
      
            
      list_news.extend(mail_gen)
      list_news.extend(hke_gen)
      # list_news.extend(bw_gen)
      list_news.extend(efm_gen)
      list_news.extend(twt_gen)
      list_news.extend(twt_consensus_gen)
      
      list_news.extend(rss_gen)
      list_news.extend(rss_google)
      list_news.extend(rss_nber)
      # list_news.extend(rss_imf)
      yield from list_news
      
    
    
    
  class Consensus:
    
    """
    SrcTwt.set_screen_names(['financialjuice'])
    SrcTwt.set_BEARER_TOKEN(bearer_token)
    list(SrcTwt.gen_twt())

    Returns:
        _type_: _description_

    Yields:
        _type_: _description_
    """
    _ChatId:Optional[str]=None

    @classmethod
    def getChatId(cls):
      if cls._ChatId is None:cls.setChatId(SrcNews.getChatId())
      return cls._ChatId
    
    @classmethod
    def setChatId(cls, ChatId:str):
      cls._ChatId = ChatId
      

      
    @staticmethod
    def gen_twt()-> List[Context]: 
      screen_names = ['ConsensusGurus']  # following 리스트
      for screen_name in screen_names:
          for tweet in SrcNews.Consensus.get_msg(screen_name):
              yield Context(content=tweet, label=screen_name, dtype='msg', botChatId=SrcNews.Consensus.getChatId())
              
    @staticmethod
    def get_msg(screen_name:str='financialjuice') -> str:
        BEARER_TOKEN=Ids.twt_beartoken()    # 트위터 접근 토큰
        client = tweepy.Client(BEARER_TOKEN)
        
        # translator = googletrans.Translator()
        try :
                t_id = client.get_user(username=screen_name).data.id # get_id
                paginator = iter(tweepy.Paginator(client.get_users_tweets, t_id, max_results=20))
                response = next(paginator)
                for tweets in response.data[::-1]:
                    # time.sleep(1) # 10초 슬립
                    # yield  [tweets.text]
                    if '@' not in tweets.text:
                      #yield [ f"#{screen_name}\n{Papago('en').translate(tweets.text)}\n\n{tweets.text}"]
                      yield [ f"#{screen_name}\n{KakaoTranslate.eng2kor(tweets.text)}\n\n{tweets.text}"]
                    # yield [ Papago(tweets.text).translate(), tweets.text]
                    # yield [ f"{tweets.text} \n {translator.translate(tweets.text, dest='ko').text}"]
                    print(f' get finish')
        except:
                print('Consensus error')
                # time.slepp(15 * 60)
            
            #
        
      

  class Tweets:
    
    """
    SrcTwt.set_screen_names(['financialjuice'])
    SrcTwt.set_BEARER_TOKEN(bearer_token)
    list(SrcTwt.gen_twt())

    Returns:
        _type_: _description_

    Yields:
        _type_: _description_
    """
    _ChatId:Optional[str]=None
    # _screen_names:List[str]=TweetsFlw.screen_names()
    # _BEARER_TOKEN:Optional[str]=Ids.twt_beartoken()

    @classmethod
    def getChatId(cls):
      if cls._ChatId is None:cls.setChatId(SrcNews.getChatId())
      return cls._ChatId
    
    @classmethod
    def setChatId(cls, ChatId:str):
      cls._ChatId = ChatId
      

      
    @staticmethod
    def gen_twt()-> List[Context]: 
      screen_names = TweetsFlw.screen_names()  # following 리스트
      for screen_name in screen_names:
          for tweet in SrcNews.Tweets.get_msg(screen_name):
              yield Context(content=tweet, label=screen_name, dtype='msg', botChatId=SrcNews.Tweets.getChatId())
              
    @staticmethod
    def get_msg(screen_name:str='financialjuice') -> str:
        BEARER_TOKEN=Ids.twt_beartoken()    # 트위터 접근 토큰
        client = tweepy.Client(BEARER_TOKEN)
      
        
        # translator = googletrans.Translator()
        try :
                t_id = client.get_user(username=screen_name).data.id # get_id
                paginator = iter(tweepy.Paginator(client.get_users_tweets, t_id, max_results=20))
                response = next(paginator)
                for tweets in response.data[::-1]:
                    # time.sleep(1) # 10초 슬립
                    # yield  [tweets.text]
                    if '@' not in tweets.text:
                      #yield [ f"#{screen_name}\n{Papago('en').translate(tweets.text)}\n\n{tweets.text}"]
                      yield [ f"#{screen_name}\n{KakaoTranslate.eng2kor(tweets.text)}\n\n{tweets.text}"]
                    # yield [ Papago(tweets.text).translate(), tweets.text]
                    # yield [ f"{tweets.text} \n {translator.translate(tweets.text, dest='ko').text}"]
                    print(f' get finish')
        except:
               print('tweets error')
               # time.slepp(15 * 60)
            #

        
# ============================================
# 네이버 메일 WSJ
# ============================================
  class Mailbox:
    _ChatId:str=None
    
    @classmethod
    def getChatId(cls):
      if cls._ChatId is None:cls.setChatId(SrcNews.getChatId())
      return cls._ChatId
    
    @classmethod
    def setChatId(cls, ChatId:str):
      cls._ChatId = ChatId
    
    @staticmethod
    def naver_mailbox_wsj():
      usr= Ids.nav_ids().get('usr')
      pid= Ids.nav_ids().get('pid')
      return  SrcGenerator.MailBox.wsj_news_from_mailbox(usr=usr, pid=pid, botChatId=SrcNews.Mailbox.getChatId())
    
  # ============================================
  # 한국 경제 신문
  # ============================================
  class HanKyungEconomy:
    _ChatId:str=None
    
    @classmethod
    def getChatId(cls):
      if cls._ChatId is None:cls.setChatId(SrcNews.getChatId())
      return cls._ChatId
    
    @classmethod
    def setChatId(cls, ChatId:str):
      cls._ChatId = ChatId
    
    @staticmethod
    def hk_global_hot_stocks(): ## 한경 글로벌 마켓 핫 스탁
        url = 'https://www.hankyung.com/globalmarket/news/hot-stock'
        attr_key='list_top_thumb'
        return SrcGenerator.HTML.get_from_web(url, attr_key, botChatId=SrcNews.HanKyungEconomy.getChatId())
    
    @staticmethod
    def hk_wallstreet_now():  ## 한경 월스리트 나우
        url = 'https://www.hankyung.com/globalmarket/news/wallstreet-now'
        attr_key='list_thumb_rowtype'
        return SrcGenerator.HTML.get_from_web(url, attr_key, botChatId=SrcNews.HanKyungEconomy.getChatId())

    @staticmethod
    def hk_economy_top(): ## 한경 경제 탑기사
        url = 'https://www.hankyung.com/economy'
        attr_key='main-headline'
        return SrcGenerator.HTML.get_from_web(url, attr_key, botChatId=SrcNews.HanKyungEconomy.getChatId())
    
    @staticmethod
    def hk_finanace_top(): #한경 금융 탑기사
        url = 'https://www.hankyung.com/financial-market'
        attr_key='main-headline'
        return SrcGenerator.HTML.get_from_web(url, attr_key, botChatId=SrcNews.HanKyungEconomy.getChatId())

    @staticmethod
    def hk_global_video_top():  #한경 글로벌 마켓 탑 비디오
        url = 'https://www.hankyung.com/globalmarket/global-tv'
        selector= '#container > div > div.vod-top > div.txt-cont > h3 > a'
        return SrcGenerator.HTML.get_from_web_with_selector(url, selector, botChatId=SrcNews.HanKyungEconomy.getChatId())

    @staticmethod
    def hk_jipconomy_top():  #한경 집코노미 탑기사
        url = 'https://www.hankyung.com/realestate'
        attr_key='main-headline'
        return SrcGenerator.HTML.get_from_web(url, attr_key, botChatId=SrcNews.HanKyungEconomy.getChatId())

    @staticmethod
    def hk_jipconomy_video():  #한경 집코노미 탑기사
        url = 'https://www.hankyung.com/realestate'
        attr_key='main-jipconomy'
        return SrcGenerator.HTML.get_from_web(url, attr_key, botChatId=SrcNews.HanKyungEconomy.getChatId())

  # ============================================
  # 브릿지 워터 인사이트
  # https://www.bridgewater.com/research-and-insights
  # ============================================
  class BridgeWater:
    _ChatId:str=None
    
    @classmethod
    def getChatId(cls):
      if cls._ChatId is None:cls.setChatId(SrcNews.getChatId())
      return cls._ChatId
    @classmethod
    def setChatId(cls, ChatId:str):
      cls._ChatId = ChatId
    
    @staticmethod
    def bridgewater_insight():  #브릿지 워터 인사이트
      url = 'https://www.bridgewater.com/research-and-insights'
      attr_key = 'MasonryList'
      return SrcGenerator.HTML.get_from_web(url, attr_key, botChatId=SrcNews.BridgeWater.getChatId())

  # ============================================
  # 연합 인포 맥스 신문
  # ============================================
  class EinFoMax:
    _ChatId:str=None
    
    @classmethod
    def getChatId(cls):
      if cls._ChatId is None:cls.setChatId(SrcNews.getChatId())
      return cls._ChatId
    
    @classmethod
    def setChatId(cls, ChatId:str):
      cls._ChatId = ChatId
    
    @staticmethod
    def efmax_top():  #연포 인포 맥스 많이 본 뉴스
      url = 'https://news.einfomax.co.kr/'
      attr_key='auto-article auto-db01'
      return SrcGenerator.HTML.get_from_web_without_http(url, attr_key, prefix='https://news.einfomax.co.kr/', botChatId=SrcNews.EinFoMax.getChatId())

    @staticmethod
    def efmax_politics_finance(): 
      url = 'https://news.einfomax.co.kr/news/articleList.html?sc_section_code=S1N15&view_type=sm'
      attr_key='auto-article auto-db01'
      return SrcGenerator.HTML.get_from_web_without_http(url, attr_key, prefix='https://news.einfomax.co.kr/', botChatId=SrcNews.EinFoMax.getChatId())

    @staticmethod
    def efmax_fx_bond(): 
      url ='https://news.einfomax.co.kr/news/articleList.html?sc_section_code=S1N16&view_type=sm'
      attr_key='auto-article auto-db01'
      return SrcGenerator.HTML.get_from_web_without_http(url, attr_key, prefix='https://news.einfomax.co.kr/', botChatId=SrcNews.EinFoMax.getChatId())

    @staticmethod
    def efmax_f_stocks(): 
      url ='https://news.einfomax.co.kr/news/articleList.html?sc_section_code=S1N21&view_type=sm'
      attr_key='auto-article auto-db01'
      return SrcGenerator.HTML.get_from_web_without_http(url, attr_key, prefix='https://news.einfomax.co.kr/', botChatId=SrcNews.EinFoMax.getChatId())

    @staticmethod
    def efmax_g_economy(): 
      url ='https://news.einfomax.co.kr/news/articleList.html?sc_section_code=S1N4&view_type=sm'
      attr_key='auto-article auto-db01'
      return SrcGenerator.HTML.get_from_web_without_http(url, attr_key, prefix='https://news.einfomax.co.kr/', botChatId=SrcNews.EinFoMax.getChatId())
    
    @staticmethod
    def efmax_cn_economy(): 
      url ='https://news.einfomax.co.kr/news/articleList.html?sc_section_code=S1N18&view_type=sm'
      attr_key='auto-article auto-db01'
      return SrcGenerator.HTML.get_from_web_without_http(url, attr_key, prefix='https://news.einfomax.co.kr/', botChatId=SrcNews.EinFoMax.getChatId())

  # ============================================
  # 구글알리미 RSS
  # ============================================
  class RssGoogle:
    _ChatId:str=None
    
    @classmethod
    def getChatId(cls):
      if cls._ChatId is None:cls.setChatId(SrcNews.getChatId())
      return cls._ChatId
    
    @classmethod
    def setChatId(cls, ChatId:str):
      cls._ChatId = ChatId
    
    @staticmethod
    def cnhk_news_google_rss(): 
      rss_url= 'https://www.google.co.kr/alerts/feeds/11305193269230284098/15091211705036215232'
      return SrcGenerator.Rss.get_from_rss_feed_by_google(rss_url, botChatId=SrcNews.RssGoogle.getChatId())

    @staticmethod
    def cen_east_news_google_rss(): 
      rss_url = 'https://www.google.co.kr/alerts/feeds/11305193269230284098/10207016080645967575'
      return SrcGenerator.Rss.get_from_rss_feed_by_google(rss_url, botChatId=SrcNews.RssGoogle.getChatId())

  # ============================================
  # RSS feed
  # ============================================
  class Rss:
    _ChatId:str=None
    
    @classmethod
    def getChatId(cls):
      if cls._ChatId is None:cls.setChatId(SrcNews.getChatId())
      return cls._ChatId
    
    @classmethod
    def setChatId(cls, ChatId:str):
      cls._ChatId = ChatId
      
    @staticmethod
    def pf_damodaran_rss(): 
      rss_url = 'https://aswathdamodaran.blogspot.com/feeds/posts/default' #다모다란 교수 블로그
      return SrcGenerator.Rss.get_from_rss_feed(rss_url, botChatId=SrcNews.Rss.getChatId())

    @staticmethod
    def gdpnow_fed_of_atlanta_rss(): 
      rss_url = 'https://www.atlantafed.org/rss/GDPNow' #GDP NOW
      return SrcGenerator.Rss.get_from_rss_feed(rss_url, botChatId=SrcNews.Rss.getChatId())

    @staticmethod
    def eia_today_energy_rss(): 
      rss_url = 'https://www.eia.gov/rss/todayinenergy.xml' # EIA today energy
      return SrcGenerator.Rss.get_from_rss_feed(rss_url, botChatId=SrcNews.Rss.getChatId())

    @staticmethod
    def eia_thisweek_petroleum_rss(): 
      rss_url = 'https://www.eia.gov/petroleum/weekly/includes/week_in_petroleum_rss.xml' # EIA thisweek_petroleum
      return SrcGenerator.Rss.get_from_rss_feed(rss_url, botChatId=SrcNews.Rss.getChatId())

  # ============================================
  # NBER economic 일정
  # ============================================
  class NBER:
    _ChatId:str=None
    
    @classmethod
    def getChatId(cls):
      if cls._ChatId is None:cls.setChatId(SrcNews.getChatId())
      return cls._ChatId
    
    @classmethod
    def setChatId(cls, ChatId:str):
      cls._ChatId = ChatId
      
    @staticmethod
    def nber_economic_indicators_releases(): 
      rss_url = 'https://back.nber.org/rss/releases.xml' # NBER economic
      return SrcGenerator.Rss.get_from_rss_NBER_schedule(rss_url, botChatId=SrcNews.NBER.getChatId())

  # ============================================
  # IMF 블로그
  # ============================================
  class IMF:
    _ChatId:str=None
    
    @classmethod
    def getChatId(cls):
      if cls._ChatId is None:cls.setChatId(SrcNews.getChatId())
      return cls._ChatId
    
    @classmethod
    def setChatId(cls, ChatId:str):
      cls._ChatId = ChatId
      
    @staticmethod
    def imf_blog_chart():  #imf 블로그 차트
      url ='https://www.imf.org/en/News/Chart-of-the-week'
      attr_key ='date'
      return SrcGenerator.HTML.get_from_web(url, attr_key, botChatId=SrcNews.IMF.getChatId())
    
    
