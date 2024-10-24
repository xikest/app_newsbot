from typing import Generator
from info.definition_obj import Mail, News
import os


class Feeder:
    def __init__(self):
        self.feeder_mail_info = {
            'usr': os.environ.get("MAILID"),
            'pid': os.environ.get("PPWW")
        }
        self.feeder_web_source = {


            'news_article_chatid': '-1001673032661',
            'news_article':
                [
                    News(name='한경_글로벌마켓', src='web', url='https://www.hankyung.com/reporter/48', class_key='news-list'),
                    # 글로벌 마켓 김현석
                    News(name='한경_글로벌마켓', src='web', url='https://www.hankyung.com/reporter/843', class_key='news_list'),
                    # 글로벌 마켓 송영찬
                    News(name='한경_글로벌마켓', src='web', url='https://www.hankyung.com/reporter/90', class_key='news_list'),
                    # 한경 박신영
                    News(name='한경_글로벌마켓', src='web', url='https://www.hankyung.com/reporter/417', class_key='news-list'),
                    # 글로벌 마켓 이지훈
                    News(name='한경_글로벌마켓', src='web', url='https://www.hankyung.com/reporter/111', class_key='news-list'),
                    # 글로벌 마켓 김일규
                    News(name='한경_글로벌마켓', src='web', url='https://www.hankyung.com/reporter/847', class_key='news-list'),
                    # 한경 김리안
                    News(name='한경_글로벌마켓', src='web', url='https://www.hankyung.com/globalmarket/news-market',
                         class_key='news-list'),
                    News(name='한경', src='web', url='https://www.hankyung.com/economy', class_key='main-headline'),
                    News(name='한경', src='web', url='https://www.hankyung.com/financial-market',
                         class_key='main-headline'),
                    News(name='한경', src='web', url='https://www.hankyung.com/realestate', class_key='main-headline'),
                    # MK 윤원섭
                    News(name='MK', src='web', url='https://www.mk.co.kr/author/322',
                         class_key='news_list latest_news_list type_desc'),

                ],

            'news_realestate_chatid': '-1001558520951',
            'news_realestate':
                [
                    News(name='한경_집코노미', src='web', url='https://www.hankyung.com/reporter/531', class_key='news-list'),
                    # 집코노미 전형진
                ],

            
            'mail_wsj_chatid': '-1001754209136',
            'mail_wsj':
                [
                    Mail(box='WSJ_NEWS', sender='The Wall Street Journal.',
                         url_conditions=['wsj.com'], filter_linktext="Read More")
                ],
                
                
                

            'rss_economist_chatid': '-1001686311222',
            'rss_economist':
                [
                    News(name='the_world_this_week', src='rss',
                         url='https://www.economist.com/the-world-this-week/rss.xml', enable_translate=True),
                    News(name='special_report', src='rss',
                         url='https://www.economist.com/special-report/rss.xml', enable_translate=True),
                    News(name='briefing', src='rss',
                         url='https://www.economist.com/briefing/rss.xml', enable_translate=True),
                    News(name='indicators', src='rss',
                         url='https://www.economist.com/economic-and-financial-indicators/rss.xml', enable_translate=True)
                ],
                
            'rss_cnbc_chatid': '-1001854256703',
            'rss_cnbc':
                [   News(name='cnbc_top_news', src='rss',
                       url='https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=100003114', enable_translate=True),
                   
                    # News(name='cnbc_world_news', src='rss',
                    #    url='https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=100727362', enable_translate=True),
                    
                    News(name='cnbc_Finance', src='rss',
                       url='https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=10000664', enable_translate=True),

                    News(name='cnbc_Business_News', src='rss',
                       url='https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=10001147', enable_translate=True),
                   
                    News(name='cnbc_Technology', src='rss',
                       url='https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=19854910', enable_translate=True),

                    News(name='cnbc_Energy', src='rss',
                       url='https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=19836768', enable_translate=True),

                    ],
                
            
            'rss_wsj_chatid': '-1001754209136',
            'rss_wsj':
                [

                    # News(name='US_World_News', src='rss',
                    #      url='https://feeds.a.dj.com/rss/RSSWorldNews.xml', enable_translate=True),
                    News(name='US_business', src='rss',
                         url='https://feeds.a.dj.com/rss/WSJcomUSBusiness.xml', enable_translate=True),
                    News(name='US_Markets', src='rss',
                         url='https://feeds.a.dj.com/rss/RSSMarketsMain.xml', enable_translate=True),
                    News(name='US_technology', src='rss',
                         url='https://feeds.a.dj.com/rss/RSSWSJD.xml', enable_translate=True),
                    News(name='cn_wsj', src='rss',
                         url='https://cn.wsj.com/zh-hans/rss', enable_translate=True),

                ],

            'rss_blogs_chatid': '-1001528926673',
            'rss_blogs':
                [
                    News(name='snpGlobal_Infographic', src='googleAlert', enable_translate=True,
                         url='https://www.google.co.kr/alerts/feeds/11305193269230284098/7612806762062248149'),
                    
                    News(name='snpGlobal_Interactive', src='googleAlert', enable_translate=True,
                         url='https://www.google.co.kr/alerts/feeds/11305193269230284098/10152480852472819673'),

                    News(name='iea_report', src='googleAlert', enable_translate=True,
                         url='https://www.google.co.kr/alerts/feeds/11305193269230284098/7382274396628814653'),
                    News(name='icap_carbon', src='googleAlert', enable_translate=True,
                         url='https://www.google.co.kr/alerts/feeds/11305193269230284098/9987650578008654233'),
                    
                    News(name='imf_chart', src='googleAlert', enable_translate=True,
                         url='https://www.google.co.kr/alerts/feeds/11305193269230284098/10686972103545313262'),    
     
                    News(name='economist_graphic"', src='rss', enable_translate=True,
                         url='https://www.economist.com/graphic-detail/rss.xml'),

                    News(name='EIA_today_energy', src='rss', enable_translate=True,
                    url='https://www.eia.gov/rss/todayinenergy.xml'),

                ],
                

            'rss_news_chatid': '-1001673032661',
            'rss_news':
                [
                    News(name='한경', src='googleAlert',
                         url='https://www.google.co.kr/alerts/feeds/11305193269230284098/9180843931580834263'),
                    News(name='한경_차이나스톡', src='googleAlert',
                         url='https://www.google.co.kr/alerts/feeds/11305193269230284098/4858968756427596008'),
                    News(name='한경_원자재이슈탐구', src='googleAlert',
                         url='https://www.google.co.kr/alerts/feeds/11305193269230284098/9036013775263201261'),
                    News(name='한경_워싱턴나우', src='googleAlert',
                         url='https://www.google.co.kr/alerts/feeds/11305193269230284098/4858968756427597753'),
                    News(name='한경_오늘의유가', src='googleAlert',
                         url='https://www.google.co.kr/alerts/feeds/11305193269230284098/8817692926258482559'),   
                    News(name='한경_에네르기파WAR', src='googleAlert',
                         url='https://www.google.co.kr/alerts/feeds/11305193269230284098/10051269404088993743'),
                    News(name='한경_글로벌마켓AS', src='googleAlert',
                         url='https://www.google.co.kr/alerts/feeds/11305193269230284098/2323969111153995290'),   
                    News(name='중동 천일야화', src='googleAlert',
                         url='https://www.google.co.kr/alerts/feeds/11305193269230284098/11030838220576993937'),    
                ],

            'rss_youtube_chatid': "-1001585250010",
            'rss_youtube':
                [  
                    News(name='Statista',  src='rss',
                         url='https://www.youtube.com/feeds/videos.xml?playlist_id=PLpV7l7rprSPsHbJOtil987oI7cGDGPW4v'),                    
                    News(name='지식Play',  src='rss',
                         url='https://www.youtube.com/feeds/videos.xml?channel_id=UCXql5C57vS4ogUt6CPEWWHA'),    
                    News(name='교양이를_부탁해',  src='rss',
                         url='https://www.youtube.com/feeds/videos.xml?playlist_id=PLq8zNPMaG8KeOje-DrA2i6PixCderPWUg'),   
                    News(name="안재광의 대기만성's", src='rss',
                         url='https://www.youtube.com/feeds/videos.xml?playlist_id=PLVups02-DZEWjZECMTA-bx14SEKzpsJi-'),   
                    News(name="power to XI_steps", src='rss',
                         url='https://www.youtube.com/feeds/videos.xml?playlist_id=PL93pjPb4DDbRKELcV4CxDueaIZZvr6D0c'),   
                    News(name="ETF 언박싱", src='rss', 
                         url='https://www.youtube.com/feeds/videos.xml?playlist_id=PLVups02-DZEX8sGPDze7pWis4mRmfRgmI'),
                    News(name="투자 Insight", src='rss',
                         url='https://www.youtube.com/feeds/videos.xml?playlist_id=PL_8dl5rgert5NCSg9on7CQsZKozfGO0Kc'),    
                    News(name="집코노미 흥청망청", src='rss',
                         url='https://www.youtube.com/feeds/videos.xml?playlist_id=PLZtm8tjZjNV5aTdl51WcHLGxpw0lFq2xP'), 
                    News(name="집코노미 오마카세", src='rss',
                         url= 'https://www.youtube.com/feeds/videos.xml?playlist_id=PLZtm8tjZjNV4rtLaPSarnw6mRUJ7wayHd'), 
                    News(name="집코노미 총총견문록", src='rss',
                         url= 'https://www.youtube.com/feeds/videos.xml?playlist_id=PLZtm8tjZjNV54z04pd1Pj8UPark_Tk0jX'), 
                    News(name="미국주식 전쟁", src='rss',
                         url='https://www.youtube.com/feeds/videos.xml?playlist_id=PL93pjPb4DDbQW8eSZDKNhYjzNYqKKG99W'),  
                    News(name="ETF의 모든 것", src='rss',
                         url='https://www.youtube.com/feeds/videos.xml?playlist_id=PLVups02-DZEWa7AdDgoxihlLkaAU59tOm'),      
                    News(name="딥코노미", src='rss',
                         url='https://www.youtube.com/feeds/videos.xml?playlist_id=PLVups02-DZEVEadSGnXvzZnh4ckyis-YK'),
                ],




            'rss_bok_chatid': '-1001918946467',
            'rss_bok':
                [
                    News(name='BOK 의결사항', src='rss',
                         url='https://www.bok.or.kr/portal/bbs/P0000093/news.rss?menuNo=200789'),
                    News(name='경제전망보고서', src='rss',
                         url='https://www.bok.or.kr/portal/bbs/P0002359/news.rss?menuNo=200066'),
                    News(name='금융안정보고서', src='rss',
                         url='https://www.bok.or.kr/portal/bbs/P0000593/news.rss?menuNo=200769'),
                    News(name='통화신용정책보고서', src='rss',
                         url='https://www.bok.or.kr/portal/bbs/P0002353/news.rss?menuNo=200433'),

                    News(name='BOK 이슈노트', src='rss',
                         url='https://www.bok.or.kr/portal/bbs/B0000156/news.rss?menuNo=200754'),
                    News(name='BOK 경제연구(국문)', src='rss',
                         url='	https://www.bok.or.kr/imer/bbs/P0002455/news.rss?menuNo=500788'),
                    News(name='경제분석', src='rss',
                         url='https://www.bok.or.kr/portal/bbs/P0000556/news.rss?menuNo=200440'),
                    News(name='이슈및관련자료 ', src='rss',
                         url='https://www.bok.or.kr/portal/bbs/P0002897/news.rss?menuNo=200788'),

                    News(name='해외경제포커스', src='rss',
                         url='https://www.bok.or.kr/portal/bbs/P0000545/news.rss?menuNo=200437'),
                    News(name='국제경제리뷰', src='rss',
                         url='https://www.bok.or.kr/portal/bbs/P0000528/news.rss?menuNo=200434'),
                    News(name='경제상황 평가', src='rss',
                         url='https://www.bok.or.kr/portal/bbs/P0002105/news.rss?menuNo=200439'),

                    News(name='뉴욕사무소 ', src='rss',
                         url='https://www.bok.or.kr/portal/bbs/P0002017/news.rss?menuNo=200365'),
                    News(name='워싱턴주재원', src='rss',
                         url='https://www.bok.or.kr/portal/bbs/P0002223/news.rss?menuNo=200082'),
                    News(name='프랑크푸르트사무소', src='rss',
                         url='https://www.bok.or.kr/portal/bbs/P0002226/news.rss?menuNo=200083'),
                    News(name='동경사무소', src='rss',
                         url='https://www.bok.or.kr/portal/bbs/P0002229/news.rss?menuNo=200084'),
                    News(name='런던사무소', src='rss',
                         url='https://www.bok.or.kr/portal/bbs/P0002231/news.rss?menuNo=200085'),
                    News(name='북경사무소', src='rss',
                         url='https://www.bok.or.kr/portal/bbs/P0002232/news.rss?menuNo=200086'),
                    News(name='홍콩주재원', src='rss',
                         url='https://www.bok.or.kr/portal/bbs/P0002233/news.rss?menuNo=200087'),
                    News(name='상해주재원 ', src='rss',
                         url='https://www.bok.or.kr/portal/bbs/P0002234/news.rss?menuNo=200088'),

                ],



        }



    def get_keylist(self, source_category: str = 'news') -> set:
        key_set = set(key.replace("_chatid", "") for key in self.feeder_web_source.keys() if source_category in key)
        print(f"feed keys of {source_category}: {key_set}")
        return key_set

    def get_feeds(self, source: str) -> Generator:
        yield from self.feeder_web_source.get(source)

    def get_chatId(self, source: str) -> str:
        return self.feeder_web_source.get(f"{source}_chatid")

    def get_feed_ids(self, key):
        return self.feeder_mail_info.get(key)




