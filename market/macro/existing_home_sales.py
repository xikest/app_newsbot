from market.macro.plotviz_economic_indicator import PlotEconomicIdx

class ExistingHomeSales:
    @staticmethod
    def existingHomeSales(mode='binary'):
        return (PlotEconomicIdx('EXHOSLUSM495S').renameColumn('기존 주택 판매')
                        .plot(title='기존 주택 판매', mode=mode, y1_title=''))
            
    @staticmethod
    def housingInventory(mode='binary'):
        return (PlotEconomicIdx('HOSINVUSM495N').renameColumn('기존 주택 재고')
                        .plot(title='기존 주택 재고', mode=mode, y1_title=''))
            
    @staticmethod
    def monthsSupply(mode='binary'):
        return (PlotEconomicIdx('HOSSUPUSM673N').renameColumn('주택재고율')
                        .plot(title='주택재고율', mode=mode, y1_title=''))
            
    @staticmethod
    def medianSalesPrice(mode='binary'):
        return (PlotEconomicIdx('HOSMEDUSM052N').renameColumn('기존주택 판매가격')
                        .plot(title='기존주택 판매가격', mode=mode, y1_title=''))
            
    @staticmethod
    def medHousingAffordabilityIndexianSalesPrice(mode='binary'):
        return (PlotEconomicIdx('FIXHAI').renameColumn('주택 구매력 지수')
                        .plot(title='주택 구매력 지수, 100', mode=mode, y1_title=''))
            

    # @staticmethod
    # def pendingHomeSalesIndex():
    #     return "https://www.nar.realtor/research-and-statistics/housing-statistics/pending-home-sales"