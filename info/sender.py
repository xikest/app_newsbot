import os

class Sender:
    def __init__(self):
        self.bot_token = '5753698180:AAEgXUBlwPeDmRGRGGmt9NpcE3JqyLYrMbU'
        # self.bot_token = os.environ.get("BOT_TOKEN")
        self.gpt_api_key = os.environ.get("GPT_API_KEY")

    def get_token(self)->str:
        return self.bot_token

    def get_gptkey(self)->str:
        return self.gpt_api_key