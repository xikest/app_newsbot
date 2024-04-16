from typing import Generator
from info.definition_obj import Mail, News
import os


class Feeder:
    def __init__(self):
        self.feeder_mail_info = {
            'usr': os.environ.get("mailid"),
            'pid': os.environ.get("ppww")
        }
        self.feeder_web_source = {
            'news_article_chatid': '-1001673032661',
            'news_article':
                [
                    News(name='한경_글로벌마켓', src='web', url='https://www.hankyung.com/reporter/48', attr_key='news-list'),
                    # 글로벌 마켓 김현석
                    News(name='한경_글로벌마켓', src='web', url='https://www.hankyung.com/reporter/99', attr_key='news_list'),
                    # 글로벌 마켓 조재길
                    News(name='한경_글로벌마켓', src='web', url='https://www.hankyung.com/reporter/90', attr_key='news_list'),
                    # 글로벌 마켓 정인설
                    News(name='한경_글로벌마켓', src='web', url='https://www.hankyung.com/reporter/575', attr_key='news-list'),
                    # 글로벌 마켓 나수지
                    News(name='한경_글로벌마켓', src='web', url='https://www.hankyung.com/reporter/109', attr_key='news-list'),
                    # 한경 박신영
                    News(name='한경_글로벌마켓', src='web', url='https://www.hankyung.com/reporter/417', attr_key='news-list'),
                    # 글로벌 마켓 이지훈
                    News(name='한경_글로벌마켓', src='web', url='https://www.hankyung.com/reporter/432', attr_key='news-list'),
                    # 글로벌 마켓 정영효
                    News(name='한경_글로벌마켓', src='web', url='https://www.hankyung.com/reporter/847', attr_key='news-list'),
                    # 한경 김리안
                    News(name='한경_글로벌마켓', src='web', url='https://www.hankyung.com/globalmarket/news-market',
                         attr_key='news-list'),
                    News(name='한경', src='web', url='https://www.hankyung.com/economy', attr_key='main-headline'),
                    News(name='한경', src='web', url='https://www.hankyung.com/financial-market',
                         attr_key='main-headline'),
                    News(name='한경', src='web', url='https://www.hankyung.com/realestate', attr_key='main-headline'),
                ],

            'news_realestate_chatid': '-1001645400224',
            'news_realestate':
                [
                    News(name='한경_집코노미', src='web', url='https://www.hankyung.com/reporter/531', attr_key='news-list'),
                    # 집코노미 전형진
                ],

            'rss_visualization_chatid': '-1001854256703',
            'rss_visualization':
                [
                    News(name='visualcapitalist', src='rss',
                         url='https://feeds.feedburner.com/visualcapitalist',
                         exceptions=['introducing-voronoi-waitlist-now-open']),
                ],

            'rss_articles_chatid': '-1001686311222',
            'rss_articles':
                [
                    # News(name='중동_소식', src='googleAlert',
                    #      url='https://www.google.co.kr/alerts/feeds/11305193269230284098/11337432206170594787'),
                    # News(name='한국은행', src='googleAlert',
                    #      url='https://www.google.co.kr/alerts/feeds/11305193269230284098/4192372648562102053'),
                    News(name='유튜브_지식플레이', src='rss',
                         url='https://www.youtube.com/feeds/videos.xml?channel_id=UCXql5C57vS4ogUt6CPEWWHA')
                ],
            # 'rss_sonytv_chatid': '-1002093329277',
            # 'rss_sonytv':
            #     [
            #         News(name='SONY + BRAVIA  + OLED -deal -deals -price', src='googleAlert',
            #              url='https://www.google.co.kr/alerts/feeds/11305193269230284098/10534109714214468206'),
            #         News(name='소니 global IR', src='googleAlert',
            #              url='"https://www.sony.com/en/SonyInfo/IR/rss/rss.xml"'),
            #         News(name='소니 global youtube', src='rss',
            #              url='https://www.youtube.com/feeds/videos.xml?channel_id=UCVjS9AuBloqJJjhsy3vIfug',
            #              # exceptions = ["headset", "buds","headphones","car","audio"]
            #              )

                # ],

            'rss_blogs_chatid': '-1001528926673',
            'rss_blogs':
                [
                    News(name='snpGlobal_Insights', src='rss',
                         url='https://www.spglobal.com/commodityinsights/en/rss-feed/blogs'),
                    # News(name='snpGlobal_Oil', src='googleAlert',
                    #      url='https://www.spglobal.com/commodityinsights/en/rss-feed/oil'),
                    # News(name='snpGlobal_Shipping', src='googleAlert',
                    #      url='https://www.spglobal.com/commodityinsights/en/rss-feed/shipping'),
                    # News(name='snpGlobal_Electronic_power', src='rss',
                    #      url='https://www.spglobal.com/commodityinsights/en/rss-feed/electric-power'),
                    # News(name='snpGlobal_Gas', src='googleAlert',
                    #      url='https://www.spglobal.com/commodityinsights/en/rss-feed/natural-gas'),
                    # News(name='snpGlobal_Metals', src='rss',
                    #      url='https://www.spglobal.com/commodityinsights/en/rss-feed/metals'),
                    # News(name='snpGlobal_Agriculture', src='rss',
                    #      url='https://www.spglobal.com/commodityinsights/en/rss-feed/agriculture'),
                    # News(name='snpGlobal_LNG', src='googleAlert',
                    #      url='hhttps://www.spglobal.com/commodityinsights/en/rss-feed/lng'),
                    News(name='snpGlobal_Energy-transition', src='rss',
                         url='https://www.spglobal.com/commodityinsights/en/rss-feed/energy-transition'),
                    # News(name='GDP_NOW', src='rss',
                    #      url='https://www.atlantafed.org/rss/GDPNow'),
                    # News(name='US_census', src='rss',
                    # url='https://www.census.gov/economic-indicators/indicator.xml'),
                    # News(name='fred_blog', src='rss',
                    #      url='http://fredblog.stlouisfed.org/feed/'),
                    # News(name='EIA_today_energy', src='rss',
                    # url='https://www.eia.gov/rss/todayinenergy.xml'),
                    News(name='EIA_thisweek_petroleum', src='rss',
                         url='https://www.eia.gov/petroleum/weekly/includes/week_in_petroleum_rss.xml'),
                ],
            # 'mail_wsj_chatid': '-1001754209136',
            # 'mail_wsj':
            #     [
            #         Mail(box='WSJ_NEWS', sender='The Wall Street Journal.',
            #              url_conditions=['www.wsj.com', 'wsj_author_alert'], filter_linktext="Read More"),
            #         # Mail(box='WSJ_NEWS', sender='The Wall Street Journal.',
            #         #      url_conditions=['www.wsj.com', 'panda_wsj_digest']),
            #         # Mail(box='WSJ_NEWS', sender='WSJ Follow Alert',
            #         #      url_conditions=['www.wsj.com', 'wsj_author_alert'])
            #     ],

            # 'mail_reuters_chatid': '-1001585250010',
            # 'mail_reuters':
            #     [
            #         Mail(box='REUTERS', sender='Reuters Business',
            #              url_conditions=['www.reuters.com', 'Reuters', 'Business'],
            #              filter_linktext="Read More"),
            #         Mail(box='REUTERS', sender='Reuters Global Investor',
            #              url_conditions=['www.reuters.com', 'Investor'],
            #              filter_linktext="Read More"),
            #         Mail(box='REUTERS', sender='Reuters Technology Roundup',
            #              url_conditions=['www.reuters.com', 'Technology', 'Roundup'],
            #              filter_linktext="Read More")
            #     ],

            # 'mail_statista_chatid': '-1001854256703',
            # 'mail_statista':
            #     [
            #         Mail(box='STATISTA', sender='Statista Daily Data - Late Edition', url_conditions=['statista.com', 'chart']),
            #         Mail(box='STATISTA', sender='Statista Daily Data - Early Edition', url_conditions=['statista.com', 'chart'])
            #     ],

            # 'rss_bok_chatid': '-1001558520951',
            # 'rss_bok':
            #     [
            #         News(name='경제전망보고서', src='rss',
            #              url='https://www.bok.or.kr/portal/bbs/P0002359/news.rss?menuNo=200066'),
            #         News(name='금융안정보고서', src='rss',
            #              url='https://www.bok.or.kr/portal/bbs/P0000593/news.rss?menuNo=200769'),
            #         News(name='통화신용정책보고서', src='rss',
            #              url='https://www.bok.or.kr/portal/bbs/B0000156/news.rss?menuNo=200754'),
            #         News(name='뉴욕사무소 ', src='rss',
            #              url='https://www.bok.or.kr/portal/bbs/P0002017/news.rss?menuNo=200365'),
            #         News(name='워싱턴주재원', src='rss',
            #              url='https://www.bok.or.kr/portal/bbs/P0002223/news.rss?menuNo=200082'),
            #         News(name='프랑크푸르트사무소', src='rss',
            #              url='https://www.bok.or.kr/portal/bbs/P0002226/news.rss?menuNo=200083'),
            #         News(name='동경사무소', src='rss',
            #              url='https://www.bok.or.kr/portal/bbs/P0002229/news.rss?menuNo=200084'),
            #         News(name='런던사무소', src='rss',
            #              url='https://www.bok.or.kr/portal/bbs/P0002231/news.rss?menuNo=200085'),
            #         News(name='북경사무소', src='rss',
            #              url='https://www.bok.or.kr/portal/bbs/P0002232/news.rss?menuNo=200086'),
            #         News(name='홍콩주재원', src='rss',
            #              url='https://www.bok.or.kr/portal/bbs/P0002233/news.rss?menuNo=200087'),
            #         News(name='상해주재원 ', src='rss',
            #              url='https://www.bok.or.kr/portal/bbs/P0002234/news.rss?menuNo=200088'),
            #         News(name='이슈및관련자료 ', src='rss',
            #              url='https://www.bok.or.kr/portal/bbs/P0002897/news.rss?menuNo=200788'),
            #     ],



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




