from typing import Generator
import time
import asyncio
from bot.handler.contents_hanlder import ContentsHandler
from bot.src_alert import Src_Alert
import logging
from tools.gcp.firestoremanager import FirestoreManager
from info.sender import Sender
import gzip
import pickle
from pathlib import Path


class Bot_Alert():
  def __init__(self):
    self.src = Src_Alert()
    self.storage_name='app_newsbot_contents'
    pass


  async def start(self):
    try:
        firestore_path = Sender().get_firestore_path()
        firestore_storage = FirestoreManager(firestore_path)
        data_list = firestore_storage.read_list(self.storage_name)
        save_to_pickle(data_list, self.storage_name)
        
        await self.update(self.src.generator)
        
        data_list = load_from_pickle(self.storage_name)
        firestore_storage.save_list({self.storage_name: data_list})
        
    except Exception as e:
        logging.info(f'bot start err.{e}')

  async def update(self, generatorForContext:Generator):
            start = time.time()
            async for context in generatorForContext(): 
                      await ContentsHandler(context).send_contents(storage_name='app_newsbot_contents')
            end = time.time()
            logging.info(f'context time taken: {(end - start)}')
            await asyncio.sleep(5)


def load_from_pickle(storage_name, data_path: Path = Path.cwd()):
    with gzip.open(f"{data_path}/{storage_name}.pickle", 'rb') as f:
        return pickle.load(f)

def save_to_pickle(data, storage_name, data_path: Path = Path.cwd()):
    with gzip.open(f"{data_path}/{storage_name}.pickle", 'wb') as f:
        pickle.dump(data, f)