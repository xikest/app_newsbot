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
from market.macro.jolt import Jolt
from market.macro.adp_employment_report import AdpNationalEmploymentReport
from market.macro.diffusion_Index_philadelphia import DiffusionIndexphiladelphia
from market.macro.busines_inventories import InventoriesSalesRatio
from market.macro.fed import Fed
from market.macro.ppi import PPI

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
            def pattern_w():
                  yield Context(content = [MarketPattern.plot(period='w')], dtype='img')
                    
            @staticmethod
            def pattern_m():
                  yield Context(content = [MarketPattern.plot(period='m')], dtype='img')
            
      
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
            def fed():
                  yield Context(content = [Fed.totalAssets(),
                                           Fed.fed_effective_rate()
                                          ], dtype='img')
        
   
        
            @staticmethod
            def cpi():
                  yield Context(content = [CPI.headLine(),
                                            CPI.core(),
                                            CPI.ma3month(),
                                            CPI.ma6month(),
                                            CPI.ma12month(),
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
                                            ReatailSales.advanceRetailSales_food_drinking(),
                                            ReatailSales.retailSales_food_drinking(),                                        
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
                    
            @staticmethod
            def jolt():
                  yield Context(content = [Jolt.jobOpenings_Nonfarm(),
                                            Jolt.jobOpenings_Private(),
                                            Jolt.jobOpenings_Government(),
                                            Jolt.hires_Nonfarm(),
                                            Jolt.hires_Private(),
                                            Jolt.hires_Government(),
                                            Jolt.separations_Nonfarm(),
                                            Jolt.separations_Private(),
                                            Jolt.separations_Government(),
                                            Jolt.quits_Nonfarm(),
                                            Jolt.quits_Private(),
                                            Jolt.quits_Government(),
                                          ], dtype='img')
                    
            @staticmethod
            def adpNationalEmploymentReport():
                  yield Context(content = [AdpNationalEmploymentReport.nonfarmPrivatePayrollEmployment(),
                                            AdpNationalEmploymentReport.nonfarmPrivateManufacturingPayrollEmployment(),
                                            AdpNationalEmploymentReport.nonfarmPrivateSmallPayrollEmployment(),
                                            AdpNationalEmploymentReport.nonfarmPrivateMediumPayrollEmployment(),
                                            AdpNationalEmploymentReport.nonfarmPrivateLargePayrollEmployment(),
                                          ], dtype='img')

                    
                    
            @staticmethod
            def diffusionIndexphiladelphia():
                  yield Context(content = [DiffusionIndexphiladelphia.currentGeneralActivity(),
                                            DiffusionIndexphiladelphia.futureEmployment(),
                                            DiffusionIndexphiladelphia.futureCapitalExpenditures(),
                                          ], dtype='img')

                    
            @staticmethod
            def inventoriesSalesRatio():
                  yield Context(content = [InventoriesSalesRatio.totalBusiness(),
                                            InventoriesSalesRatio.retailers(),
                                            InventoriesSalesRatio.retailTradeExcludingVehicle(),
                                            InventoriesSalesRatio.motorVehicle(),
                                            InventoriesSalesRatio.furniture_home_furnishings(),
                                            InventoriesSalesRatio.buildingMaterials(),
                                            InventoriesSalesRatio.clothing(),
                                            InventoriesSalesRatio.food_beverage(),
                                            InventoriesSalesRatio.generalMrchandise(),
                                            InventoriesSalesRatio.department(),
                                            InventoriesSalesRatio.merchantWholesalers(),
                                            InventoriesSalesRatio.manufacturers(),
                                            InventoriesSalesRatio.businessInventories(),
                                            InventoriesSalesRatio.retailersInventories(),
                                            InventoriesSalesRatio.merchantWholesalersInventories(),
                                            InventoriesSalesRatio.manufacturersInventories(),

                                          ], dtype='img')
            @staticmethod
            def ppi():
                  yield Context(content = [PPI.finalDemand(),
                                            PPI.finalDemand_yoy(),
                                            PPI.finalDemand_less_foods_energy(),
                                            PPI.finalDemand_less_foods_energy_yoy(),
                                            PPI.processed_goods_Intermediate_yoy(),
                                            PPI.processed_goods_Intermediate_core(),
                                            PPI.unprocessed_goods_Intermediate_yoy(),
                                            PPI.unprocessed_goods_Intermediate_core(),
                                          ], dtype='img')
