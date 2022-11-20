from typing import Optional
import time
from typing import List
import tweepy
from info.ids import Ids
from .src_generator import SrcGenerator





class TweeterMsg:
    def __init__(self, BEARER_TOKEN):
        self._client =tweepy.Client(BEARER_TOKEN)

    @property
    def client(self):
        return self._client
    
    @client.setter
    def set_client(self, BEARER_TOKEN):
        self._client = tweepy.Client(BEARER_TOKEN)
    
    def  _get_id(self, screen_name):
            return self.client.get_user(username=screen_name).data.id
    
    def get_msg(self, screen_name:str='financialjuice') -> List:
            t_id = self._get_id(screen_name)

            try :
                paginator = iter(tweepy.Paginator( self.client.get_users_tweets, t_id, max_results=50))
                response = next(paginator)
                tweets_list = [tweets.text for tweets in response.data]
                time.sleep(10) # 10초 슬립
                print(f' get finish')
            except:
                pass

            return tweets_list
        


class SrcTwt:
  _defaultChatID:Optional[str]=None
  
  @classmethod
  def getChatId(cls):
    return cls._defaultChatID
  
  @classmethod
  def setChatId(cls, defaultChatID:str):
    cls._defaultChatID = defaultChatID
  

  @staticmethod
  def gen_twt()-> List[Context]: 
    # tw_lists = TweeterMsg('팔로잉할 대상') # 리스트


      yield from list_news
        
