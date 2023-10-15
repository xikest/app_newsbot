from typing import Generator
from info.definition_obj import Mail, News

class Feeder:
    def __init__(self):
        self.feeder_mail_info = {
            'usr':'mail info',
            'pid': 'mail info',
        }

        # 클래스 정의에 맞춰서 작성
        # 주의: feed의 chat id는 "_chatid"를 붙여야 함, 
        # "news"의 "chatid"는 "news_chatid"라고 작성
        self.feeder_web_source = {
            'news_chatid': '[telegram chat ID]',
            'news':
                [
                    News(name='name', src='web', url='url', attr_key='parsing'),
                  ],
            'rss_articles_chatid': '[telegram chat ID]',
            'rss_articles':
                [
                    News(name='name', src='rss', url='url'),
                ],
            'mail_chatid': '[telegram chat ID]',
            'mail':
                [
                    Mail(box='mailbox', sender='sender', conditions=['parsing1', 'parsing2'])
                ]
        }
    def get_keylist(self, source_category:str='news')-> list:
        return [key.replace("_chatid", "") for key in self.feeder_web_source.keys() if source_category in key] #if category in key, return key dictionary. ex: {key: chat id}

    def get_feeds(self, source:str)-> Generator:
        yield from self.feeder_web_source.get(source)

    def get_chatId(self, source:str) -> str:
        return self.feeder_web_source.get(f"{source}_chatid")

    def get_feed_ids(self, key):
        return self.feeder_mail_info.get(key)
