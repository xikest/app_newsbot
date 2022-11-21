from typing import Generator
import asyncio
import time
from ..src_generator.src_macro import SrcMacro
from ..src_generator.src_stocks import SrcStocks
from tools.telegram_bot.contents import Context


from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)

# ================================================================================
# = 이벤트 작성
# ================================================================================


    
class CmdHandler:
        @staticmethod
        def _sentPhoto(update: Update, context: CallbackContext, genContents:Generator):
            context_ex:Context
            update.message.reply_text(text="잠시만 기다려 주세요.")
            # update.message.reply_text(text="잠시만 기다려 주세요.")
            
            for context_ex in genContents():
                while len(context_ex.content) > 0: 
                    time.sleep(1)
                    if context_ex.dtype == 'img': 
                        update.message.reply_photo(photo=context_ex.content.pop(0))
                    if context_ex.dtype == 'msg': 
                        update.message.reply_text(text=context_ex.content.pop(0))      
        
# =================================================================================================================================
# stocks
# =================================================================================================================================
    
        # # stock reply function
        # @staticmethod
        # def bs_stock():
        #     def _bs_stock(update: Update, context: CallbackContext):
        #         symbol = update.message.text
        #         update.message.reply_text(symbol)
        #         CmdHandler._sentPhoto(update, context, SrcStocks.Stock_bs(symbol).ratio_incomes)
        #     return CommandHandler('bs_stock', _bs_stock)

        # stock reply function
        @staticmethod
        def bs_stock():
            def bs_stock_start(update: Update, context: CallbackContext) -> int:
                update.message.reply_text("ticker를 입력해주세요. 종료하려면 'cancel'을 입력해주세요.")
                return 0
            def _bs_stock(update: Update, context: CallbackContext):
                symbol = update.message.text
                update.message.reply_text(f'입력한 ticker는 {symbol} 입니다.')
                CmdHandler._sentPhoto(update, context, SrcStocks.Stock_bs(symbol).ratio_incomes)
                
            def cancel(update: Update, context: CallbackContext) -> int:
                update.message.reply_text(
                'Bye! I hope we can talk again some day.', reply_markup=ReplyKeyboardRemove())
                return   ConversationHandler.END

            # def _bs_stock(update: Update, context: CallbackContext):
            #     symbol = update.message.text
            #     update.message.reply_text(symbol)
            #     CmdHandler._sentPhoto(update, context, SrcStocks.Stock_bs(symbol).ratio_incomes)
            return   ConversationHandler(entry_points=[CommandHandler('bs_stock', bs_stock_start)],
                                        states={ 0: [MessageHandler(Filters.text & ~Filters.command, _bs_stock)],},
                                        fallbacks=[CommandHandler('cancel', cancel)])
                    
                    
       
  
# =================================================================================================================================
# market
# =================================================================================================================================


		# shri reply function
        @staticmethod
        def shillerRatio():
            def _shillerRatio(update: Update, context: CallbackContext):
                CmdHandler._sentPhoto(update, context, SrcMacro.ShillerRatio.compareWithPrice)
            return CommandHandler('shiller_ratio', _shillerRatio)

        # mkptn reply function
        @staticmethod
        def mkPtn_w():
            def _mkPtn_w(update: Update, context: CallbackContext):
                CmdHandler._sentPhoto(update, context, SrcMacro.Market.pattern_w)
            return CommandHandler('market_pattern_w', _mkPtn_w)
        
        # mkptn reply function
        @staticmethod
        def mkPtn_m():
            def _mkPtn_m(update: Update, context: CallbackContext):
                CmdHandler._sentPhoto(update, context, SrcMacro.Market.pattern_m)
            return CommandHandler('market_pattern_m', _mkPtn_m)
        
