from market.macro.plotviz_economic_indicator import PlotEconomicIdx

class EmploymentCostIndex:
    
    
    @staticmethod
    def descr():
        return """-고용 비용 지수, 노동 비용을 가장 포괄적으로 측정한 지수-
[채권 시장]
다른 인플레이션 관련 지수들과 같은 반응이다.

[주식 시장]
임금과 복리후생보조금이 생산성보다 빠른 속도로 증가하면 기업의 비용이 상승하고, 이것은 기업의 이윤하락을 불러 올 수 있다.
FED가 시장에 개입하여 이 상황을 역전시키려고 할 수 있다. \

[외환 시장]
신뢰할 만한 연관성이 없다."""

    @staticmethod
    def wages_descr():
        return """-민간 산업 급여, 3month-
인플레이션 압력에 노출되어 있는 여부는 민간산업 부문 급여금의 연간 변화율을 구한 후, 이것을 동기간 동안의 비농업분야 생산성(생산성과 단위비용) 연간 변화율과 비교한다
연간 급여금이 연간 생산성의 증가에 비해 느린 속도로 증가하면 기업들은 이윤 감소나 제품 가격의 상승 없이 노동자에게 더 많은 급여금을 지급할 수 있는 여력이 된다.
급여금의 상승이 생산성 증가에 비해 더 빠른 속도로 이루어진다면 이것은 인플레이션 상승의 위험을 불러오게 된다."""

    @staticmethod
    def wages(mode='binary'):
        return (PlotEconomicIdx('ECIWAG').renameColumn('민간 산업 급여, 3month')
                .plot(title='민간 산업 급여, 3month', mode=mode, y1_title=''))
    
    @staticmethod
    def wages_yearly(mode='binary'):
        return (PlotEconomicIdx('ECIWAG').renameColumn('민간 산업 급여, 연간')
                .plotWithMa(window=4,title='민간 산업 급여, 연간', mode=mode, y1_title=''))

    
        
    @staticmethod    
    def productivity_nonfarm(mode='binary'):
        return (PlotEconomicIdx('PRS85006091').renameColumn('비농업 경제 부문: 생산성, 연간')
                .plot(title='비농업 경제 부문: 생산성, 연간', mode=mode, y1_title=''))
