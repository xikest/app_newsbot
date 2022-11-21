from typing import Optional
from telegram.ext import Updater
import logging
from bots.bot_xiks.basic_handler import BasicHandler
from bots.bot_xiks.command_handler import CmdHandler
import asyncio

import logging

from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

    
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)

class Echobot():
    def __init__(self, TOKEN:Optional[str]=None):  self._TOKEN = TOKEN
 
    @property
    def getToken(self)-> str: return self._TOKEN
    
    @getToken.setter
    def setToken(self, TOKEN:Optional[str]=None) -> None: self._TOKEN = TOKEN



    def start(self):
            updater = Updater(self.getToken)
            dispatcher = updater.dispatcher
            dispatcher.add_handler(BasicHandler.start())
            dispatcher.add_handler(BasicHandler.help())
            # dispatcher.add_handler(BasicHandler.echo())
            dispatcher.add_handler(BasicHandler.inline_caps())
            
            dispatcher.add_handler(CmdHandler.shillerRatio())
            dispatcher.add_handler(CmdHandler.mkPtn_m())
            dispatcher.add_handler(CmdHandler.mkPtn_w())
            dispatcher.add_handler(CmdHandler.fed())  
            dispatcher.add_handler(CmdHandler.cpi())
            dispatcher.add_handler(CmdHandler.reatailSales())
            dispatcher.add_handler(CmdHandler.newResidentialSales())
            dispatcher.add_handler(CmdHandler.durableGoods())    
            dispatcher.add_handler(CmdHandler.pce()) 
            dispatcher.add_handler(CmdHandler.employmentCostIndex())    
            dispatcher.add_handler(CmdHandler.gdp())  
            dispatcher.add_handler(CmdHandler.jolt())    
            dispatcher.add_handler(CmdHandler.adpNationalEmploymentReport())  
            dispatcher.add_handler(CmdHandler.diffusionIndexphiladelphia())   
            dispatcher.add_handler(CmdHandler.inventoriesSalesRatio())         
            dispatcher.add_handler(CmdHandler.ppi())
            dispatcher.add_handler(CmdHandler.cfnai())    
            dispatcher.add_handler(CmdHandler.empireStateManufacturingSurvey())  
            dispatcher.add_handler(CmdHandler.existingHomeSales())   
            dispatcher.add_handler(CmdHandler.industrialProduction())         
            dispatcher.add_handler(CmdHandler.ism())  
            dispatcher.add_handler(CmdHandler.productivity())    
            dispatcher.add_handler(CmdHandler.initialClaims())  
            dispatcher.add_handler(CmdHandler.ecommerce_retailes())   
            dispatcher.add_handler(CmdHandler.import_export())         
            dispatcher.add_handler(CmdHandler.cassFreightIndex())
            dispatcher.add_handler(CmdHandler.newHousing())    
            dispatcher.add_handler(CmdHandler.consumerCredit())  
            dispatcher.add_handler(CmdHandler.cpi_bra())   
            dispatcher.add_handler(CmdHandler.cpi_chn())         
            dispatcher.add_handler(CmdHandler.cpi_de())  
            dispatcher.add_handler(CmdHandler.cpi_inida())   
            dispatcher.add_handler(CmdHandler.cpi_jpn())  
            dispatcher.add_handler(CmdHandler.cpi_kr())   
            updater.start_polling()

            
 