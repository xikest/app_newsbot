from typing import Generator, Optional, Union
import time
import asyncio
from bot.handler.contents_hanlder import ContentsHandler
from bot.src_alert import Src_alert
from info.sender import BotProfiles

class Bot_Alert():

  def __init__(self):
    self._token:str = None
    self.setToken(token=BotProfiles.get_token())
    self.src = Src_alert()
    pass
  @property
  def getToken(self):
    return self._token
  @getToken.setter
  def setToken(self, token: Optional[str] = None):
        # 입력된 토큰이 None인 경우 빈 문자열로 설정
        self._token = token if token is not None else ''
  async def start(self, waitTime=30 * 60):
            try:
                await self.update(self.src.generator)
                print(f'cycle finish, sleep {time.time()}')
                await asyncio.sleep(waitTime) #5분 대기
                print(f'awake{time.time()}')
            except Exception as e:
                print(f'bot start err.{e}')

  async def update(self, generatorForContext:Generator, delay:Union[int, float]=0):
            start = time.time()
            async for context in generatorForContext(): 
                      # print(f"bot alert: {context}")
                      await ContentsHandler(context).sendTo(self.getToken)
            end = time.time()
            print(f'context time taken: {(end - start)}')
            await asyncio.sleep(5)


