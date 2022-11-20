from market.macro.plotviz_economic_indicator import PlotEconomicIdx

class CPI_JPN:
    @staticmethod
    def production_industry_exc_construction(mode='binary'):
        return (PlotEconomicIdx('JPNPRINTO01GYSAM').renameColumn('일본 산업 생산')
                .plot(title='일본 산업 생산', mode=mode, y1_title=''))
        

    def cpi(mode='binary'):
        return (PlotEconomicIdx('JPNCPIALLMINMEI').renameColumn('일본 CPI')
                .plot(title='일본 CPI', mode=mode, y1_title=''))    