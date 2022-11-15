from market.macro.plotviz_economic_indicator import PlotEconomicIdx

class inventoriesSalesRatio:
    @staticmethod
    def descr():
        return ""
    
    @staticmethod
    def totalBusiness(mode='binary'):
        return (PlotEconomicIdx('ISRATIO').renameColumn('총 기업재고율')
                .plotWithMa(title='총 기업재고율', mode=mode, y1_title=''))
    @staticmethod    
    def retailers(mode='binary'):
        return (PlotEconomicIdx('RETAILIRSA').renameColumn('소매업 재고')
                .plot(title='소매업 재고', mode=mode, y1_title=''))
        
    @staticmethod    
    def retailTradeExcludingVehicle(mode='binary'):
        return (PlotEconomicIdx('MRTSIR4400AUSS').renameColumn('소매업 토탈 자동차 제외')
                .plot(title='소매업 토탈 자동차 제외', mode=mode, y1_title=''))


    @staticmethod
    def motorVehicle(mode='binary'):
        return (PlotEconomicIdx('MRTSIR441USS').renameColumn('자동차 재고율')
                .plotWithMa(title='자동차 재고율', mode=mode, y1_title=''))
    @staticmethod    
    def furniture_home_furnishings(mode='binary'):
        return (PlotEconomicIdx('MRTSIR4423XUSS').renameColumn('가구업 재고율')
                .plot(title='가구업 재고율', mode=mode, y1_title=''))
        
    @staticmethod    
    def buildingMaterials(mode='binary'):
        return (PlotEconomicIdx('MRTSIR444USS').renameColumn('건축자재 재고율')
                .plot(title='건축자재 재고율', mode=mode, y1_title=''))




    @staticmethod
    def clothing(mode='binary'):
        return (PlotEconomicIdx('MRTSIR448USS').renameColumn('의류 재고율')
                .plotWithMa(title='의류 재고율', mode=mode, y1_title=''))
    @staticmethod    
    def food_beverage(mode='binary'):
        return (PlotEconomicIdx('MRTSIR445USS').renameColumn('식음료 재고율')
                .plot(title='식음료 재고율', mode=mode, y1_title=''))
        
    @staticmethod    
    def generalMrchandise(mode='binary'):
        return (PlotEconomicIdx('MRTSIR452USS').renameColumn('종합 소매업 재고율')
                .plot(title='종합 소매업 재고율', mode=mode, y1_title=''))



    @staticmethod
    def department(mode='binary'):
        return (PlotEconomicIdx('MRTSIR4521EUSS').renameColumn('백화점 재고율')
                .plotWithMa(title='백화점 재고율', mode=mode, y1_title=''))
    @staticmethod    
    def merchantWholesalers(mode='binary'):
        return (PlotEconomicIdx('WHLSLRIRSA').renameColumn('도매업 재고')
                .plot(title='도매업 재고', mode=mode, y1_title=''))
        
    @staticmethod    
    def manufacturers(mode='binary'):
        return (PlotEconomicIdx('MNFCTRIRSA').renameColumn('제조업 재고')
                .plot(title='제조업 재고', mode=mode, y1_title=''))


    @staticmethod
    def businessInventories(mode='binary'):
        return (PlotEconomicIdx('TOTBUSMPCIMSA').renameColumn('총기업 재고 변화')
                .plotWithMa(title='총기업 재고 변화', mode=mode, y1_title=''))
    @staticmethod    
    def retailersInventories(mode='binary'):
        return (PlotEconomicIdx('RETAILMPCIMSA').renameColumn('소매업 재고 변화')
                .plot(title='소매업 재고 변화', mode=mode, y1_title=''))
        
    @staticmethod    
    def merchantWholesalersInventories(mode='binary'):
        return (PlotEconomicIdx('WHLSLRMPCIMSA').renameColumn('도매업 재고 변화')
                .plot(title='도매업 재고 변화', mode=mode, y1_title=''))

    @staticmethod    
    def manufacturersInventories(mode='binary'):
        return (PlotEconomicIdx('MNFCTRMPCIMSA').renameColumn('제조업 재고 변화')
                .plot(title='제조업 재고 변화', mode=mode, y1_title=''))


