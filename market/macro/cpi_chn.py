from market.macro.plotviz_economic_indicator import PlotEconomicIdx

class CPI_CHN:
    @staticmethod
    def production_industry_exc_construction(mode='binary'):
        return (PlotEconomicIdx('CHNPRINTO01IXPYM').renameColumn('중국 산업 생산')
                .plot(title='중국 산업 생산', mode=mode, y1_title=''))
        

    def cpi(mode='binary'):
        return (PlotEconomicIdx('CHNCPIALLMINMEI').renameColumn('중국 CPI')
                .plot(title='중국 CPI', mode=mode, y1_title=''))    