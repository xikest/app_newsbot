from market.macro.plotviz_economic_indicator import PlotEconomicIdx

class CPI_DE:
    
    @staticmethod
    def production_industry_exc_construction_descr():
        return """[독일 산업 생산]
유로존 전체의 국내 총샌상의 변화와 밀접한 연관성을 보인다."""
    
    @staticmethod
    def production_industry_exc_construction(mode='binary'):
        return (PlotEconomicIdx('DEUPROINDMISMEI').renameColumn('독일 산업 생산')
                .plot(title='독일 산업 생산', mode=mode, y1_title=''))
        
    @staticmethod
    def cpi_descr():
        return """[독일 CPI]
독일의 물가가 우려할 만한 속도로 상승한다면, 인접 국가들의 물가상승률이 상대적으로 안정된 수준을 보일 때에도 ECB는 금리를 상향할 가능성이 매우 크다."""

    def cpi(mode='binary'):
        return (PlotEconomicIdx('DEUCPIALLMINMEI').renameColumn('독일 CPI')
                .plot(title='독일 CPI', mode=mode, y1_title=''))    