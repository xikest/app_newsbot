import asyncio
from typing import Generator, Optional, Union
import time
import asyncio
import telegram

from tools.telegram_bot import Contents

class BotAlert():
  """
  """
  status = True
  STOP = False
  
  def __init__(self, token:Optional[str]=None):
    super().__init__()
    self._token = token
    pass
    # self.bot = TelegramBot(token)
    # self.contents = Contents()

  @property
  def getToken(self):
    return self._token
  
  @getToken.setter
  def setToken(self, token:Optional[str]=None):
    self._token = token
  
  async def get_chatId(self):
        bot = telegram.Bot(self.getToken)
        async with bot:
          print((await bot.get_updates())[0])
  
  
  async def start(self,generator:Generator, waitTime=1*60):
            while BotAlert.status != BotAlert.STOP:
                try:
                    await self.update(generator)
                    print(f'cycle finish, sleep {time.time()}')
                    await asyncio.sleep(waitTime) #5분 대기
                    print(f'awake{time.time()}')
                except Exception as e:
                    print(f'bot start err.{e}')
                    pass


#======================
# 내부 함수
#======================

  async def update(self, generatorForContext:Generator, delay:Union[int, float]=0):
            start = time.time()
            async for context in generatorForContext(): 
                      # print(f"bot alert: {context}")
                      await Contents(context).sendTo(self.getToken, delay=delay)
            end = time.time()
            print(f'context time taken: {(end - start)}')
            await asyncio.sleep(5)