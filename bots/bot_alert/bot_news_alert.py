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
  
  
  async def start(self,genContent_list:Generator):
            while True:
                try:
                    await self.updateMassgeFromGenerators(genContent_list)
                    print(f'cycle finish, sleep {time.time()}')
                    await asyncio.sleep(1800) #5분 대기
                    print(f'awake{time.time()}')
                except:
                    pass


#======================
# 내부 함수
#======================
  def updateMassgeFromGenerators(self, genContent_list:Generator):
      return asyncio.gather(*[self.update(genContent, delay=i) for  i, genContent in enumerate(genContent_list())]) 

  async def update(self, genContent:Generator, delay:Union[int, float]=0):
            start = time.time()
            for context in genContent(): await Contents(context).sendTo(self.getToken, delay=delay)
            end = time.time()
            print(f'context time taken: {(end - start)}')
              

