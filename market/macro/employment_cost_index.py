from market.macro.plotviz_economic_indicator import PlotEconomicIdx

class EmploymentCostIndex:
    @staticmethod
    def wages(mode='binary'):
        return (PlotEconomicIdx('ECIWAG').renameColumn('민간 산업 급여, 3month')
                .plot(title='민간 산업 급여, 3month', mode=mode, y1_title=''))
    
    #민간 산업 급여, 연간
    # @staticmethod    
    # def realDisposablePersonalIncome(mode='binary'):
    #     return (PlotEconomicIdx('DSPIC96').renameColumn('실질 가처분 소득')
    #             .plot(title='실질 가처분 소득', mode=mode, y1_title=''))
    
    
        
    @staticmethod    
    def productivity_nonfarm(mode='binary'):
        return (PlotEconomicIdx('PRS85006091').renameColumn('비농업 경제 부문: 생산성, 연간')
                .plot(title='비농업 경제 부문: 생산성, 연간', mode=mode, y1_title=''))