# =================================================================================================================================
# Macro
# =================================================================================================================================

        # fed reply function
        @staticmethod
        def fed():
            def _fed(update: Update, context: CallbackContext):
                CmdHandler._sentPhoto(update, context, SrcMacro.Macro.fed)
            return CommandHandler('fed', _fed)
        
        # cpi reply function
        @staticmethod
        def cpi():
            def _cpi(update: Update, context: CallbackContext):
                CmdHandler._sentPhoto(update, context, SrcMacro.Macro.cpi)
            return CommandHandler('cpi', _cpi)
        
        # reatailSales reply function
        @staticmethod
        def reatailSales():
            def _reatailSales(update: Update, context: CallbackContext):
                CmdHandler._sentPhoto(update, context, SrcMacro.Macro.reatailSales)
            return CommandHandler('reatail_sales', _reatailSales)
        
        # newResidentialSales reply function
        @staticmethod
        def newResidentialSales():
            def _newResidentialSales(update: Update, context: CallbackContext):
                CmdHandler._sentPhoto(update, context, SrcMacro.Macro.newResidentialSales)
            return CommandHandler('new_residential_sales', _newResidentialSales)
        
        # durableGoods reply function
        @staticmethod
        def durableGoods():
            def _durableGoods(update: Update, context: CallbackContext):
                CmdHandler._sentPhoto(update, context, SrcMacro.Macro.durableGoods)
            return CommandHandler('durable_goods', _durableGoods)
        
        # def reply function
        @staticmethod
        def pce():
            def _pce(update: Update, context: CallbackContext):
                CmdHandler._sentPhoto(update, context, SrcMacro.Macro.pce)
            return CommandHandler('pce', _pce)

        # employmentCostIndex reply function
        @staticmethod
        def employmentCostIndex():
            def _employmentCostIndex(update: Update, context: CallbackContext):
                CmdHandler._sentPhoto(update, context, SrcMacro.Macro.employmentCostIndex)
            return CommandHandler('employment_cost_index', _employmentCostIndex)
        
        # gdp reply function
        @staticmethod
        def gdp():
            def _gdp(update: Update, context: CallbackContext):
                CmdHandler._sentPhoto(update, context, SrcMacro.Macro.gdp)
            return CommandHandler('gdp', _gdp)

        # jolt reply function
        @staticmethod
        def jolt():
            def _jolt(update: Update, context: CallbackContext):
                CmdHandler._sentPhoto(update, context, SrcMacro.Macro.jolt)
            return CommandHandler('jolt', _jolt)

        # adp reply function
        @staticmethod
        def adpNationalEmploymentReport():
            def _adpNationalEmploymentReport(update: Update, context: CallbackContext):
                CmdHandler._sentPhoto(update, context, SrcMacro.Macro.adpNationalEmploymentReport)
            return CommandHandler('adp_employment_report', _adpNationalEmploymentReport)
        
        # DiffusionIndexphiladelphia reply function
        @staticmethod
        def diffusionIndexphiladelphia():
            def _diffusionIndexphiladelphia(update: Update, context: CallbackContext):
                CmdHandler._sentPhoto(update, context, SrcMacro.Macro.diffusionIndexphiladelphia)
            return CommandHandler('diffusion_index_philadelphia', _diffusionIndexphiladelphia)

        # inventoriesSalesRatio reply function
        @staticmethod
        def inventoriesSalesRatio():
            def _inventoriesSalesRatio(update: Update, context: CallbackContext):
                CmdHandler._sentPhoto(update, context, SrcMacro.Macro.inventoriesSalesRatio)
            return CommandHandler('inventories_sales_ratio', _inventoriesSalesRatio)   
        
        # PPI reply function
        @staticmethod
        def ppi():
            def _ppi(update: Update, context: CallbackContext):
                CmdHandler._sentPhoto(update, context, SrcMacro.Macro.ppi)
            return CommandHandler('ppi', _ppi)   

       
        # cfnai reply function
        @staticmethod
        def cfnai():
            def _cfnai(update: Update, context: CallbackContext):
                CmdHandler._sentPhoto(update, context, SrcMacro.Macro.cfnai)
            return CommandHandler('cfnai', _cfnai)   
       
        # empireStateManufacturingSurvey reply function
        @staticmethod
        def empireStateManufacturingSurvey():
            def _empireStateManufacturingSurvey(update: Update, context: CallbackContext):
                CmdHandler._sentPhoto(update, context, SrcMacro.Macro.empireStateManufacturingSurvey)
            return CommandHandler('empirestate_manufacturing', _empireStateManufacturingSurvey)   
       
        # existingHomeSales reply function
        @staticmethod
        def existingHomeSales():
            def _existingHomeSales(update: Update, context: CallbackContext):
                CmdHandler._sentPhoto(update, context, SrcMacro.Macro.existingHomeSales)
            return CommandHandler('existing_home_sales', _existingHomeSales) 
        
        # industrialProduction reply function
        @staticmethod
        def industrialProduction():
            def _industrialProduction(update: Update, context: CallbackContext):
                CmdHandler._sentPhoto(update, context, SrcMacro.Macro.industrialProduction)
            return CommandHandler('industrial_production_capacity', _industrialProduction)   
       
        # ISM reply function
        @staticmethod
        def ism():
            def _ism(update: Update, context: CallbackContext):
                CmdHandler._sentPhoto(update, context, SrcMacro.Macro.ism)
            return CommandHandler('ism', _ism)   
       
        # productivity reply function
        @staticmethod
        def productivity():
            def _productivity(update: Update, context: CallbackContext):
                CmdHandler._sentPhoto(update, context, SrcMacro.Macro.productivity)
            return CommandHandler('productivity', _productivity)   
        
        # InitialClaims reply function
        @staticmethod
        def initialClaims():
            def _initialClaims(update: Update, context: CallbackContext):
                CmdHandler._sentPhoto(update, context, SrcMacro.Macro.initialClaims)
            return CommandHandler('initial_claims', _initialClaims)  
        
        
        # E_COMMERCE reply function
        @staticmethod
        def ecommerce_retailes():
            def _ecommerce(update: Update, context: CallbackContext):
                CmdHandler._sentPhoto(update, context, SrcMacro.Macro.ecommerce_retails)
            return CommandHandler('ecommerce', _ecommerce)  
        
        # ImportExport reply function
        @staticmethod
        def import_export():
            def _import_export(update: Update, context: CallbackContext):
                CmdHandler._sentPhoto(update, context, SrcMacro.Macro.import_export)
            return CommandHandler('import_export', _import_export)  
        
        # CassFreightIndex reply function
        @staticmethod
        def cassFreightIndex():
            def _cassFreightIndex(update: Update, context: CallbackContext):
                CmdHandler._sentPhoto(update, context, SrcMacro.Macro.cassFreightIndex)
            return CommandHandler('cass_freight_index', _cassFreightIndex)  
        
        # NewHousing reply function
        @staticmethod
        def newHousing():
            def _newHousing(update: Update, context: CallbackContext):
                CmdHandler._sentPhoto(update, context, SrcMacro.Macro.newHousing)
            return CommandHandler('new_housing', _newHousing)  
        
        # ConsumerCredit reply function
        @staticmethod
        def consumerCredit():
            def _consumerCredit(update: Update, context: CallbackContext):
                CmdHandler._sentPhoto(update, context, SrcMacro.Macro.consumerCredit)
            return CommandHandler('consumer_credit', _consumerCredit)  
        
        # CPI_BRA reply function
        @staticmethod
        def cpi_bra():
            def _cpi_bra(update: Update, context: CallbackContext):
                CmdHandler._sentPhoto(update, context, SrcMacro.Macro.cpi_bra)
            return CommandHandler('cpi_bra', _cpi_bra)  
        
        # CPI_CHN reply function
        @staticmethod
        def cpi_chn():
            def _cpi_chn(update: Update, context: CallbackContext):
                CmdHandler._sentPhoto(update, context, SrcMacro.Macro.cpi_chn)
            return CommandHandler('cpi_chn', _cpi_chn)  
        
        # CPI_DE reply function
        @staticmethod
        def cpi_de():
            def _cpi_de(update: Update, context: CallbackContext):
                CmdHandler._sentPhoto(update, context, SrcMacro.Macro.cpi_de)
            return CommandHandler('cpi_de', _cpi_de)  
        
        # CPI_INDIA reply function
        @staticmethod
        def cpi_inida():
            def _cpi_inida(update: Update, context: CallbackContext):
                CmdHandler._sentPhoto(update, context, SrcMacro.Macro.cpi_inida)
            return CommandHandler('cpi_inida', _cpi_inida)  
        
        # CPI_JPN reply function
        @staticmethod
        def cpi_jpn():
            def _cpi_jpn(update: Update, context: CallbackContext):
                CmdHandler._sentPhoto(update, context, SrcMacro.Macro.cpi_jpn)
            return CommandHandler('cpi_jpn', _cpi_jpn)  
        
        # CPI_KR reply function
        @staticmethod
        def cpi_kr():
            def _cpi_kr(update: Update, context: CallbackContext):
                CmdHandler._sentPhoto(update, context, SrcMacro.Macro.cpi_kr)
            return CommandHandler('cpi_kr', _cpi_kr)  