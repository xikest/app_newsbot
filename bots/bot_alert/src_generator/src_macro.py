from datetime import timedelta
from bots.bot_alert.src_generator.src_generator import SrcGenerator
from bots.bot_alert.src_generator.src_news import SrcNews
from tools.time.time import Timer
from tools.telegram_bot.contents import Context

# 반환 값은 모두 리스트 값 
from market.shiller_cape_ratio import ShillerRatio
from market.market_pattern import MarketPattern
from market.macro.cpi import CPI
from market.macro.pce import PCE
from market.macro.retail_sales import  ReatailSales
from market.macro.new_residential_sales import  NewResidentialSales
from market.macro.durable_goods import  DurableGoods
from market.macro.employment_cost_index import EmploymentCostIndex
from market.macro.gdp import GDP

class SrcMacro:
      class ShillerRatio:    
            @staticmethod
            def compareWithPrice():
                  yield Context(content = [ShillerRatio.plot('S&P 500 Real Price by Month'),
                                           ShillerRatio.plot('S&P 500 Dividend Yield by Month'),
                                           ShillerRatio.plot('S&P 500 Earnings Yield by Month'),
                                           ShillerRatio.plot('S&P 500 PE Ratio by Month')], dtype='img')
            
            
      class Market:
            @staticmethod
            def pattern():
                  yield Context(content = [MarketPattern.plot()], dtype='img')
            
      
      class EconomicIdx:
            @staticmethod
            def gen_nber_releases():
                  genContent = SrcNews.NBER.nber_economic_indicators_releases()
                  for context in genContent:
                        context:Context
                        context.content=[context.descr] ## 컨텐츠 업데이트
                        yield context
                  
      class Macro:
            @staticmethod
            def cpi():
                  yield Context(content = [CPI.headLine(),
                                            CPI.core(),
                                            CPI.ma3month(),
                                            CPI.ma3month(),
                                            CPI.ma3month(),
                                            CPI.medicalCare(),
                                            CPI.shelter(),
                                            CPI.rent()], dtype='img')
                  
            @staticmethod
            def reatailSales():
                  yield Context(content = [ReatailSales.advanceRetailSales(),
                                            ReatailSales.retailSales(),
                                            ReatailSales.advanceRetailSalesExcludingMotorVehicle(),
                                            ReatailSales.retailSalesExcludingMotorVehicle(),
                                            ReatailSales.advanceRetailSales_Gasoline(),
                                            ReatailSales.retailSales_Gasoline(),
                                            ReatailSales.advanceRetailSales_NonstoreRetailers(),
                                            ReatailSales.retailSales_NonstoreRetailers(),
                                            ReatailSales.advanceRetailSales_NonstoreRetailers(),
                                            ReatailSales.retailSales_NonstoreRetailers(),                                        
                                            ], dtype='img')

                    
            @staticmethod
            def newResidentialSales():
                  yield Context(content = [NewResidentialSales.housesSold(),
                                            NewResidentialSales.monthlySupply(),
                                            NewResidentialSales.medianSalesPriceforNewHousesSold(),
                                            NewResidentialSales.averageSalesPriceforNewHousesSold(),
                                            NewResidentialSales.newHousesSoldNotStarted(),
                                          ], dtype='img')

            @staticmethod
            def durableGoods():
                  yield Context(content = [DurableGoods.newOrder_durableGoods(),
                                            DurableGoods.newOrder_durableGoodsExcludingTransportation(),
                                            DurableGoods.newOrder_durableGoodsExcludingDefence(),
                                            DurableGoods.primaryMetals(),
                                            DurableGoods.capitalGoods(),
                                            DurableGoods.capitalGoodsExcludingDefence(),
                                            DurableGoods.UnfilledOrdersDurableGoods(),
                                          ], dtype='img')


            @staticmethod
            def pce():
                  yield Context(content = [PCE.personalIncome(),
                                            PCE.realDisposablePersonalIncome(),
                                            PCE.personaloutlays(),
                                            PCE.pce(),
                                            PCE.personalInterestPayments(),
                                            PCE.expenditures_durable(),
                                            PCE.real_pce(),
                                            PCE.pce_PriceIndex()], dtype='img')


            @staticmethod
            def employmentCostIndex():
                  yield Context(content = [EmploymentCostIndex.wages(),
                                            EmploymentCostIndex.productivity_nonfarm(),
                                          ], dtype='img')
                    
            @staticmethod
            def gdp():
                  yield Context(content = [GDP.gdp(),
                                            GDP.personalConsumptionExpenditures(),
                                            GDP.durableGoods(),
                                            GDP.non_durableGoods(),
                                            GDP.services(),
                                            GDP.domesticInvestment(),
                                            GDP.fixedInvestment(),
                                            GDP.changeInventories(),
                                            GDP.netExports(),
                                            GDP.governmentConsumptionExpenditures_GrossInvestment(),
                                          ], dtype='img')

    
              