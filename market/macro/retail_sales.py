from market.macro.plotviz_economic_indicator import PlotEconomicIdx

class ReatailSales:
    @staticmethod
    def advanceRetailSales(mode='binary'):
        return (PlotEconomicIdx('RSAFS').renameColumn('사전 소매 판매 보고')
                .plot(title='사전 소매 판매 보고', mode=mode, y1_title=''))
    @staticmethod    
    def retailSales(mode='binary'):
        return (PlotEconomicIdx('MRTSSM44X72USS').renameColumn('소매 판매 보고')
                .plot(title='소매 판매 보고', mode=mode, y1_title=''))
        
    @staticmethod    
    def advanceRetailSalesExcludingMotorVehicle(mode='binary'):   
        return (PlotEconomicIdx('RSFSXMV').renameColumn('사전 소매 판매 보고(자동차 제외)')
                .plot( title='사전 소매 판매 보고 (자동차 제외)', mode=mode, y1_title=''))
    @staticmethod    
    def retailSalesExcludingMotorVehicle(mode='binary'):
        return (PlotEconomicIdx('MRTSSM44Y72USS').renameColumn('소매 판매 보고 (자동차 제외)')
                .plot(title='소매 판매 보고 (자동차 제외)', mode=mode, y1_title=''))
    
    @staticmethod    
    def advanceRetailSales_Gasoline(mode='binary'):
        return (PlotEconomicIdx('RSGASS').renameColumn('사전 소매 판매 보고 (휘발유)')
                .plot(title='사전 소매 판매 보고 (휘발유)', mode=mode, y1_title=''))
            
    @staticmethod    
    def retailSales_Gasoline(mode='binary'):
        return (PlotEconomicIdx('MRTSSM447USS').renameColumn('소매 판매 보고 (휘발유)')
                .plot(title='소매 판매 보고 (휘발유)', mode=mode, y1_title=''))
        
    @staticmethod    
    def advanceRetailSales_NonstoreRetailers(mode='binary'):   
        return (PlotEconomicIdx('RSNSR').renameColumn('사전 소매 판매 보고 (무인 점포)')
                .plot(title='사전 소매 판매 보고 (무인 점포)', mode=mode, y1_title=''))
    @staticmethod    
    def retailSales_NonstoreRetailers(mode='binary'): 
        return (PlotEconomicIdx('MRTSSM454USS').renameColumn('소매 판매 보고 (무인 점포)')
                .plot(title='소매 판매 보고 (무인 점포)', mode=mode, y1_title=''))

    @staticmethod    
    def advanceRetailSales_food_drinking(mode='binary'):  
        return (PlotEconomicIdx('RSFSDP').renameColumn('사전 소매 판매 보고 (음식점 및 술집)')
                .plot(title='사전 소매 판매 보고 (음식점 및 술집)', mode=mode, y1_title=''))
        
    @staticmethod    
    def retailSales_food_drinking(mode='binary'):
        return (PlotEconomicIdx('MRTSSM722USS').renameColumn('소매 판매 보고 (음식점 및 술집)')
                .plot(title='소매 판매 보고 (음식점 및 술집)', mode=mode, y1_title=''))