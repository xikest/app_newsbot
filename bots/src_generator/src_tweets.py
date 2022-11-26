
from typing import Optional, List,Generator
import tweepy
from tools.telegram_bot.contents import Context
from tools.translate.papago import Papago
# from tools.translate.google import GoogleTranslate
# from tools.translate.kakao import KakaoTranslate

import asyncio

class SrcTweets:

    def __init__(self, BEARERTOKEN:Optional[str], screenNames:Generator, ChatId:Optional[str]):
        self._ChatId:Optional[str]=ChatId
        self._BEARERTOKEN = BEARERTOKEN
        self._screenNames:Generator = screenNames

        
        
    async   def generator(self)-> Context: 
            for screenName in self._screenNames : # following 리스트
                client = tweepy.Client(self._BEARERTOKEN)
                t_id = self.get_id(client, screenName) # get_id
                tweets = client.get_users_tweets
                async   for tweet_msg in self.get_msg(tweets, t_id, screenName):
                        yield Context(content=[tweet_msg], label=screenName, dtype='msg', botChatId=self._ChatId)
                        

    async   def get_msg(self, tweets, t_id, screenName:str='financialjuice') -> str:                
                try :
                        if t_id is None: raise Exception('failed get tweets id')
                        paginator = iter(tweepy.Paginator(tweets, t_id, max_results=50))
                        response = next(paginator)
                        
                        for tweet in response.data[::-1]:
                            if '@' not in tweet.text:
                                res = await Papago('en').translate(tweet.text)
                                print(res)
                                yield f"#{screenName}\n{res}\n\n{tweet.text}"
                                # yield f"#{screenName}\n{await GoogleTranslate('en').eng2kor(tweet.text)}\n\n{tweet.text}"
                                # yield f"#{screenName}\n{KakaoTranslate.eng2kor(tweet.text)}\n\n{tweet.text}"
                except Exception as e:
                    print(f'tweets error msg : {e}')
                    await asyncio.sleep(15*60)    

    def get_id(self, client, screenName:str) -> str:
        try:
            return client.get_user(username=screenName).data.id # get_id
        except:
            raise Exception(f'tweets error id')
            


        