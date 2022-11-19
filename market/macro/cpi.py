from market.macro.plotviz_economic_indicator import PlotEconomicIdx

class CPI:
    @staticmethod
    def descr():
        return """[채권 시장]
core CPI는 인플레이션 율의 근본적인 하락을 반영하기 때문에 이 지수가 급등하면 채권에서의 손실은 더 악화될 가능성이 크다. 

[주식 시장]
core CPI의 급격한 상승을 악재로 받아들인다.
높은 CPI는 금리 상으로 이어지고, 이것은 기업의 대출비용 상승으로 연결되기 때문이다.
기업의 매출과 수익이 인플레이션의 영향으로 증가할 수 있지만, 이것은 가격 상승보다 판매 증가에 따른 기업의 수익증가를 선호하는 주주들에게 반가운 소식이 아니다.
인플레이션의 위협은 FED의 시장 개입을 불러올 수 있다. 

[외환 시장]
금리 인상은 달러를 인기있는 통화로 만든다.
그러나 인플레이션에 대한 우려에서 야기되는 이자율의 급상승은 달러의 가치에 손상을 입힌다.
또한 높은 인플레이션은 달러화 표시 투자자산의 가치를 하락시킬 가능성도 있다.\ CPI의 지속적인 상승은 달러에 부정적인 영향을 끼친다고 할 수 있다."""
    
    @staticmethod
    def headLine(mode='binary'):
        return (PlotEconomicIdx('CPIAUCSL').renameColumn('CPI 모든 품목')
                .plot(title='CPI head', mode=mode, y1_title=''))
        
    @staticmethod    
    def core_descr():
        return """[핵심 소비자 물가 지수(Core)]
식량과 에너지 가격을 제외한 항목들에 대한 소비자 물가 지수
CPI에서 약 25%를 차지하는 식량과 에너지의 가격은 흉작이나 전 세계적 오일 공급 하락 같은 일시적 요인으로 인해 극심하게 변동할 수 있어 경제에 나타나는 인플레이션이 왜곡될 수 있다."""
        
    @staticmethod    
    def core(mode='binary'):
        return (PlotEconomicIdx('CPILFESL').renameColumn('CPI core')
                .plot(title='CPI core', mode=mode, y1_title=''))
        
    @staticmethod    
    def ma_descr():
        return """[소비자 물가 지수 동향의 변화]
3개월, 6개월, 12개월 동안의 소비자물가지수 변화율"""
        
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
    def medicalCare_descr():
        return """[의료]
기업체의 직원 건강보험듬 부담은 기업 지출에서 가장 큰 비중을 차지하는 항목 중 하나이다.
기업들은 직원 건강보험금 부담금을 예산 편성에 포함 시킬 때 CPI 보고서 중 '의료' 항목을 참조한다."""
        
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