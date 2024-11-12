from typing import AsyncGenerator
import os
import logging
from bot.handler import Handler
from bot.feeder import Feeder
from tools.gcp.firestoremanager import FirestoreManager
from tools.file.filemanager import FileManager



class NewsBot():
  def __init__(self):
    
    self.feeder = Feeder(feeds_path = 'https://raw.githubusercontent.com/xikest/app_newsbot/main/json/feeds.json')
    self.firestore = "json/web-driver.json"
    self.storage_name='app_newsbot_contents'
    self.bot_token = os.environ.get("BOT_TOKEN")
    self.gpt_api_key = os.environ.get("GPT_API_KEY")
    pass


  async def start(self):
    try:
        firestore_storage = FirestoreManager(self.firestore)
        data_list = firestore_storage.read_list(self.storage_name)
        FileManager.save_to_pickle(data_list, self.storage_name)
        
        await self.update(self.feeder.generator)
        
        data_list = FileManager.load_from_pickle(self.storage_name)
        firestore_storage.save_list({self.storage_name: data_list})
        
    except Exception as e:
        logging.info(f'bot start err.{e}')

  async def update(self, context_generator_from_feed:AsyncGenerator):
            async for context in context_generator_from_feed(): 
                      await Handler(context, self.bot_token, self.gpt_api_key).send_content(storage_name='app_newsbot_contents')


        
