from market.macro.plotviz_economic_indicator import PlotEconomicIdx

class NewResidentialSales:
    @staticmethod
    def descr():
        return """[신규 주택 판매, 신규 단독 주택의 월간 판매를 측정]

[채권 시장]
경제가 활발히 성장하는 동안 신규주택의 판매가 예쌍보다 더 높은 수준으로 증가하면 인플레이션의 위협이 다가왔을 암시함으로써 채권가격 하락을 유발할 수 있다.
경재 회복기에서는 신규주택 판매의 반등이 물가상승을 그다지 부추기지 않는다.
주택 판매율에서 매달 반복적으로 급락이 나타날 경우 경제상황이 악화되고 인플레이션이 하락할 것이라고 예쌍할 수 있다.

[주식 시장]
반응이 없다.

[외환 시장]
반응이 없다."""
    
    @staticmethod
    def housesSold_descr():
        return """[판매 완료 신규 주택]
판매 동향이 눈에 띄게 변화하면 이것은 경제 성장이 멈추었거나 또는 회복을 위해 피치를 올리고 있음을 의미한다."""
    
    @staticmethod
    def housesSold(mode='binary'):
        return (PlotEconomicIdx('HSN1F').renameColumn('판매 완료 신규 주택')
                .plot(title='판매 완료 신규 주택', mode=mode, y1_title=''))
        
    @staticmethod
    def monthlySupply_descr():
        return """[월간 공급]
신규 주택재고율은 가장 최근의 신규주택 판매 속도를 기준으로 하였을 때 신규 주택의 현재 공급물량이 판매 완료 되기까지 몇 달의 시간이 소요되는지를 측정하는 것으로서, 미래 주택건설산업을 예껸하는 지표 역할을 한다.
주택 판매가 활기를 띠면 일반적으로 주택의 월간공급률은 안정적으로 유지되거나 하락하는 경향이 있다.
월간공급률이 4개월분의 공급량에 해당하는 수준 또는 그 이하로 하락한다면 신규 건설에 대한 건설업체들의 투자가 지속적으로 나타난다.
주택 판매가 하락하거나 또는 건설 중인 모든 신규주택을 구매할 수 있는 구매자가 충분하지 않다면 신규 주택의 재고율은 6개월 이상 수준으로 상승할 수 있다.
이러한 상황은 대부분 신규주택 건설 활동의 침체를 예견하는 것으로 해석된다."""
    
    @staticmethod    
    def monthlySupply(mode='binary'):
        return (PlotEconomicIdx('MSACSR').renameColumn('월간 공급')
                .plot(title='월간 공급', mode=mode, y1_title=''))

    @staticmethod
    def medianSalesPriceforNewHousesSold_descr():
        return """[주택판매 가격의 중앙값]
신규 주택 가격은 기존 주택 가격보다 더 빠른 속도로 상승하는 경향이 있다.
신규 주택이 일반적으로 기존주택에 비해 더 많은 현대적 집기나 편의시설들을 구비하고 있기 때문이다.
신규 주택 가격이 인플레이션에 비해 지나치게 빠른 속도로 상승하면 주택을 매력적인 장기 투자 수단으로 여길 가능성이 커진다."""

    @staticmethod    
    def medianSalesPriceforNewHousesSold(mode='binary'):
        return (PlotEconomicIdx('MSPNHSUS').renameColumn('신규 주택판매 가격의 중앙값')
                .plot(title='신규 주택판매 가격의 중앙값', mode=mode, y1_title=''))
        
    @staticmethod    
    def averageSalesPriceforNewHousesSold(mode='binary'):
        return (PlotEconomicIdx('ASPNHSUS').renameColumn('신규 주택판매 가격의 평균값')
                .plot(title='신규 주택판매 가격의 평균값', mode=mode, y1_title=''))
        
    @staticmethod
    def newHousesSoldNotStarted_descr():
        return """대상 기간 동안 판매되었지만 착공이 시작되지 않음]
단독주택 부지의 매매가 크게 증가하면 더 많은 집을 지을 것이라는 전조로 볼 수 있다.
기본적으로 공사가 아직 시작되지 않은 최근 달에 팔린 부지의 수를 계산하며, 해당 지표가 변화하는 것을 관찰하면 주택시장 동향을 파악할 수 있는 좋은 선행 지표로 활용할 수 있다."""
    
    @staticmethod    
    def newHousesSoldNotStarted(mode='binary'):
        return (PlotEconomicIdx('NHSDPNSS').renameColumn('대상 기간 동안 판매되었지만 착공이 시작되지 않음')
                .plot(title='대상 기간 동안 판매되었지만 착공이 시작되지 않음', mode=mode, y1_title=''))
    