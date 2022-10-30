from typing import Generator
import asyncio
from bots.bot_alert.src_generator.src_macro import SrcMacro
from bots.bot_alert.src_generator.src_stocks import SrcStocks

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)

# ================================================================================
# = 이벤트 작성
# ================================================================================

    
    
class CmdHandler:
        @staticmethod
        async   def _sentPhoto(update: Update, context: ContextTypes.DEFAULT_TYPE, genContent:Generator):
                    await   update.message.reply_text(text="잠시만 기다려 주세요.")
                    # update.message.reply_text(text="잠시만 기다려 주세요.")
                    for context_ex in genContent():
                        while len(context_ex.content) > 0: 
                            await asyncio.sleep(1)
                            await    update.message.reply_photo(photo=context_ex.content.pop(0))
                
# =================================================================================================================================
# stocks
# =================================================================================================================================
    
        # # stock reply function
        # @staticmethod
        # def bs_stock():
        #     def _bs_stock(update: Update, context: ContextTypes.DEFAULT_TYPE):
        #         symbol = update.message.text
        #         update.message.reply_text(symbol)
        #         CmdHandler._sentPhoto(update, context, SrcStocks.Stock_bs(symbol).ratio_incomes)
        #     return CommandHandler('bs_stock', _bs_stock)

        # stock reply function
        @staticmethod
        def bs_stock():
            async   def bs_stock_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
                await   update.message.reply_text("ticker를 입력해주세요. 종료하려면 'cancel'을 입력해주세요.")
                return 0
            async   def _bs_stock(update: Update, context: ContextTypes.DEFAULT_TYPE):
                symbol = update.message.text
                await   update.message.reply_text(symbol)
                await   CmdHandler._sentPhoto(update, context, SrcStocks.Stock_bs(symbol).ratio_incomes)
            async   def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
                await   update.message.reply_text(
                    'Bye! I hope we can talk again some day.', reply_markup=ReplyKeyboardRemove())
                return ConversationHandler.END

            # def _bs_stock(update: Update, context: ContextTypes.DEFAULT_TYPE):
            #     symbol = update.message.text
            #     update.message.reply_text(symbol)
            #     CmdHandler._sentPhoto(update, context, SrcStocks.Stock_bs(symbol).ratio_incomes)
            return ConversationHandler(entry_points=[CommandHandler('bs_stock', bs_stock_start)],
                                        states={ 0: [MessageHandler(filters.TEXT & ~filters.COMMAND, _bs_stock)],},
                                        fallbacks=[CommandHandler('cancel', cancel)])
                    
                    
       
       
        
# =================================================================================================================================
# Macro
# =================================================================================================================================
        # shri reply function
        @staticmethod
        def shillerRatio():
            async   def _shillerRatio(update: Update, context: ContextTypes.DEFAULT_TYPE):
                await   CmdHandler._sentPhoto(update, context, SrcMacro.ShillerRatio.compareWithPrice)
            return CommandHandler('shiller_ratio', _shillerRatio)

        # mkptn reply function
        @staticmethod
        def mkPtn():
            async   def _mkPtn(update: Update, context: ContextTypes.DEFAULT_TYPE):
                await   CmdHandler._sentPhoto(update, context, SrcMacro.Market.pattern)
            return CommandHandler('market_pattern', _mkPtn)
        
        # cpi reply function
        @staticmethod
        def cpi():
            async   def _cpi(update: Update, context: ContextTypes.DEFAULT_TYPE):
                await   CmdHandler._sentPhoto(update, context, SrcMacro.Macro.cpi)
            return CommandHandler('cpi', _cpi)
        
        # reatailSales reply function
        @staticmethod
        def reatailSales():
            async   def _reatailSales(update: Update, context: ContextTypes.DEFAULT_TYPE):
                await   CmdHandler._sentPhoto(update, context, SrcMacro.Macro.reatailSales)
            return CommandHandler('reatail_sales', _reatailSales)
        
        # newResidentialSales reply function
        @staticmethod
        def newResidentialSales():
            async   def _newResidentialSales(update: Update, context: ContextTypes.DEFAULT_TYPE):
                await   CmdHandler._sentPhoto(update, context, SrcMacro.Macro.newResidentialSales)
            return CommandHandler('new_residential_sales', _newResidentialSales)
        
        # durableGoods reply function
        @staticmethod
        def durableGoods():
            async   def _durableGoods(update: Update, context: ContextTypes.DEFAULT_TYPE):
                await   CmdHandler._sentPhoto(update, context, SrcMacro.Macro.durableGoods)
            return CommandHandler('durable_goods', _durableGoods)
        
        # def reply function
        @staticmethod
        def pce():
            async   def _pce(update: Update, context: ContextTypes.DEFAULT_TYPE):
                await   CmdHandler._sentPhoto(update, context, SrcMacro.Macro.pce)
            return CommandHandler('pce', _pce)

        # employmentCostIndex reply function
        @staticmethod
        def employmentCostIndex():
            async   def _employmentCostIndex(update: Update, context: ContextTypes.DEFAULT_TYPE):
                await   CmdHandler._sentPhoto(update, context, SrcMacro.Macro.employmentCostIndex)
            return CommandHandler('employment_cost_index', _employmentCostIndex)
        
        # gdp reply function
        @staticmethod
        def gdp():
            async   def _gdp(update: Update, context: ContextTypes.DEFAULT_TYPE):
                await   CmdHandler._sentPhoto(update, context, SrcMacro.Macro.gdp)
            return CommandHandler('gdp', _gdp)

