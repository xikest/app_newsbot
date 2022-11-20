from typing import Optional
import time
from typing import List
import tweepy
from info.ids import Ids
from .src_generator import SrcGenerator
from tools.telegram_bot.contents import Context

#####SRC News에 통합


class SrcTwt:
  
  """
  SrcTwt.set_screen_names(['financialjuice'])
  SrcTwt.set_BEARER_TOKEN(bearer_token)
  list(SrcTwt.gen_twt())

  Returns:
      _type_: _description_

  Yields:
      _type_: _description_
  """
  _defaultChatID:Optional[str]=None
  _screen_names:List[str]=None
  _BEARER_TOKEN:Optional[str]=None

  @classmethod
  def getChatId(cls):
    return cls._defaultChatID
  
  @classmethod
  def setChatId(cls, defaultChatID:str):
    cls._defaultChatID = defaultChatID
    
    
  @classmethod
  def get_screen_names(cls)->List:
    return cls._screen_names
  
  @classmethod
  def set_screen_names(cls, screen_names:List[str]):
    cls._screen_names = screen_names
    
    
  @classmethod
  def get_BEARER_TOKEN(cls)->str:
    return cls._BEARER_TOKEN
  
  @classmethod
  def set_BEARER_TOKEN(cls, BEARER_TOKEN:Optional[str]=None):
    cls._BEARER_TOKEN = BEARER_TOKEN
    
    
  @staticmethod
  def gen_twt()-> List[Context]: 
    for screen_name in SrcTwt.get_screen_names():
        for tweet in SrcTwt.get_msg(screen_name):
            yield Context(content=tweet, label=screen_name, dtype='msg', botChatId=SrcTwt.getChatId())
            
  @staticmethod
  def get_msg(screen_name:str='financialjuice') -> str:
          client = tweepy.Client(SrcTwt.get_BEARER_TOKEN())
          t_id = client.get_user(username=screen_name).data.id # get_id
          try :
                  paginator = iter(tweepy.Paginator(client.get_users_tweets, t_id, max_results=50))
                  response = next(paginator)
                  for tweets in response.data:
                      time.sleep(1) # 10초 슬립
                      yield tweets.text
                      print(f' get finish')
          except:
                pass    



