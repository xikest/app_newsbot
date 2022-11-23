
from typing import Optional, List
import tweepy
from tools.telegram_bot.contents import Context
from info.ids import Ids
from info.twt_following import TweetsFlw


class Tweets:


    def __init__(self, BEARER_TOKEN:Optional[str], screen_names:List[str]):
        """
        
        BEARER_TOKEN = Ids.twt_beartoken()    # 트위터 접근 토큰
        gen_twt = Tweets(BEARER_TOKEN, screen_names).setChatId(chat_id).gen_twt()
        
        

        Args:
            BEARER_TOKEN (Optional[str]): _description_
            screen_names (List[str]): _description_
        """

        self._ChatId:Optional[str]=None
        self._BEARER_TOKEN = BEARER_TOKEN
        self._screen_names = screen_names

    def getChatId(self):
        if self._ChatId is None:self.setChatId(self.getChatId())
        return self._ChatId

    def setChatId(self, ChatId:str):
        self._ChatId = ChatId
        return self
        
    def gen_twt(self)-> List[Context]: 
        for screen_name in self._screen_names : # following 리스트
            for tweet in self.get_msg(screen_name):
                yield Context(content=tweet, label=screen_name, dtype='msg', botChatId=self.getChatId())
                

    def get_msg(self, screen_name:str='financialjuice') -> str:
        client = tweepy.Client(self._BEARER_TOKEN)
        t_id = client.get_user(username=screen_name).data.id # get_id
        try :
                paginator = iter(tweepy.Paginator(client.get_users_tweets, t_id, max_results=50))
                response = next(paginator)
                for tweets in response.data:

                    if '@' not in tweets.text:
                        yield [ f"#{screen_name}\n{KakaoTranslate.eng2kor(tweets.text)}/n{tweets.text}"]
        except:
                pass    


 