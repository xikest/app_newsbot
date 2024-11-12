import json
from typing import AsyncGenerator
from .feed_rss import RSS
from .feed_news import NEWS
from .feed_mail import MAIL
import requests

 
class Feeder:
    def __init__(self, feeds_path:json):
        self.feeds_dict = {
            # 'mail': 'MAIL',
            'rss': RSS,
            'news': NEWS,
        }
        
        try: 
            with open(feeds_path, 'r', encoding='utf-8') as file:
                self.src_json = json.load(file)
        except:
            response = requests.get(feeds_path)
            if response.status_code == 200:
                self.src_json = json.loads(response.text)
            else:
                print(f"Error: {response.status_code}")


    async def generator(self) -> AsyncGenerator:
        for category in list(self.src_json.keys()):
            feeder = self.feeds_dict.get(category)
            for src_params in self.src_json.get(category):
                try:
                    async for context in feeder(**src_params).generator():
                        yield context  
                except:
                    continue

