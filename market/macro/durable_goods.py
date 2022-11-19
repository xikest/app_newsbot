from market.macro.plotviz_economic_indicator import PlotEconomicIdx

class DurableGoods:
    
    @staticmethod
    def descr():
        return """-내구재 주문, 미래 제조업 활동에 대한 주요 지표-
내구재는 자동차와 컴퓨터, 기계류, 항공기, 통신장비 등 최소 3년 평균 수명을 가지고 있는 상품을 일컫는다.
기계 설비와 같은 내구생산재에 대한 '주문'은 몇 달 후에 있을 생산과 관련된 것이다.
주문의 급증은 소비자의 수요를 만족시키기 위해 공장과 노동자들이 생산활동을 왕성하게 지속하리라는 사실을 의미한다는 점에서 경제에 긍정적인 신호로 받아들여진다.

[채권 시장]
방산재와 항공기를 제외한 신규 주문의 급증은 제조업 부문의 강화, 더 빠른 GDP 성장, 그리고 인플레이션의 상승 가능성을 제시한다.
신규 주문이 예상보다 훨씬 빠른 속도로 발생할 때 채권가격은 하락 한다. 

[주식 시장]
일반적으로 신규주문의 급증은 기업 이윤의 증가로 이어질 수 있다는 점 때문에 긍정적인 현상으로 받아들여진다.
그러나 경제가 이미 최대 생산 수준을 보이고 있다면 신규주문의 급증을 따른 이자율의 급상승 가능성에 불안을 느낄 수 있다.

[외환 시장]
다른 산업국가들에 비해 월등한 강화를 가리키는 증거가 나타날 때 대체로 반등하는 양상을 보인다.
그러나 경제 과열을 예고하는 경우에는 달러화의 가치가 하락할 수 있다. """

    @staticmethod
    def newOrder_durableGoods_descr():
        return """[신규 주문]
미국에서 생상되는 내구재에 대한 주문은 미국과 해외 구매자의 가장 최신 수요를 반영한다.
그러나 방산재 및 항공기의 대량주문 한 건이 내구재의 신규주문 전체 수치를 부풀림으로써 경제 잠재력에 대한 평가를 잘못된 방향으로 유도할 수 있다.
"""
        
    @staticmethod
    def newOrder_durableGoods(mode='binary'):
        return (PlotEconomicIdx('DGORDER').renameColumn('내구재 신규 주문')
                .plot(title='내구재 신규 주문', mode=mode, y1_title=''))
        
    @staticmethod
    def newOrder_durableGoodsExcludingTransportation_descr():
        return """[운송 제외 주문]
민간 항공기 주문이 주기적으로 발생하며 엄청난 고비용을 요구하기 때문에 제외 한다.
큰 규모의 주문이 있을 때 신규주문 총액이 일시적 팽창으로 인하여 심하게 과장된다."""
        
    @staticmethod    
    def newOrder_durableGoodsExcludingTransportation(mode='binary'):
        return (PlotEconomicIdx('ADXTNO').renameColumn('운송 제외 내구재 신규 주문')
                .plot(title='운송 제외 내구재 신규 주문', mode=mode, y1_title=''))
        
    @staticmethod
    def newOrder_durableGoodsExcludingDefence_descr():
        return """[방산재 제외 내구재 주문]
방산재 제외 주문은 산업생산량의 증감이 민간항공기 대량 주문에 영향을 받지 않는 경우에 한해 산업생산량에 대한 뛰어난 예측 도구로 여겨지고 있다..
예를 들어 비방산 내구재 주문의 증가가 34개월 동안 지속되면, 36개월 후에 제조업 활동이 광범위하게 개선되고 공장의 고용이 증가할 것이라고 짐작할 수 있다."""
         
    @staticmethod    
    def newOrder_durableGoodsExcludingDefence(mode='binary'):
        return (PlotEconomicIdx('AMTUNO').renameColumn('방산재 제외 내구재 신규 주문')
                .plot(title='방산재 제외 내구재 신규 주문', mode=mode, y1_title=''))

    @staticmethod
    def newOrder_excludingDefense_descr():
        return """[방산재 및 운송을 제외한 신규 내구재 주문]
가계의 임의 소비지출 중 15% 가량이 내구재 구매와 관련된 것으로서, 경제 상황에 대한 소비자들의 불안감이 커지면 내구재에 대한 소비지출이 가장 먼저 타격을 받게 된다.
신규 주문의 회복은 소비자들이 지출을 재개할 수 있을 정도로 재정상태와 고용전망이 안정적이며, 더 나아가 산업부문과 경제 전반에 대해서 충분히 만족하고 있다는 사실을 의미한다."""

    @staticmethod    
    def newOrder_excludingDefense(mode='binary'):
        return (PlotEconomicIdx('AMTUNO').sub('DGORDER').sub('ADXTNO').renameColumn('방산재 및 운송을 제외한 신규 내구재 주문')
                .plot(title='방산재 및 운송을 제외한 신규 내구재 주문', mode=mode, y1_title=''))
        
        
    @staticmethod
    def primaryMetals_descr():
        return """[1차 금속 주문]
대형 제조업체가 생상증가에 박차를 가하기 앞서 우선적으로 하는 일은 원재료를 충분히 확보하는 것이다."""
  
    @staticmethod    
    def primaryMetals(mode='binary'):
        return (PlotEconomicIdx('A31SNO').renameColumn('1차 금속 신규 주문')
                .plot(title='1차 금속 신규 주문', mode=mode, y1_title=''))
        
    @staticmethod
    def capitalGoods_descr():
        return """[자본재 주문]
다른 상품의 생산에 사용하기 위한 수단으로 기업들이 구매하는 값비싼 상품들을 다루고 있다.
용광고, 기계 공구, 로봇, 유사 장비 등이 속한다."""
        
    @staticmethod    
    def capitalGoods(mode='binary'):
        return (PlotEconomicIdx('ATCGNO').renameColumn('자본재 신규 주문')
                .plot(title='자본재 신규 주문', mode=mode, y1_title=''))
        
    @staticmethod
    def capitalGoodsExcludingDefence_descr():
        return """[비군수용 자본재(항공기 제외)]
핵심 자본재 주문으로 알려져 있다.
자본재 주문은 경제 침체를 6 ~12개월 선행하여 하락하며, 일반적으로 경기 침체의 바닥에서 3 ~18개월 경과 후에 반등하는 경향이 있다."""
        
    @staticmethod    
    def capitalGoodsExcludingDefence(mode='binary'):
        return (PlotEconomicIdx('NEWORDER').renameColumn('비군수용 자본재(항공기 제외) 신규 주문')
                .plot(title='비군수용 자본재(항공기 제외) 신규 주문', mode=mode, y1_title=''))
        
    @staticmethod
    def unfilledOrdersDurableGoods_descr():
        return """[수주 잔량]
대형 수주 잔량은 공장들이 향후 바쁘게 돌아갈 것을 암시한다.
수주 잔량의 증가는 경제에 문제를 초래하기도 한다. 제조 자원이 지나치게 한꺼번에 이용될 수 있고, 심각한 생산 병목 현상을 불러올 수도 있으며, 운송 지연의 유발과 심지어는 인플레이션 압력으로 이어질 수도 있다.
이러한 문제점들을 바로잡기 위해 기업들은 생산설비를 확충하거나 노동자를 고용해야 하며, 또는 생산라인을 초과 운영해야 한다.
이와 같은 개선이 이루어지지 않는다면 제조업체들은 만성적인 운송 지연에 지친 고객들을 잃어버리게 될 수 있다. 
수주 잔량은 기업들이 적정 수준으로 운영됨으로써 모든 주문을 신속히 충족시킬 수 있는 경우와 주문 자체가 현저하게 둔화는 경우에 하락할 수 있다. """        
        
    @staticmethod    
    def unfilledOrdersDurableGoods(mode='binary'):
        return (PlotEconomicIdx('AMDMUO').renameColumn('수주 잔량')
                .plot(title='수주 잔량', mode=mode, y1_title=''))
    