from collections import namedtuple
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
    



class FeedFlowwings:
    @staticmethod
    def get_rss_urls():
        yield from [News(name='뉴스핌', src='googleAlert', url='https://www.google.co.kr/alerts/feeds/11305193269230284098/15091211705036215232'),
                    News(name='인남식', src='googleAlert', url='https://www.google.co.kr/alerts/feeds/11305193269230284098/10207016080645967575'),
                    News(name='다모다란', src='rss', url='https://aswathdamodaran.blogspot.com/feeds/posts/default'),
                    News(name='GDP NOW', src='rss', url='https://www.atlantafed.org/rss/GDPNow'),
                    News(name='EIA today energy', src='rss', url='https://www.eia.gov/rss/todayinenergy.xml'),
                    News(name='EIA thisweek_petroleum', src='rss', url='https://www.eia.gov/petroleum/weekly/includes/week_in_petroleum_rss.xml')
                    ]

    @staticmethod
    def get_news_urls():
        yield from [News(name='한경 글로벌 마켓 핫 스탁', src='web', url = 'https://www.hankyung.com/globalmarket/news/hot-stock', attr_key='list_top_thumb'),
                    News(name='한경 월스리트 나우',src='web', url='https://www.hankyung.com/globalmarket/news/wallstreet-now', attr_key='list_thumb_rowtype'),
                    News(name='한경 경제 탑기사', src='web', url = 'https://www.hankyung.com/economy', attr_key='main-headline'),
                    News(name='한경 금융 탑기사', src='web',url = 'https://www.hankyung.com/financial-market', attr_key='main-headline'),
                    # News(name='한경 집코노미 탑기사', src='web', url = 'https://www.hankyung.com/realestate', attr_key='main-headline'),
                    # News(name='한경 집코노미 주요 기사', src='web', url = 'https://www.hankyung.com/realestate', attr_key='main-jipconomy'),
                    News(name='연포 인포 맥스 많이 본 뉴스', src='webWithoutHttp', url = 'https://news.einfomax.co.kr/', attr_key='auto-article auto-db01', prefix='https://news.einfomax.co.kr/'),
                    News(name='연포 인포 맥스 정치', src='webWithoutHttp', url = 'https://news.einfomax.co.kr/news/articleList.html?sc_section_code=S1N15&view_type=sm', attr_key='auto-article auto-db01', prefix='https://news.einfomax.co.kr/'),
                    News(name='연포 인포 맥스 많이 본 뉴스', src='webWithoutHttp', url = 'https://news.einfomax.co.kr/', attr_key='auto-article auto-db01', prefix='https://news.einfomax.co.kr/'),
                    News(name='연포 인포 맥스 외환', src='webWithoutHttp',  url ='https://news.einfomax.co.kr/news/articleList.html?sc_section_code=S1N16&view_type=sm', attr_key='auto-article auto-db01', prefix='https://news.einfomax.co.kr/'),
                    News(name='연포 인포 맥스 주식', src='webWithoutHttp', url ='https://news.einfomax.co.kr/news/articleList.html?sc_section_code=S1N21&view_type=sm', attr_key='auto-article auto-db01', prefix='https://news.einfomax.co.kr/'),
                    News(name='연포 인포 맥스 글로벌 경제', src='webWithoutHttp', url ='https://news.einfomax.co.kr/news/articleList.html?sc_section_code=S1N4&view_type=sm', attr_key='auto-article auto-db01', prefix='https://news.einfomax.co.kr/'),
                    News(name='연포 인포 맥스 중국 경제', src='webWithoutHttp',  url ='https://news.einfomax.co.kr/news/articleList.html?sc_section_code=S1N18&view_type=sm', attr_key='auto-article auto-db01', prefix='https://news.einfomax.co.kr/')
                    ]
                    
    @staticmethod
    def get_screenNames():      
            yield from ['financialjuice',
                        'NickTimiraos']
            # 'ConsensusGurus',