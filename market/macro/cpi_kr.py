from market.macro.plotviz_economic_indicator import PlotEconomicIdx

class CPI_KR:
    
    
    @staticmethod
    def production_industry_exc_construction(mode='binary'):
        return (PlotEconomicIdx('KORPRINTO01GPSAM').renameColumn('한국 산업 생산')
                .plot(title='한국 산업 생산', mode=mode, y1_title=''))
        

    def cpi(mode='binary'):
        return (PlotEconomicIdx('KORCPIALLMINMEI').renameColumn('한국 CPI')
                .plot(title='한국 CPI', mode=mode, y1_title=''))    