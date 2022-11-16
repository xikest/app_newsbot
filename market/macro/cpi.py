from market.macro.plotviz_economic_indicator import PlotEconomicIdx

class CPI:
    @staticmethod
    def headLine(mode='binary'):
        return (PlotEconomicIdx('CPIAUCSL').renameColumn('CPI 모든 품목')
                .plot(title='CPI head', mode=mode, y1_title=''))
    @staticmethod    
    def core(mode='binary'):
        return (PlotEconomicIdx('CPILFESL').renameColumn('CPI core')
                .plot(title='CPI core', mode=mode, y1_title=''))
        
    @staticmethod    
    def ma3month(mode='binary'):
        return (PlotEconomicIdx('CPILFESL').renameColumn('CPI 3month_ma')
                .plotWithMa(window=3, title='CPI 3month_ma', mode=mode, y1_title=''))
    @staticmethod    
    def ma6month(mode='binary'):
        return (PlotEconomicIdx('CPILFESL').renameColumn('CPI 6month_ma')
                .plotWithMa(window=6, title='CPI 6month_ma', mode=mode, y1_title=''))
        
    @staticmethod    
    def ma12month(mode='binary'): 
        return (PlotEconomicIdx('CPILFESL').renameColumn('CPI 12month_ma')
                .plotWithMa(window=12, title='CPI 12month_ma',mode=mode, y1_title=''))
        
    @staticmethod    
    def medicalCare(mode='binary'):
        return (PlotEconomicIdx('CUSR0000SAM2').renameColumn('CPI 의료')
                .plot(title='CPI 의료', mode=mode, y1_title=''))
    @staticmethod    
    def shelter(mode='binary'):
        return (PlotEconomicIdx('CUSR0000SAH1').renameColumn('CPI 주거비')
                .plot(title='CPI 주거비', mode=mode, y1_title=''))
    
    def rent(mode='binary'):
        return (PlotEconomicIdx('CUSR0000SEHA').renameColumn('CPI 주택 렌트')
                .plot(title='CPI 주택 렌트', mode=mode, y1_title=''))    