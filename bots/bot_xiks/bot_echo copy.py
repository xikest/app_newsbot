from tools.telegram_bot.telegram_bot import TelegramBot
from .basic_handler import EventHandler
from telegram.ext import Updater, CallbackQueryHandler
from telegram.ext import MessageHandler, Filters, CommandHandler  
import asyncio
from typing import Generator, List, Callable, Optional

class Echobot(TelegramBot):
    # def __init__(self, bot):
    def __init__(self, token:Optional[str]=None):
        self._token = token
        # TelegramBot.__init__(self, self.getToken)
        # self = bot

        pass

    @property
    def getToken(self):
        return self._token
    
    @getToken.setter
    def setToken(self, token:Optional[str]=None):
        self._token = token

    # def update(self):
    #     self.updater = Updater(token=self.getToken, use_context=True)
    #     self.dispatcher = self.updater.dispatcher
    #     (self.add_message_handler()
    #         .add_help_handler()
    #         .add_photo_handler()
    #         .add_file_handler()
    #         .add_btn_handler())
    #     self.start()
 
    async	def start(self):
                self.updater = Updater(token=self.getToken, use_context=True)
                self.dispatcher = self.updater.dispatcher
                (self.add_message_handler()
                    .add_help_handler()
                    .add_cmd_handler()
                    .add_photo_handler()
                    .add_file_handler()
                    .add_btn_handler())
                await	self.updater.start_polling(timeout=3)
            
 # async   def stop(self):
 #            await   Updater(token=self.getToken).stop()


    def add_message_handler(self):
        message_handler = MessageHandler(Filters.text & (~Filters.command), EventHandler.get_message) # 메세지중에서 command 제외
        self.dispatcher.add_handler(message_handler)
        return self

    def add_help_handler(self):
        help_handler  = CommandHandler('help', EventHandler.help_command)
        self.dispatcher.add_handler(help_handler)
        return self   


# shiller_ratio - 쉴러 PE Ratio
# market_pattern - market_pattern
# cpi - cpi
# reatail_sales - 소매 판매 보고서

    def add_cmd_handler(self):
        self.dispatcher.add_handler( CommandHandler('shiller_ratio', EventHandler.shri_command))
        self.dispatcher.add_handler(CommandHandler('market_pattern', EventHandler.mkptn_command))
        self.dispatcher.add_handler(CommandHandler('cpi', EventHandler.cpi_command))
        self.dispatcher.add_handler(CommandHandler('reatail_sales', EventHandler.reatailSales_command))
        
        return self   

    def add_file_handler(self):
        file_handler = MessageHandler(Filters.document, EventHandler.get_file)
        self.dispatcher.add_handler(file_handler)
        return self


    def add_photo_handler(self):
        photo_handler  = MessageHandler(Filters.photo, EventHandler.get_photo)
        self.dispatcher.add_handler(photo_handler)
        return self
    
        
    def add_btn_handler(self):
        self.set_btn_handler().set_btn_action_handler() 
        return self
        
    def set_btn_handler(self):
        btn_handler = CommandHandler("task", EventHandler.btns_task)
        self.dispatcher.add_handler(btn_handler)
        return self
        
    def set_btn_action_handler(self):
        btn_action_handler =CallbackQueryHandler(EventHandler.btns_action)
        self.dispatcher.add_handler(btn_action_handler)
        return self


