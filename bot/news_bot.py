from typing import AsyncGenerator
import os
import logging
from bot.handler import Handler
from bot.feeder import Feeder


class NewsBot():
  def __init__(self):
    
    self.feeder = Feeder(feeds_path = 'https://raw.githubusercontent.com/xikest/app_newsbot/main/json/feeds.json')
    
    self.firestore = "json/web-driver.json"
    self.bot_token = os.environ.get("BOT_TOKEN")
    self.gpt_api_key = os.environ.get("GPT_API_KEY")
    self.gpt_model = os.getenv("GPT_MODEL", "gpt-4o-mini")
    self.ydown_url = os.getenv("ydown_url")
    self.storage_name = os.getenv("news_bot_storage_name")
    pass


  async def start(self):
    try:
        await self.update(self.feeder.generator)
    except Exception as e:
        logging.info(f'bot start err.{e}')
    
  async def update(self, context_generator_from_feed:AsyncGenerator):
            async for context in context_generator_from_feed():
                    await Handler(context=context, token=self.bot_token, 
                                  gpt_key=self.gpt_api_key, gpt_model=self.gpt_model, 
                                  firestore_auth=self.firestore, ydown_url= self.ydown_url,
                                  storage_name = self.storage_name).send_content(storage_name='news_collection')


        
