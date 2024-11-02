import os
import json
import logging

class Sender:
    def __init__(self):
        self.bot_token = os.environ.get("BOT_TOKEN")
        self.gpt_api_key = os.environ.get("GPT_API_KEY")
        self.firestore = "web-driver.json"

    def get_token(self)->str:
        return self.bot_token

    def get_gptkey(self)->str:
        return self.gpt_api_key
    
    def get_firestore_path(self)->str:
        return self.firestore