from typing import Generator
import time
import asyncio
from bot.handler.contents_hanlder import ContentsHandler
from bot.src_alert import Src_Alert
from info.sender import Sender

class Bot_Alert():
  STATUS = True
  STOP = False
  def __init__(self):
    self._TOKEN = Sender().get_token()
    self._GPT = Sender().get_gptkey()
    self.src = Src_Alert()
    pass
  @property
  def getToken(self):
    return self._TOKEN

  @property
  def getGpt(self):
    return self._GPT

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
                      await ContentsHandler(context).send_to(self.getToken, self._GPT)
            end = time.time()
            print(f'context time taken: {(end - start)}')
            await asyncio.sleep(5)


