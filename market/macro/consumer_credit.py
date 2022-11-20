from market.macro.plotviz_economic_indicator import PlotEconomicIdx

class ConsumerCredit :
    @staticmethod
    def descr():
        return """-소비자 신용 거래 미상환분-

[채권 시장]
별다른 영향을 미치지 않는다.
예기치 않은 차입의 폭등은 채권시장을 교란시킬 수도 있다.

[주식 시장]
일반적으로 영향을 주지 않는다.
차입의 지속적인 감소가 감지된다면, 이는 가계가 처한 재정적 압력을 암시하며, 나아가 소비자 지출의 감소 및 이에 따른 기업들의 매출 감소로 이어진다.

[외환 시장]
별다른 영향을 미치지 않는다.
"""

    @staticmethod
    def report_url():
        return "https://www.federalreserve.gov/releases/g19"
    
    @staticmethod
    def total_consumer_credit(mode='binary'):
        return (PlotEconomicIdx('TOTALSL').renameColumn('소비자 신용거래 미상환분')
                .plot(title='소비자 신용거래 미상환분', mode=mode, y1_title=''))

    @staticmethod
    def revolvingConsumerCreditOwnedSecuritized_descr():
        return """[소비자 신용거래 미상환분(리볼빙)]
소비자들은 경기불황의 조짐이 보인다 하더라도 현재의 생활수준을 낮추는 것을 꺼리기 때문에 경기가 불안정한 시기에도 여전히 강세를 보일 수 있다.
갑자기 외식, 주말여행, 쇼핑, 영화관람 등과 같은 취미 생활을 위한 지출을 줄이는 것은 쉽지 않다
뿐만 아니라 휴대전화 사용료, 의약품 구입, 음식 등의 필수품에 지출을 멈출 수 있는 것도 아니다.
"""
    @staticmethod
    def revolvingConsumerCreditOwnedSecuritized (mode='binary'):
        return (PlotEconomicIdx('REVOLSL').renameColumn('소비자 신용거래 미상환분(리볼빙)')
                .plot(title='소비자 신용거래 미상환분(리볼빙)', mode=mode, y1_title=''))
        
    @staticmethod
    def non_revolvingConsumerCreditOwnedSecuritized_descr():
        return """[소비자 신용거래 미상환분(Non 리볼빙)]
높은 이자율에 따른 채무상환 비용의 증가와 향후의 임금하락 및 수급에 대한 불안감 때문에 소비자들은 값비싼 물건을 사는 것을 꺼려할 것이고, 그 결과 비회전 신용을 위한 대출 신청의 하락이 나타나게 될 것이다.
"""
    @staticmethod
    def non_revolvingConsumerCreditOwnedSecuritized (mode='binary'):
        return (PlotEconomicIdx('NONREVSL').renameColumn('소비자 신용거래 미상환분(Non 리볼빙)')
                .plot(title='소비자 신용거래 미상환분(Non 리볼빙)', mode=mode, y1_title=''))
        
    @staticmethod
    def percentChangeTotalConsumerCredit_descr():
        return """[소비자 신용거래 미상환분]
소비자의 채무 수준이 증가하고 있는지 감소하고 있는지를 제시한다.
"""
    @staticmethod
    def percentChangeTotalConsumerCredit(mode='binary'):
        return (PlotEconomicIdx('TOTALSLAR').renameColumn('소비자 신용거래 미상환분')
                .plot(title='소비자 신용거래 미상환분', mode=mode, y1_title=''))
        
    @staticmethod
    def commercialInterestRate_CreditCardPlans_descr():
        return """[신용카드 대출 금리]
신용카드를 통한 대출에 가장 높은 이자율이 적용되므로, 경기 불황기 동안에는 가계가 대출금을 상환하는 데 더욱 큰 어려움을 겪을 수 있다.
그 결과 신용카드대금 미납 폭등과 개인 파산 신청의 증가로 이어질 수 있다.
"""
    @staticmethod
    def commercialInterestRate_CreditCardPlans(mode='binary'):
        return (PlotEconomicIdx('TERMCBCCALLNS').renameColumn('신용카드 대출 금리')
                .plot(title='신용카드 대출 금리', mode=mode, y1_title=''))
    