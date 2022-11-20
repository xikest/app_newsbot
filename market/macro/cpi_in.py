from market.macro.plotviz_economic_indicator import PlotEconomicIdx

class CPI_IN:
    @staticmethod
    def production_industry_exc_construction(mode='binary'):
        return (PlotEconomicIdx('INDPRINTO01GYSAM').renameColumn('인도 산업 생산')
                .plot(title='인도 산업 생산', mode=mode, y1_title=''))
        
    def cpi(mode='binary'):
        return (PlotEconomicIdx('INDCPIALLMINMEI').renameColumn('인도 CPI')
                .plot(title='인도 CPI', mode=mode, y1_title=''))    