# import asyncio
# import telegram

# class TelegramBot:
#   """
#   token = '5419434216:AAGf88KSC0ETWkSkogbf3N7pmzcQEG0PAQ8'
#   beta_chat_id= '-1001601197449'
#   bot = TelegramBot(token=token, chat_id=beta_chat_id)
  
#   loop = asyncio.get_event_loop()
#   group = asyncio.gather(bot.send_message('start hi'),
#                         bot.send_message('start hi2'), return_exceptions=True)
#   loop.run_until_complete(group)
#   loop.close()
#   """
#   def __init__(self, token:str=None):
#     self._token=token
#     pass

#   @property 
#   def getToken(self): return self._token
#   @getToken.setter
#   def setToken(self,token:str): self._token=token

#   def get_chat_id(self):
#     return [i.message['chat']['id'] for i in telegram.Bot(self._token).getUpdates()][0]
  
    
#   def send_message(self, chat_id:str, text:str):
#       telegram.Bot(self.getToken).sendMessage(chat_id=chat_id, text=text)  #url만 발송
#       return self
        
#   def send_image(self, chat_id:str, photo, byte=True):
#       if byte is False : photo = open(photo, 'rb')
#       telegram.Bot(self.getToken).send_photo(chat_id = chat_id, photo=photo)
#       return self
            