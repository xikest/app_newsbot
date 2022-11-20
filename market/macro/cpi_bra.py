from market.macro.plotviz_economic_indicator import PlotEconomicIdx

class CPI_BRA:
    
    
    @staticmethod
    def production_industry_exc_construction(mode='binary'):
        return (PlotEconomicIdx('BRAPROINDMISMEI').renameColumn('브라질 산업 생산')
                .plot(title='브라질 산업 생산', mode=mode, y1_title=''))
        

    def cpi(mode='binary'):
        return (PlotEconomicIdx('CPALTT01BRM659N').renameColumn('브라질 CPI')
                .plot(title='브라질 CPI', mode=mode, y1_title=''))    