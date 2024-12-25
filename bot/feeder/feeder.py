import json
import requests
import logging
from typing import AsyncGenerator
from .feed_rss import RSS
from .feed_news import NEWS
from .feed_mail import MAIL

 
class Feeder:
    def __init__(self, feeds_path:json):
        self.feeder_dict = {
            'mail': MAIL,
            # 'rss': RSS,
            # 'news': NEWS,
        }
        
        try: 
            with open(feeds_path, 'r', encoding='utf-8') as file:
                self.src_json = json.load(file)
        except:
            response = requests.get(feeds_path)
            if response.status_code == 200:
                self.src_json = json.loads(response.text)
            else:
                logging.error(f"Error: {response.status_code}")


    async def generator(self) -> AsyncGenerator:
        for category in list(self.src_json.keys()):
            for src_params in self.src_json.get(category):
                try:
                    feeder = self.feeder_dict.get(category)
                    async for context in feeder(**src_params).generator():
                        yield context  
                except:
                    continue

