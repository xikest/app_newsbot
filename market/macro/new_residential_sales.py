from market.macro.plotviz_economic_indicator import PlotEconomicIdx

class NewResidentialSales:
    @staticmethod
    def housesSold(mode='binary'):
        return (PlotEconomicIdx('HSN1F').renameColumn('판매 완료 신규 주택')
                .plot(title='판매 완료 신규 주택'))
    @staticmethod    
    def monthlySupply(mode='binary'):
        return (PlotEconomicIdx('MSACSR').renameColumn('월간 공급')
                .plot(title='월간 공급', mode=mode))
        
    @staticmethod    
    def medianSalesPriceforNewHousesSold(mode='binary'):
        return (PlotEconomicIdx('MSPNHSUS').renameColumn('신규 주택판매 가격의 중앙값')
                .plot(title='신규 주택판매 가격의 중앙값', mode=mode))
        
    @staticmethod    
    def averageSalesPriceforNewHousesSold(mode='binary'):
        return (PlotEconomicIdx('ASPNHSUS').renameColumn('신규 주택판매 가격의 평균값')
                .plot(title='신규 주택판매 가격의 평균값', mode=mode))
    @staticmethod    
    def newHousesSoldNotStarted(mode='binary'):
        return (PlotEconomicIdx('NHSDPNSS').renameColumn('대상 기간 동안 판매되었지만 착공이 시작되지 않음')
                .plot(title='대상 기간 동안 판매되었지만 착공이 시작되지 않음', mode=mode))
    