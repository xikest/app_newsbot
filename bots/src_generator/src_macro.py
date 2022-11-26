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
from market.macro.e_commerce_retail_sales import E_COMMERCE
from market.macro.import_export import ImportExport
from market.macro.cass_freight_index import CassFreightIndex
from market.macro.new_housing import NewHousing
from market.macro.consumer_credit import ConsumerCredit
from market.macro.initial_claims import InitialClaims
from market.macro.cpi_bra import CPI_BRA
from market.macro.cpi_chn import CPI_CHN
from market.macro.cpi_de import CPI_DE
from market.macro.cpi_india import CPI_INDIA
from market.macro.cpi_jpn import CPI_JPN
from market.macro.cpi_kr import CPI_KR


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
                  yield Context(content = [MarketPattern.plot(period='m'), MarketPattern.plot(period='w')], dtype='img')
                
            
      
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
                  yield from  [Context(content = [ReatailSales.descr()], dtype='msg'),
                              Context(content = [ReatailSales.advanceRetailSales()], dtype='img'),
                              
                              Context(content = [ReatailSales.retailSales_descr()], dtype='msg'),
                              Context(content = [ReatailSales.retailSales()], dtype='img'),
                              
                              Context(content = [ReatailSales.advanceRetailSalesExcludingMotorVehicle_descr()], dtype='msg'),
                              Context(content = [ReatailSales.advanceRetailSalesExcludingMotorVehicle()], dtype='img'),
                              Context(content = [ReatailSales.retailSalesExcludingMotorVehicle()], dtype='img'),
                              
                              Context(content = [ReatailSales.advanceRetailSales_Gasoline_descr()], dtype='msg'),
                              Context(content = [ReatailSales.advanceRetailSales_Gasoline()], dtype='img'),
                              Context(content = [ReatailSales.retailSales_Gasoline()], dtype='img'),

                              Context(content = [ReatailSales.advanceRetailSales_NonstoreRetailers()], dtype='img'),
                              Context(content = [ReatailSales.retailSales_NonstoreRetailers_descr()], dtype='msg'),
                              Context(content = [ReatailSales.retailSales_NonstoreRetailers()], dtype='img'),
                              
                              Context(content = [ReatailSales.advanceRetailSales_food_drinking()], dtype='img'),
                              Context(content = [ReatailSales.retailSales_food_drinking_descr()], dtype='msg'),
                              Context(content = [ReatailSales.retailSales_food_drinking()], dtype='img')
                  ]


                    
            @staticmethod
            def newResidentialSales():
                  yield from  [Context(content = [NewResidentialSales.descr()], dtype='msg'),
                               
                              Context(content = [NewResidentialSales.housesSold_descr()], dtype='msg'),
                              Context(content = [NewResidentialSales.housesSold()], dtype='img'),
                              
                              Context(content = [NewResidentialSales.monthlySupply_descr()], dtype='msg'),
                              Context(content = [NewResidentialSales.monthlySupply()], dtype='img'),
                              
                              Context(content = [NewResidentialSales.medianSalesPriceforNewHousesSold_descr()], dtype='msg'),
                              Context(content = [NewResidentialSales.medianSalesPriceforNewHousesSold()], dtype='img'),
                              Context(content = [NewResidentialSales.averageSalesPriceforNewHousesSold()], dtype='img'),
 
                              Context(content = [NewResidentialSales.newHousesSoldNotStarted_descr()], dtype='msg'),
                              Context(content = [NewResidentialSales.newHousesSoldNotStarted()], dtype='img')
                              ]


            @staticmethod
            def durableGoods():
                  yield from  [Context(content = [DurableGoods.descr()], dtype='msg'),
                               
                              Context(content = [DurableGoods.newOrder_durableGoods_descr()], dtype='msg'),
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
                 yield from  [Context(content = [PCE.descr()], dtype='msg'),
                              
                              Context(content = [PCE.personalIncome_descr()], dtype='msg'),
                              Context(content = [PCE.personalIncome()], dtype='img'),
                              
                              Context(content = [PCE.realDisposablePersonalIncome_descr()], dtype='msg'),
                              Context(content = [PCE.realDisposablePersonalIncome()], dtype='img'),
                              
                              Context(content = [PCE.personaloutlays_descr()], dtype='msg'),
                              Context(content = [PCE.personaloutlays()], dtype='img'),

                              Context(content = [PCE.pce_descr()], dtype='msg'),
                              Context(content = [PCE.pce()], dtype='img'),
                              
                              Context(content = [PCE.personalInterestPayments_descr()], dtype='msg'),
                              Context(content = [PCE.personalInterestPayments()], dtype='img'),

                              Context(content = [PCE.personalInterestPayments_disposablePersonalIncome_descr()], dtype='msg'),
                              Context(content = [PCE.personalInterestPayments_disposablePersonalIncome()], dtype='img'),

                              Context(content = [PCE.expenditures_durable_descr()], dtype='msg'),
                              Context(content = [PCE.expenditures_durable()], dtype='img'),

                              Context(content = [PCE.real_pce_descr()], dtype='msg'),
                              Context(content = [PCE.real_pce()], dtype='img'),
                              
                              Context(content = [PCE.pce_PriceIndex()], dtype='img'),

                              Context(content = [PCE.pce_PriceIndex_yearly_descr()], dtype='msg'),
                              Context(content = [PCE.pce_PriceIndex_yearly()], dtype='img')
                              ]


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
                  yield from  [Context(content = [GDP.descr()], dtype='msg'),
                              
                              Context(content = [GDP.gdp_descr()], dtype='msg'),
                              Context(content = [GDP.gdp()], dtype='img'),
                              
                              Context(content = [GDP.pce_descr()], dtype='msg'),
                              Context(content = [GDP.pce()], dtype='img'),
                              
                              Context(content = [GDP.durableGoods_descr()], dtype='msg'),
                              Context(content = [GDP.durableGoods()], dtype='img'),
                    
                              Context(content = [GDP.services_descr()], dtype='msg'),
                              Context(content = [GDP.services()], dtype='img'),
                              
                              Context(content = [GDP.domesticInvestment_descr()], dtype='msg'),
                              Context(content = [GDP.domesticInvestment()], dtype='img'),
                              
                              Context(content = [GDP.fixedInvestment_descr()], dtype='msg'),
                              Context(content = [GDP.fixedInvestment()], dtype='img'),
                    
                              Context(content = [GDP.changeInventories_descr()], dtype='msg'),
                              Context(content = [GDP.changeInventories()], dtype='img'),
                              
                              Context(content = [GDP.netExports_descr()], dtype='msg'),
                              Context(content = [GDP.netExports()], dtype='img'),
                              
                              Context(content = [GDP.governmentConsumptionExpenditures_GrossInvestment_descr()], dtype='msg'),
                              Context(content = [GDP.governmentConsumptionExpenditures_GrossInvestment()], dtype='img'),
                    
                              Context(content = [GDP.finalSalesofDomesticProduct_descr()], dtype='msg'),
                              Context(content = [GDP.finalSalesofDomesticProduct()], dtype='img'),
                              
                              Context(content = [GDP.grossDomesticPurchases_descr()], dtype='msg'),
                              Context(content = [GDP.grossDomesticPurchases()], dtype='img'),
                              
                              Context(content = [GDP.gDPImplicitPriceDeflator_descr()], dtype='msg'),
                              Context(content = [GDP.gDPImplicitPriceDeflator()], dtype='img'),
                              
                              Context(content = [GDP.gNPImplicitPriceDeflator_descr()], dtype='msg'),
                              Context(content = [GDP.gNPImplicitPriceDeflator()], dtype='img'),
                              
                              Context(content = [GDP.pCeDeflator_descr()], dtype='msg'),
                              Context(content = [GDP.pCeDeflator()], dtype='img'),
                              
                              Context(content = [GDP.realGrossDomesticProduct_descr()], dtype='msg'),
                              Context(content = [GDP.realGrossDomesticProduct()], dtype='img'),  
                              
                              Context(content = [GDP.realNetExportsofGoodsandServices_descr()], dtype='msg'),
                              Context(content = [GDP.realNetExportsofGoodsandServices()], dtype='img'),
                              
                              Context(content = [GDP.realFinalSalestoPrivateDomesticPurchasers_descr()], dtype='msg'),
                              Context(content = [GDP.realFinalSalestoPrivateDomesticPurchasers()], dtype='img'),
                              
                              Context(content = [GDP.rGDPdivRealFinalSales_descr()], dtype='msg'),
                              Context(content = [GDP.rGDPdivRealFinalSales()], dtype='img'),  
                              
                              Context(content = [GDP.gDPdivGNP_descr()], dtype='msg'),
                              Context(content = [GDP.gDPdivGNP()], dtype='img'),
                              
                              Context(content = [GDP.realGDP_Computers_descr()], dtype='msg'),
                              Context(content = [GDP.realGDP_Computers()], dtype='img'),
                              
                              Context(content = [GDP.realGDP_Vehicle_descr()], dtype='msg'),
                              Context(content = [GDP.realGDP_Vehicle()], dtype='img'),                          
                              
                              Context(content = [GDP.rPCE_excludingfood_energy_descr()], dtype='msg'),
                              Context(content = [GDP.rPCE_excludingfood_energy()], dtype='img')
                              ]
                                         
                    
            @staticmethod
            def import_export():
                  yield from  [Context(content = [ImportExport.descr()], dtype='msg'),
                              Context(content = [ImportExport.importPriceIndex()], dtype='img'),
                              Context(content = [ImportExport.importPriceIndex_excludeFuel()], dtype='img'),
                              
                              Context(content = [ImportExport.exportPriceIndex_descr()], dtype='msg'),
                              Context(content = [ImportExport.exportPriceIndex()], dtype='img'),
                              
                              Context(content = [ImportExport.exportPriceIndex_nonagricultural()], dtype='msg'),
                              Context(content = [ImportExport.importPriceIndex_nonmanufacturing()], dtype='img'),
                              Context(content = [ImportExport.importPriceIndex_oil_gas()], dtype='img'),
                              Context(content = [ImportExport.exportPriceIndex_nonmanufacturing()], dtype='img'),
                              Context(content = [ImportExport.exportPriceIndex_oil_gas()], dtype='img'),
                              Context(content = [ImportExport.downward_usd_descr()], dtype='msg'),
                              Context(content = [ImportExport.upward_usd_descr()], dtype='msg')]
                              
                              
                              
            @staticmethod
            def jolt():
                  yield from [Context(content = [Jolt.descr()], dtype='msg'),
                              Context(content = [Jolt.jobOpenings_Nonfarm(),
                                                Jolt.jobOpenings_Private(),
                                                Jolt.jobOpenings_Government(),
                                                Jolt.hires_Nonfarm(),
                                                Jolt.hires_Private(),
                                                Jolt.hires_Government(),
                                                Jolt.separations_Nonfarm(),
                                                Jolt.separations_Private(),
                                                Jolt.separations_Government()], dtype='img'),
                              Context(content = [Jolt.quits_Nonfarm_descr()], dtype='msg'),
                              Context(content = [Jolt.quits_Nonfarm(),
                                                Jolt.quits_Private(),
                                                Jolt.quits_Government()], dtype='img')
                              ]
                    
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
                  
                  yield from  [Context(content = [DiffusionIndexphiladelphia.descr(),
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
                  yield from [Context(content = [PPI.descr()], dtype='msg'),
                              Context(content = [PPI.finalDemand(),
                                                PPI.finalDemand_yoy(),
                                                PPI.finalDemand_less_foods_energy(),
                                                PPI.finalDemand_less_foods_energy_yoy(),
                                                PPI.processed_goods_Intermediate_yoy(),
                                                PPI.processed_goods_Intermediate_core(),
                                                PPI.unprocessed_goods_Intermediate_yoy(),
                                                PPI.unprocessed_goods_Intermediate_core(),
                                                ], dtype='img')  
                              ]


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


            def industrialProduction():
                  yield from  [Context(content = [IndustrialProduction.descr()], dtype='msg'),
                               
                              Context(content = [IndustrialProduction.industrialProduction_descr()], dtype='msg'),
                              Context(content = [IndustrialProduction.industrialProduction()], dtype='img'),
                              
                              Context(content = [IndustrialProduction.industrialProduction_ExcludingSelected()], dtype='img'),
                        
                              Context(content = [IndustrialProduction.industrialProduction_ConsumerGoods_descr()], dtype='msg'),
                              Context(content = [IndustrialProduction.industrialProduction_ConsumerGoods()], dtype='img'),
                              
                              Context(content = [IndustrialProduction.industrialProduction_BusinessEquipment_descr()], dtype='msg'),
                              Context(content = [IndustrialProduction.industrialProduction_BusinessEquipment()], dtype='img'),
                              
                              Context(content = [IndustrialProduction.industrialProduction_Defense_Space_Equipment_descr()], dtype='msg'),
                              Context(content = [IndustrialProduction.industrialProduction_Defense_Space_Equipment()], dtype='img'),
                              
                              Context(content = [IndustrialProduction.industrialProduction_Manufacturing_descr()], dtype='msg'),
                              Context(content = [IndustrialProduction.industrialProduction_Manufacturing()], dtype='img'),
 
                              Context(content = [IndustrialProduction.industrialProduction_Motor_VehiclesParts_descr()], dtype='msg'),
                              Context(content = [IndustrialProduction.industrialProduction_Motor_VehiclesParts()], dtype='img'),
                              Context(content = [IndustrialProduction.industrialProduction_Communications_Equipment()], dtype='img'),
                              Context(content = [IndustrialProduction.industrialProduction_Semiconductor()], dtype='img'),

                              Context(content = [IndustrialProduction.industrialProduction_Computer_Electronic_descr()], dtype='msg'),
                              Context(content = [IndustrialProduction.industrialProduction_Computer_Electronic()], dtype='img'),
                              
                              Context(content = [IndustrialProduction.industrialProduction_ExcludingMotorVehicles_descr()], dtype='msg'),
                              Context(content = [IndustrialProduction.industrialProduction_ExcludingMotorVehicles()], dtype='img'),
                              Context(content = [IndustrialProduction.industrialProduction_ExcludingHi_Tech()], dtype='img'),
                              
                              Context(content = [IndustrialProduction.capacityUtilization_descr()], dtype='msg'),
                              Context(content = [IndustrialProduction.capacityUtilization()], dtype='img'),                           
                              Context(content = [IndustrialProduction.capacityUtilization_Manufacturing()], dtype='img'),
                              Context(content = [IndustrialProduction.capacityUtilization_Manufacturing_hi_tech()], dtype='img'),                           
                              Context(content = [IndustrialProduction.capacityUtilization_Manufacturing_Computers()], dtype='img'),
                              Context(content = [IndustrialProduction.capacityUtilization_Manufacturing_Communications()], dtype='img'),                           
                              Context(content = [IndustrialProduction.capacityUtilization_Vehicles()], dtype='img'),
                              Context(content = [IndustrialProduction.capacityUtilization_PrimaryMetal()], dtype='img')]
                              
            def cassFreightIndex():
                  yield from  [Context(content = [CassFreightIndex.descr()], dtype='msg'),
                              Context(content = [CassFreightIndex.report_url()], dtype='msg'),
                              
                              Context(content = [CassFreightIndex.cassFreightIndex_descr()], dtype='msg'),
                              Context(content = [CassFreightIndex.cassFreightIndex()], dtype='img'),
                              
                              Context(content = [CassFreightIndex.cassFreightIndex_expenditures_descr()], dtype='msg'),
                              Context(content = [CassFreightIndex.cassFreightIndex_expenditures()], dtype='img')]
                              
            def initialClaims():
                  yield from  [Context(content = [InitialClaims.descr()], dtype='msg'),
                              
                              Context(content = [InitialClaims.initialClaims_4WeekMA()], dtype='img'),
                              Context(content = [InitialClaims.insuredUnemployment_4WeekMA()], dtype='img'),
                              
                              Context(content = [InitialClaims.insuredUnemploymentRate_descr()], dtype='msg'),
                              Context(content = [InitialClaims.insuredUnemploymentRate()], dtype='img')]
                              
            def ecommerce_retails():
                  yield from  [Context(content = [E_COMMERCE.descr()], dtype='msg'),                              
                              Context(content = [E_COMMERCE.e_CommerceRetailSales()], dtype='img')]



            @staticmethod
            def ism():
                  yield from  [Context(content = [ISM.service_descr()], dtype='msg'),                              
                              Context(content = [ISM.manufactoring0_descr()], dtype='msg'),  
                              Context(content = [ISM.manufactoring1_descr()], dtype='msg'), 
                              Context(content = [ISM.ism_ReportOnBusiness()], dtype='msg')]



            @staticmethod
            def productivity():
                  yield from [Context(content = [Productivity.descr()], dtype='msg'),
                              
                              Context(content = [Productivity.laborProductivity_descr()], dtype='msg'),
                              Context(content = [Productivity.laborProductivity()], dtype='img'),
                          
                              Context(content = [Productivity.hourlyCompensation_descr()], dtype='msg'),
                              Context(content = [Productivity.hourlyCompensation()], dtype='img'),
                              
                              Context(content = [Productivity.unitLaborCosts()], dtype='img'),
                              Context(content = [Productivity.importPriceIndex()], dtype='img'),
                              Context(content = [Productivity.exportPriceIndex_AllCommodities()], dtype='img'),
                              Context(content = [Productivity.exportPriceIndex_NonagriculturalCommodities()], dtype='img'),

                              Context(content = [Productivity.upward_usd_descr()], dtype='msg'),
                              Context(content = [Productivity.downward_usd_descr()], dtype='msg')
                              ]
                        

            @staticmethod
            def newHousing():
                  yield from [Context(content = [NewHousing.descr()], dtype='msg'),
                              Context(content = [NewHousing.report_url()], dtype='msg'),
                              
                              Context(content = [NewHousing.newHousing_total_descr()], dtype='msg'),
                              Context(content = [NewHousing.newHousing_total()], dtype='img'),
                          
                              Context(content = [NewHousing.newHousing_single_descr()], dtype='msg'),
                              Context(content = [NewHousing.newHousing_single()], dtype='img'),
                              
                              Context(content = [NewHousing.newHousing_total_permit_descr()], dtype='msg'),
                              Context(content = [NewHousing.newHousing_total_permit()], dtype='img'),
                              Context(content = [NewHousing.newHousing_single_permit()], dtype='img'),
                              
                              Context(content = [NewHousing.newHousing_total_notStarted_descr()], dtype='msg'),
                              Context(content = [NewHousing.newHousing_total_notStarted()], dtype='img'),
                              Context(content = [NewHousing.newHousing_single_notStarted()], dtype='img'),
                              
                              Context(content = [NewHousing.newHousing_total_underConstruction()], dtype='img'),
                              Context(content = [NewHousing.newHousing_single_underConstruction()], dtype='img'),


                              Context(content = [NewHousing.newHousing_total_completed_descr()], dtype='msg'),
                              Context(content = [NewHousing.newHousing_total_completed()], dtype='img'),
                              Context(content = [NewHousing.newHousing_single_completed()], dtype='img')
                              ]
                        
            @staticmethod
            def consumerCredit():
                  yield from [Context(content = [ConsumerCredit.descr()], dtype='msg'),
                              Context(content = [ConsumerCredit.report_url()], dtype='msg'),
                              
                              Context(content = [ConsumerCredit.total_consumer_credit()], dtype='img'),
                              
                              Context(content = [ConsumerCredit.revolvingConsumerCreditOwnedSecuritized_descr()], dtype='msg'),
                              Context(content = [ConsumerCredit.revolvingConsumerCreditOwnedSecuritized()], dtype='img'),
                              
                              Context(content = [ConsumerCredit.non_revolvingConsumerCreditOwnedSecuritized_descr()], dtype='msg'),
                              Context(content = [ConsumerCredit.non_revolvingConsumerCreditOwnedSecuritized()], dtype='img'),
                          
                              Context(content = [ConsumerCredit.percentChangeTotalConsumerCredit_descr()], dtype='msg'),
                              Context(content = [ConsumerCredit.percentChangeTotalConsumerCredit()], dtype='img'),
                          
                              Context(content = [ConsumerCredit.commercialInterestRate_CreditCardPlans_descr()], dtype='msg'),
                              Context(content = [ConsumerCredit.commercialInterestRate_CreditCardPlans()], dtype='img')
                              ]
                          
            @staticmethod
            def cpi_bra():
                  yield from [Context(content = [CPI_BRA.production_industry_exc_construction()], dtype='img'),
                              Context(content = [CPI_BRA.cpi()], dtype='img')]

            @staticmethod
            def cpi_chn():
                  yield from [Context(content = [CPI_CHN.production_industry_exc_construction()], dtype='img'),
                              Context(content = [CPI_CHN.cpi()], dtype='img')]

            @staticmethod
            def cpi_de():
                  yield from [Context(content = [CPI_DE.production_industry_exc_construction()], dtype='msg'),
                              Context(content = [CPI_DE.production_industry_exc_construction()], dtype='img'),
                              Context(content = [CPI_DE.cpi_descr()], dtype='msg'),
                              Context(content = [CPI_DE.cpi()], dtype='img')]

            @staticmethod
            def cpi_inida():
                  yield from [Context(content = [CPI_INDIA.production_industry_exc_construction()], dtype='img'),
                              Context(content = [CPI_INDIA.cpi()], dtype='img')]
                  
            @staticmethod
            def cpi_jpn():
                  yield from [Context(content = [CPI_JPN.production_industry_exc_construction()], dtype='img'),
                              Context(content = [CPI_JPN.cpi()], dtype='img')]
                  
            @staticmethod
            def cpi_kr():
                  yield from [Context(content = [CPI_KR.production_industry_exc_construction()], dtype='img'),
                              Context(content = [CPI_KR.cpi()], dtype='img')]