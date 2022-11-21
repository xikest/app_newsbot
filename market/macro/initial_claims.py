from market.macro.plotviz_economic_indicator import PlotEconomicIdx

class InitialClaims:
    @staticmethod
    def descr():
        return """-주간 실업수당 신청건수-
[채권 시장]
실업 수당 신규 청구 건수가 30,000건 이상 급중하는 현상을 호재로 받아들인다. 신규 신청 건수의 증가는 경제 상황의 악화와 인플레이션 압력의 감소를 의미한다.
[주식 시장]
실업 수당 청구 건수의 증가가 금리의 하락으로 이어지면서 주가에 긍정적인 영향을 주기도 하지만, 노동시장의 심각한 악화를 암시한다는 점에서 경제와 기업 이윤, 주가에 부정적인 영향을 줄 수 있다.
[외환 시장]
경제의 침체에서 비롯된 신규 청구 건수의 지속적인 증가는 미국 채권을 매도하도록 유도하며, 외환 시장에서의 달러 가치를 약화 시킨다."""

    @staticmethod
    def initialClaims_4WeekMA (mode='binary'):
        return (PlotEconomicIdx('IC4WSA').renameColumn('주간 실업 수당 신청 건수 MA 4weeks')
                .plot(title='주간 실업 수당 신청 건수 MA 4weeks', mode=mode, y1_title=''))
        
    @staticmethod
    def insuredUnemployment_4WeekMA (mode='binary'):
        return (PlotEconomicIdx('CC4WSA').renameColumn('주간 실업 보험 수 MA 4weeks')
                .plot(title='주간 실업 보험 수 MA 4weeks', mode=mode, y1_title=''))
        
    @staticmethod
    def insuredUnemploymentRate_descr():
        return """실업 보험 수취 실업 률
미국 노동자의 총수 대비 현재 실업보험을 수취하고 있는 사람들의 수를 비교한 비율"""
    
    @staticmethod
    def insuredUnemploymentRate(mode='binary'):
        return (PlotEconomicIdx('IURSA').renameColumn('실업 보험 수취 실업 률')
                .plot(title='실업 보험 수취 실업 률', mode=mode, y1_title=''))