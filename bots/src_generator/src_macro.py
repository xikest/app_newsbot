from datetime import timedelta

from .src_generator import SrcGenerator
from .src_news import SrcNews
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
from market.macro.cfnai import CFNAI
from market.macro.empire_state_manufacturing import EmpireStateManufacturingSurvey
from market.macro.existing_home_sales import ExistingHomeSales
from market.macro.industrial_production import IndustrialProduction
from market.macro.ism import ISM
from market.macro.productivity import Productivity







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
                                           Fed.fed_effective_rate(),
                                           Fed.m2v()
                                          ], dtype='img')
        
   
        
            @staticmethod
            def cpi():
                  yield from [Context(content = [CPI.descr()], dtype='msg'),
                              Context(content = [CPI.headLine()], dtype='img'),
                              Context(content = [CPI.core_descr()], dtype='msg'),
                              Context(content = [CPI.core()], dtype='img'),
                              Context(content = [CPI.ma_descr()], dtype='msg'),
                              Context(content = [CPI.ma3month(),
                                                CPI.ma6month(),
                                                CPI.ma12month()], dtype='img'),
                              Context(content = [CPI.medicalCare_descr()], dtype='msg'),
                              Context(content = [CPI.medicalCare(),
                                                CPI.shelter(),
                                                CPI.rent()], dtype='img')
                              ]
                  
                  
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
                  yield from  [Context(content = [DurableGoods.descr(),
                                                  DurableGoods.newOrder_durableGoods_descr()], dtype='msg'),
                              Context(content = [DurableGoods.newOrder_durableGoods()], dtype='img'),
                              Context(content = [DurableGoods.newOrder_durableGoodsExcludingTransportation_descr()], dtype='msg'),
                              Context(content = [DurableGoods.newOrder_durableGoodsExcludingTransportation()], dtype='img'),
                              
                              Context(content = [DurableGoods.newOrder_durableGoodsExcludingDefence_descr()], dtype='msg'),
                              Context(content = [DurableGoods.newOrder_durableGoodsExcludingDefence()], dtype='img'),
                              
                              Context(content = [DurableGoods.newOrder_excludingDefense_descr()], dtype='msg'),
                              Context(content = [DurableGoods.newOrder_excludingDefense()], dtype='img'),
                              
                              Context(content = [DurableGoods.primaryMetals_descr()], dtype='msg'),
                              Context(content = [DurableGoods.primaryMetals()], dtype='img'),           
                              
                              Context(content = [DurableGoods.capitalGoods_descr()], dtype='msg'),
                              Context(content = [DurableGoods.capitalGoods()], dtype='img'),           
                              
                              Context(content = [DurableGoods.capitalGoodsExcludingDefence_descr()], dtype='msg'),
                              Context(content = [DurableGoods.capitalGoodsExcludingDefence()], dtype='img'),   
                              
                              Context(content = [DurableGoods.unfilledOrdersDurableGoods_descr()], dtype='msg'),
                              Context(content = [DurableGoods.unfilledOrdersDurableGoods()], dtype='img')
                              ]


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
                  yield from  [Context(content = [EmploymentCostIndex.descr(), 
                                            EmploymentCostIndex.wages_descr()], dtype='msg'),
                              Context(content = [EmploymentCostIndex.wages(), 
                                                EmploymentCostIndex.wages_yearly(),
                                                EmploymentCostIndex.productivity_nonfarm()], dtype='img')
                              ]
                    
                    
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
                  yield from [Context(content = [AdpNationalEmploymentReport.descr()], dtype='msg'),
                              Context(content = [AdpNationalEmploymentReport.nonfarmPrivatePayrollEmployment()], dtype='img'),
                              Context(content = [AdpNationalEmploymentReport.nonfarmPrivateManufacturingPayrollEmployment_descr()], dtype='msg'),
                              Context(content = [AdpNationalEmploymentReport.nonfarmPrivateManufacturingPayrollEmployment()], dtype='img'),
                              Context(content = [AdpNationalEmploymentReport.nonfarmPrivateSmallPayrollEmployment_descr()], dtype='msg'), 
                              Context(content = [AdpNationalEmploymentReport.nonfarmPrivateSmallPayrollEmployment()], dtype='img'),   
                              Context(content = [AdpNationalEmploymentReport.nonfarmPrivateMediumPayrollEmployment_descr()], dtype='msg'),
                              Context(content = [AdpNationalEmploymentReport.nonfarmPrivateMediumPayrollEmployment(),
                                                 AdpNationalEmploymentReport.nonfarmPrivateLargePayrollEmployment()], dtype='img')]
                    
            @staticmethod
            def diffusionIndexphiladelphia():
                  
                  yield [Context(content = [DiffusionIndexphiladelphia.descr(),
                                            DiffusionIndexphiladelphia.currentGeneralActivity_descr()], dtype='msg'),
                        Context(content = [DiffusionIndexphiladelphia.currentGeneralActivity()], dtype='img'),
                        Context(content = [DiffusionIndexphiladelphia.futureEmployment_descr()], dtype='msg'),
                        Context(content = [DiffusionIndexphiladelphia.futureEmployment()], dtype='img'), 
                        Context(content = [DiffusionIndexphiladelphia.futureCapitalExpenditures_descr()], dtype='msg'),
                        Context(content = [DiffusionIndexphiladelphia.futureCapitalExpenditures()], dtype='img')]


                    
            @staticmethod
            def inventoriesSalesRatio():
                  yield from [Context(content = [InventoriesSalesRatio.descr(),
                                                 
                                                InventoriesSalesRatio.business_descr()], dtype='msg'),
                              Context(content = [InventoriesSalesRatio.totalBusiness()], dtype='img'),
                              Context(content = [InventoriesSalesRatio.saleInventory_descr(),
                                                InventoriesSalesRatio.retailers_descr()], dtype='msg'),
                              Context(content = [InventoriesSalesRatio.retailers()], dtype='img'),
                              
                              Context(content = [InventoriesSalesRatio.retailers_descr()], dtype='msg'), 
                              Context(content = [InventoriesSalesRatio.retailTradeExcludingVehicle(),
                                                InventoriesSalesRatio.motorVehicle(),
                                                InventoriesSalesRatio.furniture_home_furnishings(),
                                                InventoriesSalesRatio.buildingMaterials(),
                                                InventoriesSalesRatio.clothing(),
                                                InventoriesSalesRatio.food_beverage(),
                                                InventoriesSalesRatio.generalMrchandise(),
                                                InventoriesSalesRatio.department(),
                                                InventoriesSalesRatio.merchantWholesalers(),
                                                InventoriesSalesRatio.manufacturers(),], dtype='img'),  
                               
                              Context(content = [InventoriesSalesRatio.inventory_descr()], dtype='msg'),
                              Context(content = [InventoriesSalesRatio.businessInventories(),
                                                InventoriesSalesRatio.retailersInventories(),
                                                InventoriesSalesRatio.merchantWholesalersInventories(),
                                                InventoriesSalesRatio.manufacturersInventories()], dtype='img')]

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
                  
            @staticmethod
            def cfnai():
                  yield from [Context(content = [CFNAI.descr(), CFNAI.chicagoFedNationalActivityIndex_descr()], dtype='msg'),
                              Context(content = [CFNAI.chicagoFedNationalActivityIndex()], dtype='img')
                              ]

            @staticmethod
            def empireStateManufacturingSurvey():
                  yield Context(content = [EmpireStateManufacturingSurvey.descr(),
                                           EmpireStateManufacturingSurvey.report_descr(),
                                           EmpireStateManufacturingSurvey.report()], dtype='msg')
                  
            @staticmethod
            def existingHomeSales():
                  yield from  [Context(content = [ExistingHomeSales.descr(),
                                                  ExistingHomeSales.existingHomeSales_descr()], dtype='msg'),
                         
                              Context(content = [ExistingHomeSales.existingHomeSales(),
                                                ExistingHomeSales.housingInventory() ], dtype='img'),
                        
                              Context(content = [ExistingHomeSales.monthsSupply_descr()], dtype='msg'),
                              Context(content = [ExistingHomeSales.monthsSupply()], dtype='img'),
                              
                              Context(content = [ExistingHomeSales.medianSalesPrice_descr()], dtype='msg'),
                              Context(content = [ExistingHomeSales.medianSalesPrice()], dtype='img'),
                              
                              Context(content = [ExistingHomeSales.medHousingAffordabilityIndexianSalesPrice_descr()], dtype='msg'),
                              Context(content = [ExistingHomeSales.medHousingAffordabilityIndexianSalesPrice()], dtype='img'),
                              
                              Context(content = [ExistingHomeSales.pendingHomeSalesIndex()], dtype='msg')]




            @staticmethod
            def industrialProduction():
                  yield Context(content = [IndustrialProduction.industrialProduction(),
                                          IndustrialProduction.industrialProduction_ExcludingSelected(),
                                          IndustrialProduction.industrialProduction_ConsumerGoods(),
                                          IndustrialProduction.industrialProduction_BusinessEquipment(),
                                          IndustrialProduction.industrialProduction_Defense_Space_Equipment(),
                                          IndustrialProduction.industrialProduction_Manufacturing(),
                                          IndustrialProduction.industrialProduction_Motor_VehiclesParts(),
                                          IndustrialProduction.industrialProduction_Communications_Equipment(),
                                          IndustrialProduction.industrialProduction_Semiconductor(),
                                          IndustrialProduction.industrialProduction_Computer_Electronic(),
                                          IndustrialProduction.industrialProduction_ExcludingMotorVehicles(),
                                          IndustrialProduction.industrialProduction_ExcludingHi_Tech(),
                                          IndustrialProduction.capacityUtilization(),
                                          IndustrialProduction.capacityUtilization_Manufacturing(),
                                          IndustrialProduction.capacityUtilization_Manufacturing_hi_tech(),
                                          IndustrialProduction.capacityUtilization_Manufacturing_Computers(),
                                          IndustrialProduction.capacityUtilization_Manufacturing_Communications(),
                                          IndustrialProduction.capacityUtilization_Vehicles(),
                                          IndustrialProduction.capacityUtilization_PrimaryMetal()
                                          ], dtype='img')



            @staticmethod
            def ism():
                  yield Context(content = [ISM.ism_ReportOnBusiness(),
                                          ], dtype='msg')


            @staticmethod
            def productivity():
                  yield from [Context(content = [Productivity.laborProductivity(),
                                          Productivity.hourlyCompensation(),
                                          Productivity.unitLaborCosts(),
                                          Productivity.importPriceIndex(),
                                          Productivity.exportPriceIndex_AllCommodities(),
                                          Productivity.exportPriceIndex_NonagriculturalCommodities(),
                                          ], dtype='img'),
                              
                              Context(content = [Productivity.upward_usd(),
                                                 Productivity.downward_usd(),
                                                ], dtype='msg')
                              ]
                        


