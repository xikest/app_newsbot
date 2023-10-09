from typing import Generator
import time
import asyncio
from bot.handler.contents_hanlder import ContentsHandler
from bot.src_alert import Src_Alert
from info.sender import Bot_Profiles

class Bot_Alert():
  STATUS = True
  STOP = False

  def __init__(self):
    self._TOKEN = Bot_Profiles().get_token()
    self.src = Src_Alert()
    pass
  @property
  def getToken(self):
    return self._TOKEN
  @getToken.setter
  def setToken(self, token:str = None):
        # 입력된 토큰이 None인 경우 빈 문자열로 설정
        self._TOKEN = token if token is not None else ''

  async def start(self, waitTime:int = 1800):
            while Bot_Alert.STATUS != Bot_Alert.STOP:
                try:
                    await self.update(self.src.generator)
                    print(f'cycle finish, sleep {time.time()}')
                    await asyncio.sleep(waitTime) #5분 대기
                    print(f'awake{time.time()}')
                except Exception as e:
                    print(f'bot start err.{e}')

  async def update(self, generatorForContext:Generator):
            start = time.time()
            async for context in generatorForContext(): 
                      # print(f"bot alert: {context}")
                      await ContentsHandler(context).sendTo(self.getToken)
            end = time.time()
            print(f'context time taken: {(end - start)}')
            await asyncio.sleep(5)


