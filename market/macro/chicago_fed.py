from market.macro.plotviz_economic_indicator import PlotEconomicIdx

class NFCI:
    
    @staticmethod
    def descr():
        return """국가재정상황지수"""
    
    @staticmethod
    def financialConditionsIndex_descr():
        return """NFCI의 plus값은 평균보다 타이트한 재정 상태를 나타내고 마이너스 값은 평균보다 느슨한 재정 상태를 나타낸다.
    NFCI(Risk, Credit, Leverage)의 3가지 Subindex는를 통해 NFCI의 움직임을 보다 상세하게 조사할 수 있다.
    NFCI와 마찬가지로 평균 값이 0이고 표준 편차가 1이 되도록 구성되어 있다.
    Risk Subindex는 금융부문의 변동성과 자금조달 위험을 포착하고, 
    Credit Subindex는 신용조건의 척도로 구성되며, 
    Leverage Subindex는 부채 및 지분 척도로 구성된다.
    리스크의 증가, 신용조건의 긴축, 레버리지의 감소는 재무조건의 긴축과 일치한다.
    따라서 개별 하위지수에 대한 양의 값은 대응하는 재무상황의 측면이 평균보다 빡빡함을 나타내며, 음의 값은 그 반대임을 나타낸다."""
    
    @staticmethod
    def financialConditionsIndex(mode='binary'):
        return (PlotEconomicIdx('NFCI').renameColumn('National Financial Conditions Index')
                        .plot(title='National Financial Conditions Index', mode=mode, y1_title='',secondary_y=False))
            
    @staticmethod
    def financialConditionsCreditSubindex(mode='binary'):
        return (PlotEconomicIdx('NFCICREDIT').renameColumn('nfci Credit Subindex')
                        .plot(title='nfci Credit Subindex', mode=mode, y1_title='',secondary_y=False))
    @staticmethod
    def financialConditionsLeverageSubindex(mode='binary'):
        return (PlotEconomicIdx('NFCILEVERAGE').renameColumn('nfci Leverage Subindex')
                        .plot(title='nfci Leverage Subindex', mode=mode, y1_title='',secondary_y=False))
        
        
    @staticmethod
    def financialConditionsRiskSubindex(mode='binary'):
        return (PlotEconomicIdx('NFCIRISK').renameColumn('nfci Risk Subindex')
                        .plot(title='nfci Risk Subindex', mode=mode, y1_title='',secondary_y=False))
        
    @staticmethod
    def financialConditionsNonfinancialLeveralSubindex_descr():
        return """NFCI의 onfinancial Leveral Subindex는 레버리지가 금융 스트레스와 경제성장에 미치는 잠재적 영향에 대한 조기 경고 신호로 어떻게 작용할 수 있는지를 가장 잘 보여준다.
이 NFCI Subindex의 가계 및 비금융 사업 레버리지 조치에 할당된 양의 가중치는 종종 "financial accelerator"라고 불리는 경제의 금융 부문과 비금융 부문 간의 피드백 과정의 특징을 만든다.
갈수록 긴축적인 재무 상황은 위험 프리미엄의 상승과 자산 가치의 하락과 관련되어 있다.
따라서 가계와 비금융회사의 순자산은 credit tightens과 동시에 감소한다.
이는 경제의 금융 및 비금융 부문에 걸쳐 deleveraging(즉, 부채 감소)을 초래하고 궁극적으로 경제 활동을 감소시킨다."""
   
   
    @staticmethod
    def financialConditionsNonfinancialLeveralSubindex(mode='binary'):
        return (PlotEconomicIdx('NFCINONFINLEVERAGE').renameColumn('nfci Nonfinancial Leveral Subindex')
                        .plot(title='nfci Nonfinancial Leveral Subindex', mode=mode, y1_title='',secondary_y=False))
        
    
class CFNAI:
    @staticmethod
    def descr():
        return """-시카고 연방은행_국가활동지수-
경제 활동과 인플레이션 압력을 측정하는 전국단위 지수"""

    def chicagoFedNationalActivityIndex_descr():
        return """[CFNAI-MA3]
MA 값이 0.7 이하로 하락한다면 경기 침체의 가능성이 상당한 수준에 이르렀음을 알 수 있다.
지수가 -1.5까지 하락하면 심각한 불황을 겪고 있을 가능성이 크다.
0.2 이상을 기록한다면, 경기 침체 종료를 암시한다.
MA 값이 2년 이상 0.7 이상까지 상승하며 경제성장이 이어진다면, 인플레이션의 가속화를 경고하는 신호로 볼 수 있다.
경기 확장이 본격화 되었을 때 MA 값이 1.0 이상을 보인다면 기업활동이 과열되고 있으며 인플레이션이 지속적으로 상승할 것이라는 경고로 받아들여도 무방하다.
    """
    
    @staticmethod
    def chicagoFedNationalActivityIndex(mode='binary'):
        return (PlotEconomicIdx('CFNAIMA3').renameColumn('시카고 연방은행_국가활동지수')
                        .plot(title='시카고 연방은행_국가활동지수_MA3', mode=mode, secondary_y=False))
            
