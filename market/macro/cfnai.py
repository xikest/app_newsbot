from market.macro.plotviz_economic_indicator import PlotEconomicIdx

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
                        .plot(title='시카고 연방은행_국가활동지수_MA3', mode=mode))
            
