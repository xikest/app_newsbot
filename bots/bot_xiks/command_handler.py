from typing import Generator
import asyncio
from ..src_generator.src_macro import SrcMacro
from ..src_generator.src_stocks import SrcStocks
from tools.telegram_bot.contents import Context


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
        async   def _sentPhoto(update: Update, context: ContextTypes.DEFAULT_TYPE, genContents:Generator):
                    context_ex:Context
                    await   update.message.reply_text(text="잠시만 기다려 주세요.")
                    # update.message.reply_text(text="잠시만 기다려 주세요.")
                    
                    for context_ex in genContents():
                        while len(context_ex.content) > 0: 
                            await asyncio.sleep(1)
                            if context_ex.dtype == 'img': 
                                await    update.message.reply_photo(photo=context_ex.content.pop(0))
                            if context_ex.dtype == 'msg': 
                                await    update.message.reply_text(text=context_ex.content.pop(0))      
                
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
                await   update.message.reply_text(f'입력한 ticker는 {symbol} 입니다.')
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
# market
# =================================================================================================================================


		# shri reply function
        @staticmethod
        def shillerRatio():
            async   def _shillerRatio(update: Update, context: ContextTypes.DEFAULT_TYPE):
                await   CmdHandler._sentPhoto(update, context, SrcMacro.ShillerRatio.compareWithPrice)
            return CommandHandler('shiller_ratio', _shillerRatio)

        # mkptn reply function
        @staticmethod
        def mkPtn_w():
            async   def _mkPtn_w(update: Update, context: ContextTypes.DEFAULT_TYPE):
                await   CmdHandler._sentPhoto(update, context, SrcMacro.Market.pattern_w)
            return CommandHandler('market_pattern_w', _mkPtn_w)
        
        # mkptn reply function
        @staticmethod
        def mkPtn_m():
            async   def _mkPtn_m(update: Update, context: ContextTypes.DEFAULT_TYPE):
                await   CmdHandler._sentPhoto(update, context, SrcMacro.Market.pattern_m)
            return CommandHandler('market_pattern_m', _mkPtn_m)
        
# =================================================================================================================================
# Macro
# =================================================================================================================================

        # fed reply function
        @staticmethod
        def fed():
            async   def _fed(update: Update, context: ContextTypes.DEFAULT_TYPE):
                await   CmdHandler._sentPhoto(update, context, SrcMacro.Macro.fed)
            return CommandHandler('fed', _fed)
        
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

        # jolt reply function
        @staticmethod
        def jolt():
            async   def _jolt(update: Update, context: ContextTypes.DEFAULT_TYPE):
                await   CmdHandler._sentPhoto(update, context, SrcMacro.Macro.jolt)
            return CommandHandler('jolt', _jolt)

        # adp reply function
        @staticmethod
        def adpNationalEmploymentReport():
            async   def _adpNationalEmploymentReport(update: Update, context: ContextTypes.DEFAULT_TYPE):
                await   CmdHandler._sentPhoto(update, context, SrcMacro.Macro.adpNationalEmploymentReport)
            return CommandHandler('adp_employment_report', _adpNationalEmploymentReport)
        
        # DiffusionIndexphiladelphia reply function
        @staticmethod
        def diffusionIndexphiladelphia():
            async   def _diffusionIndexphiladelphia(update: Update, context: ContextTypes.DEFAULT_TYPE):
                await   CmdHandler._sentPhoto(update, context, SrcMacro.Macro.diffusionIndexphiladelphia)
            return CommandHandler('diffusion_index_philadelphia', _diffusionIndexphiladelphia)

        # inventoriesSalesRatio reply function
        @staticmethod
        def inventoriesSalesRatio():
            async   def _inventoriesSalesRatio(update: Update, context: ContextTypes.DEFAULT_TYPE):
                await   CmdHandler._sentPhoto(update, context, SrcMacro.Macro.inventoriesSalesRatio)
            return CommandHandler('inventories_sales_ratio', _inventoriesSalesRatio)   
        
        # PPI reply function
        @staticmethod
        def ppi():
            async   def _ppi(update: Update, context: ContextTypes.DEFAULT_TYPE):
                await   CmdHandler._sentPhoto(update, context, SrcMacro.Macro.ppi)
            return CommandHandler('ppi', _ppi)   

       
        # cfnai reply function
        @staticmethod
        def cfnai():
            async   def _cfnai(update: Update, context: ContextTypes.DEFAULT_TYPE):
                await   CmdHandler._sentPhoto(update, context, SrcMacro.Macro.cfnai)
            return CommandHandler('cfnai', _cfnai)   
       
        # empireStateManufacturingSurvey reply function
        @staticmethod
        def empireStateManufacturingSurvey():
            async   def _empireStateManufacturingSurvey(update: Update, context: ContextTypes.DEFAULT_TYPE):
                await   CmdHandler._sentPhoto(update, context, SrcMacro.Macro.empireStateManufacturingSurvey)
            return CommandHandler('empirestate_manufacturing', _empireStateManufacturingSurvey)   
       
        # existingHomeSales reply function
        @staticmethod
        def existingHomeSales():
            async   def _existingHomeSales(update: Update, context: ContextTypes.DEFAULT_TYPE):
                await   CmdHandler._sentPhoto(update, context, SrcMacro.Macro.existingHomeSales)
            return CommandHandler('existing_home_sales', _existingHomeSales) 
        
        # industrialProduction reply function
        @staticmethod
        def industrialProduction():
            async   def _industrialProduction(update: Update, context: ContextTypes.DEFAULT_TYPE):
                await   CmdHandler._sentPhoto(update, context, SrcMacro.Macro.industrialProduction)
            return CommandHandler('industrial_production_capacity', _industrialProduction)   
       
        # ISM reply function
        @staticmethod
        def ism():
            async   def _ism(update: Update, context: ContextTypes.DEFAULT_TYPE):
                await   CmdHandler._sentPhoto(update, context, SrcMacro.Macro.ism)
            return CommandHandler('ism', _ism)   
       
        # productivity reply function
        @staticmethod
        def productivity():
            async   def _productivity(update: Update, context: ContextTypes.DEFAULT_TYPE):
                await   CmdHandler._sentPhoto(update, context, SrcMacro.Macro.productivity)
            return CommandHandler('productivity', _productivity)   
        
        # InitialClaims reply function
        @staticmethod
        def initialClaims():
            async   def _initialClaims(update: Update, context: ContextTypes.DEFAULT_TYPE):
                await   CmdHandler._sentPhoto(update, context, SrcMacro.Macro.initialClaims)
            return CommandHandler('initial_claims', _initialClaims)  
        
        
        # E_COMMERCE reply function
        @staticmethod
        def ecommerce():
            async   def _ecommerce(update: Update, context: ContextTypes.DEFAULT_TYPE):
                await   CmdHandler._sentPhoto(update, context, SrcMacro.Macro.ecommerce)
            return CommandHandler('ecommerce', _ecommerce)  
        
        # ImportExport reply function
        @staticmethod
        def import_export():
            async   def _import_export(update: Update, context: ContextTypes.DEFAULT_TYPE):
                await   CmdHandler._sentPhoto(update, context, SrcMacro.Macro.import_export)
            return CommandHandler('import_export', _import_export)  
        
        # CassFreightIndex reply function
        @staticmethod
        def cassFreightIndex():
            async   def _cassFreightIndex(update: Update, context: ContextTypes.DEFAULT_TYPE):
                await   CmdHandler._sentPhoto(update, context, SrcMacro.Macro.cassFreightIndex)
            return CommandHandler('cass_freight_index', _cassFreightIndex)  
        
        