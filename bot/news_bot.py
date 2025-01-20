from typing import AsyncGenerator
import os
import logging
from bot.handler import Handler
from bot.feeder import Feeder


class NewsBot():
  def __init__(self):
    
    self.feeder = Feeder(feeds_path = 'https://raw.githubusercontent.com/xikest/app_newsbot/main/json/feeds.json')
    # self.feeder = Feeder(feeds_path = 'json/feeds.json')
    
    self.firestore = "json/web-driver.json"
    self.storage_name='news_collection'
    self.bot_token = os.environ.get("BOT_TOKEN")
    self.gpt_api_key = os.environ.get("GPT_API_KEY")
    pass


  async def start(self):
    try:
        await self.update(self.feeder.generator)
    except Exception as e:
        logging.info(f'bot start err.{e}')

  async def update(self, context_generator_from_feed:AsyncGenerator):
            async for context in context_generator_from_feed():
                    await Handler(context, self.bot_token, self.gpt_api_key, self.firestore).send_content(storage_name=self.storage_name)


        
