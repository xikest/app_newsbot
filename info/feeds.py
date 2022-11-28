from dataclasses import dataclass



@dataclass
class News:
    name:str
    src:str
    url:str
    attr_key:str = None
    selector:str = None
    prefix:str = None
    class_key:str = None
    enable_translate:bool = False
    
    
@dataclass
class Mail:
    box:str
    sender:str
    
   
    


class FeedFlowwings:
    @staticmethod
    def get_rss_urls():
        yield from [
                    News(name='fred_blog', src='rss', url='http://fredblog.stlouisfed.org/feed/', enable_translate=True),
                    News(name='EIA_today_energy', src='rss', url='https://www.eia.gov/rss/todayinenergy.xml', enable_translate=True),
                    News(name='EIA_thisweek_petroleum', src='rss_s', url='https://www.eia.gov/petroleum/weekly/includes/week_in_petroleum_rss.xml', enable_translate=True),
                    News(name='GDP_NOW', src='rss', url='https://www.atlantafed.org/rss/GDPNow', enable_translate=True),
                    News(name='fred_blog', src='rss', url='http://fredblog.stlouisfed.org/feed/', enable_translate=True),
                    News(name='opec_basketprice', src='rss', url=' https://www.opec.org/opec_web/en/basket.rss', enable_translate=True),
                    News(name='중국_소식', src='googleAlert', url='https://www.google.co.kr/alerts/feeds/11305193269230284098/15091211705036215232'),
                    News(name='중동_소식', src='googleAlert', url='https://www.google.co.kr/alerts/feeds/11305193269230284098/10207016080645967575'),
                    # News(name='다모다란_교수', src='rss', url='https://aswathdamodaran.blogspot.com/feeds/posts/default'),
                    ]




    @staticmethod
    def get_news_urls():
        yield from [            
                    News(name='한경_글로벌마켓', src='web', url = 'https://www.hankyung.com/globalmarket/news/hot-stock', attr_key='list_top_thumb'),
                    News(name='한경_월스리트나우',src='web', url='https://www.hankyung.com/globalmarket/news/wallstreet-now', attr_key='list_thumb_rowtype'),
                    News(name='한경_경제', src='web', url = 'https://www.hankyung.com/economy', attr_key='main-headline'),
                    News(name='한경_금융', src='web',url = 'https://www.hankyung.com/financial-market', attr_key='main-headline'),
                    News(name='한경_집코노미', src='web', url = 'https://www.hankyung.com/realestate', attr_key='main-headline'),
                    # News(name='한경 집코노미 주요 기사', src='web', url = 'https://www.hankyung.com/realestate', attr_key='main-jipconomy'),
                    # News(name='einfomax', src='webWithoutHttp', url = 'https://news.einfomax.co.kr/', attr_key='auto-article auto-db02 db05', prefix='https://news.einfomax.co.kr/'),
                    News(name='einfomax_정책금융', src='webWithoutHttp', url = 'https://news.einfomax.co.kr/news/articleList.html?sc_section_code=S1N15&view_type=sm', attr_key='auto-article auto-db01', prefix='https://news.einfomax.co.kr/'),
                    # News(name='einfomax', src='webWithoutHttp', url = 'https://news.einfomax.co.kr/', attr_key='auto-article auto-db01', prefix='https://news.einfomax.co.kr/'),
                    News(name='einfomax_채권외환', src='webWithoutHttp',  url ='https://news.einfomax.co.kr/news/articleList.html?sc_section_code=S1N16&view_type=sm', attr_key='auto-article auto-db01', prefix='https://news.einfomax.co.kr/'),
                    News(name='einfomax_해외주식', src='webWithoutHttp', url ='https://news.einfomax.co.kr/news/articleList.html?sc_section_code=S1N21&view_type=sm', attr_key='auto-article auto-db01', prefix='https://news.einfomax.co.kr/'),
                    News(name='einfomax_글로벌경제', src='webWithoutHttp', url ='https://news.einfomax.co.kr/news/articleList.html?sc_section_code=S1N4&view_type=sm', attr_key='auto-article auto-db01', prefix='https://news.einfomax.co.kr/'),
                    News(name='einfomax_중국경제', src='webWithoutHttp',  url ='https://news.einfomax.co.kr/news/articleList.html?sc_section_code=S1N18&view_type=sm', attr_key='auto-article auto-db01', prefix='https://news.einfomax.co.kr/'),
                    # News(name='브릿지워터', src='web',  url ='https://www.bridgewater.com/research-and-insights', attr_key = 'MasonryList')
                    ]

    @staticmethod
    def get_mailing():
        yield from [Mail(box='WSJ', sender='WSJ Follow Alert')]
                   
   
    @staticmethod
    def get_screenNames():      
            yield from ['financialjuice', #매크로
                        'NickTimiraos', #Fed
                       'Fxhedgers',  #fx
                       'unusual_whales',
                        'Amena_Bakr',  # 오일
                        'staunovo',  #원자재 애널리스트
                        'DanielTNiles', #댄 나일스, 사토리 펀드 설립자
                       'michaeljburry']  #마이클 버리
            # 'ConsensusGurus',