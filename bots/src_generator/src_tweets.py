
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
            # print('generator')
            try: 
                for screenName in self._screenNames() : # following 리스트
                        # print(screenName)
                        client = tweepy.Client(self._BEARERTOKEN)
                        t_id = await self.get_id(client, screenName) # get_id
                        tweets = client.get_users_tweets
                        async for tweet_msg in self.get_msg(tweets, t_id):
                                # print(f'tweet_msg generator : {tweet_msg}')
                                # await asyncio.sleep(1)
                                yield Context(content=[tweet_msg], label=f'{screenName}', summary=[tweet_msg], enable_translate = True, botChatId=self._ChatId,  dtype='msg')
            except Exception as e:
                print(f"tweets body error: {e}")
                pass



    async   def get_msg(self, tweets, t_id) -> str:                
                try :
                        if t_id is None: raise Exception('failed get tweets id')
                        paginator = iter(tweepy.Paginator(tweets, t_id, max_results=5))
                        response = next(paginator)
                        
                        for tweet in response.data[::-1]:
                            if '@' not in tweet.text:
                                # print('get_msg')
                                # await asyncio.sleep(1)
                                yield tweet.text
                except Exception as e:
                    print(f'tweets connect error, sleep 15min.: {e}')
                    await asyncio.sleep(15*60)    



    async   def get_id(self, client, screenName:str) -> str:
                try:
                    return client.get_user(username=screenName).data.id # get_id
                except:
                    raise Exception(f'tweets error id')
            


        