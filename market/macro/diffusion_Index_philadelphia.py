from market.macro.plotviz_economic_indicator import PlotEconomicIdx

class DiffusionIndexphiladelphia:
    @staticmethod
    def descr():
        return ""
    
    @staticmethod
    def currentGeneralActivity(mode='binary'):
        return (PlotEconomicIdx('GACDFSA066MSFRBPHI').renameColumn('전반적 경제 활동 지수')
                .plotWithMa(title='전반적 경제 활동 지수', mode=mode))
    @staticmethod    
    def futureEmployment(mode='binary'):
        return (PlotEconomicIdx('NEFDFSA066MSFRBPHI').renameColumn('6개월 제조업분야 고용자 수 전망')
                .plot(title='6개월 제조업분야 고용자 수 전망', mode=mode))
        
    @staticmethod    
    def futureCapitalExpenditures(mode='binary'):
        return (PlotEconomicIdx('CEFDFSA066MSFRBPHI').renameColumn('6개월 자본 지출 전망')
                .plot(title='6개월 자본 지출 전망', mode=mode))
