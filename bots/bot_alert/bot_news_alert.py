import asyncio
from typing import Generator, List, Callable, Optional, Union
from tools.telegram_bot.contents import Contents
from tools.time.time import Timer
import time
import asyncio
import telegram

class NewsAlert():
  """
  """

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
  
  
  async def start(self,generator:Generator, waitTime=5*60):
            while True:
                try:
                    await self.update(generator)
                    print(f'cycle finish, sleep {time.time()}')
                    # await asyncio.sleep(waitTime) #5분 대기
                    print(f'awake{time.time()}')
                except:
                    pass


#======================
# 내부 함수
#======================

  async def update(self, generatorForContext:Generator, delay:Union[int, float]=0):
            start = time.time()
            async for context in generatorForContext(): 
                      await Contents(context).sendTo(self.getToken, delay=delay)
            end = time.time()
            print(f'context time taken: {(end - start)}')
            await asyncio.sleep(5)