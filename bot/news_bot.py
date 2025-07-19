from typing import AsyncGenerator
import os
import hashlib
import logging
import pandas as pd
from datetime import datetime
from tools.gcp.cloud_storage import ParquetHandler
from bot.feeder import Feeder
import pytz
import time

def get_today_date():
    tz = pytz.timezone('Europe/Moscow')# 미국 동부 기준 오후 5시, 한국 기준 오전 7시, 러시아 기준 자정
    ## 모스코바 자정으로하여 한국 확인 시점에 이전 기사 획득득
    # tz = pytz.timezone('America/New_York')
    
    today = datetime.now(tz)
    return today.strftime('%Y-%m-%d')


class NewsBot():
  def __init__(self, storage_auth=None, storage_property:dict={"bucket_name":"news_collection", "src_filename":"news_collection.parquet"}):
    # storage_auth='json/storage.json'
    self.feeder = Feeder(feeds_path = 'https://raw.githubusercontent.com/xikest/app_newsbot/main/json/feeds.json')
    # self.feeder = Feeder(feeds_path = 'json/feeds.json')
 
    self.src_filename = storage_property.get('src_filename')
    self.storage_handler = ParquetHandler(credentials_file=storage_auth, bucket_name=storage_property.get('bucket_name'))
    try:
      self.df = self.storage_handler.read_parquet_from_gcs(self.src_filename)
    except Exception as e:
        logging.warning(f"파일을 읽을 수 없어 새 DataFrame을 생성합니다: {e}")
        self.df = pd.DataFrame(columns=["title", "date", "link"])
    pass


  async def start(self):
    try:
        await self.update(self.feeder.generator)
    except Exception as e:
        logging.error(f'bot start err.{e}')
    
  async def check_db(self):
        try:
            df = self.storage_handler.read_parquet_from_gcs(self.src_filename)
            print(df.sort_values(by='date', ascending=False).head())
            await time.sleep(1)
        except Exception as e:
            logging.error(f'bot start err.{e}')
    
  async def update(self, context_generator_from_feed:AsyncGenerator):
            def url_to_doc_key_sha256(url: str) -> str:
              return hashlib.sha256(url.encode('utf-8')).hexdigest()
            
            async for context in context_generator_from_feed():
              
                      doc_key = url_to_doc_key_sha256(context.link)
                      if doc_key in self.df.index:
                        logging.info(f"중복 뉴스 스킵: {context.link}")
                        continue
                      
                      self.df.loc[doc_key] = {
                                              "title": context.title,
                                              "date": get_today_date(),
                                              "link": context.link
                                              }
            self.storage_handler.save_parquet_to_gcs(self.src_filename, self.df) 
            logging.info("finish update")
            return None

