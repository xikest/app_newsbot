from typing import Optional
from telegram.ext import Updater
import logging
from bots.bot_xiks.basic_handler import BasicHandler
from bots.bot_xiks.command_handler import CmdHandler
import asyncio

import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

    
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
            application  =  ApplicationBuilder().token(self.getToken).build()

            application.add_handler(BasicHandler.start())
            application.add_handler(BasicHandler.help())
            # application.add_handler(BasicHandler.echo())
            application.add_handler(BasicHandler.inline_caps())
            
            application.add_handler(CmdHandler.bs_stock())
            
            application.add_handler(CmdHandler.shillerRatio())
            application.add_handler(CmdHandler.mkPtn())
            application.add_handler(CmdHandler.fed())  
            application.add_handler(CmdHandler.cpi())
            application.add_handler(CmdHandler.reatailSales())
            application.add_handler(CmdHandler.newResidentialSales())
            application.add_handler(CmdHandler.durableGoods())    
            application.add_handler(CmdHandler.pce()) 
            application.add_handler(CmdHandler.employmentCostIndex())    
            application.add_handler(CmdHandler.gdp())  
            application.add_handler(CmdHandler.jolt())    
            application.add_handler(CmdHandler.adpNationalEmploymentReport())  
            application.add_handler(CmdHandler.diffusionIndexphiladelphia())   
            application.add_handler(CmdHandler.inventoriesSalesRatio())         
            application.add_handler(CmdHandler.ppi())
            application.add_handler(CmdHandler.cfnai())    
            application.add_handler(CmdHandler.empireStateManufacturingSurvey())  
            application.add_handler(CmdHandler.existingHomeSales())   
            application.add_handler(CmdHandler.industrialProduction())         
            application.add_handler(CmdHandler.ism())  
            application.add_handler(CmdHandler.productivity())    
            application.add_handler(CmdHandler.initialClaims())  
            application.add_handler(CmdHandler.ecommerce_retailes())   
            application.add_handler(CmdHandler.import_export())         
            application.add_handler(CmdHandler.cassFreightIndex())
            application.add_handler(CmdHandler.newHousing())    
            application.add_handler(CmdHandler.consumerCredit())  
            application.add_handler(CmdHandler.cpi_bra())   
            application.add_handler(CmdHandler.cpi_chn())         
            application.add_handler(CmdHandler.cpi_de())  
            application.add_handler(CmdHandler.cpi_inida())   
            application.add_handler(CmdHandler.cpi_jpn())  
            application.add_handler(CmdHandler.cpi_kr())   
              

            application.run_polling(timeout=3)