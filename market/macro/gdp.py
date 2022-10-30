from market.macro.plotviz_economic_indicator import PlotEconomicIdx

class GDP:
    @staticmethod
    def gdp(mode='binary'):
        return (PlotEconomicIdx('GDP').renameColumn('GDP')
                .plot(title='GDP', mode=mode, y1_title=''))
    @staticmethod    
    def personalConsumptionExpenditures(mode='binary'):
        return (PlotEconomicIdx('PCEC').renameColumn('개인 소비 지출')
                .plot(title='개인 소비 지출', mode=mode, y1_title=''))
        
    @staticmethod    
    def durableGoods(mode='binary'):
        return (PlotEconomicIdx('PCDG').renameColumn('내구재')
                .plot(title='내구재', mode=mode, y1_title=''))

    @staticmethod    
    def non_durableGoods(mode='binary'):
        return (PlotEconomicIdx('PCND').renameColumn('비내구재')
                .plot(title='비내구재', mode=mode, y1_title=''))
    @staticmethod    
    def services(mode='binary'):
        return (PlotEconomicIdx('PCESV').renameColumn('서비스')
                .plot(title='서비스', mode=mode, y1_title=''))
    
    
    def domesticInvestment(mode='binary'):
        return (PlotEconomicIdx('GPDI').renameColumn('민간 국내 총투자')
                .plot(title='민간 국내 총투자', mode=mode, y1_title=''))    
    
    def  fixedInvestment(mode='binary'):
        return (PlotEconomicIdx('FPI').renameColumn('고정 투자')
                .plot(title='고정 투자', mode=mode, y1_title=''))    
    
    def  changeInventories(mode='binary'):
        return (PlotEconomicIdx('CBI').renameColumn('민간 재고의 변화')
                .plot(title='민간 재고의 변화', mode=mode, y1_title=''))    
    
    
    def netExports(mode='binary'):
        return (PlotEconomicIdx('NETEXP').renameColumn('순수출')
                .plot(title='순수출', mode=mode, y1_title=''))    
    
    def  governmentConsumptionExpenditures_GrossInvestment(mode='binary'):
        return (PlotEconomicIdx('GCE').renameColumn('정부 소비지출과 총투자')
                .plot(title='정부 소비지출과 총투자', mode=mode, y1_title=''))    

    