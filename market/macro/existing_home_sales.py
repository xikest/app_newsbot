from market.macro.plotviz_economic_indicator import PlotEconomicIdx

class ExistingHomeSales:
    
    @staticmethod
    def descr():
        return """-기존 주택 판매, 기존 단독 주택의 월간 판매를 측정-
    
[채권 시장]
경제가 과열상태에 가까워지거나 인플레이션 압력의 폭발저인 증가에 직면하고 있는 상황이 아니라면, 채권시장은 기존주택 판매에 별다른 반응을 보이지 않는다.
기존 주택 판매의 급락은 몇 달 후 경제 활동의 침체가 나타날 것이라는 징조로 여겨진다.

[주식 시장]
주택 산업은 대다수의 다른 산업들이 의존하고 있는 주요 산업이다.
긍정적인 결과를 주식 시장에도 긍정적인 영향을 준다.
그러나 기존주택판매가 과열 양상을 보이면 인플레이션을 부추킴으로써 FED가 금리를 인상시킬 수 있다.

[외환 시장]
기존 주택 판매가 지속적으로 하락하지 않는 한, 달러 가치는 안정적인 수준을 유지하거나 상승세를 보이는 것이 일반적이다."""
    
    @staticmethod
    def existingHomeSales_descr():
        return """[기존 주택 판매]
소비자 지출, 특히 가구와 가전제품 같은 내구재에 대한 소비자 지출과 기존주택구매 사이에는 높은 상관관계가 존재한다.
기존 주택 판매의 지속적인 하락 또는 반등은 종종 경제의 터닝포인트를 암시한다.
주택판매의 현저한 증가는 큰 폭의 자본이득 상승을 불러오는데, 그 결과 더 많은 주택구매와 관련 소비를 촉진할 수 있다.
고용 시장의 약화는 주택구입을 둔화시킬 것이며, 모기지율이 1% 상승할 때마다 기존주택판매가 250,000채씩 감소한다고 추정된다."""
    
    @staticmethod
    def existingHomeSales(mode='binary'):
        return (PlotEconomicIdx('EXHOSLUSM495S').renameColumn('기존 주택 판매')
                        .plot(title='기존 주택 판매', mode=mode, y1_title=''))
            
    @staticmethod
    def housingInventory(mode='binary'):
        return (PlotEconomicIdx('HOSINVUSM495N').renameColumn('기존 주택 재고')
                        .plot(title='기존 주택 재고', mode=mode, y1_title=''))
        
    @staticmethod
    def monthsSupply_descr():   
        return """[주택재고율]
기존 주택 재고 판매에 몇 달이 소요되는지를 보여준다.
일반적으로 4.5 ~ 6개월분이 균형 상태라고 본다.
4.5개월 이하인 경우 주택 공급에 차질이 생길 것임을 암시함으로써 주택 가격에 대한 상승압력이 거세질 수 있다.
6개월 이상의 재고율은 주택의 공급이 수요를 초과했음을 의미하며 그 결과 주택가격의 하락 가능성이 증가한다."""
    
    @staticmethod
    def monthsSupply(mode='binary'):
        return (PlotEconomicIdx('HOSSUPUSM673N').renameColumn('주택재고율')
                        .plot(title='주택재고율', mode=mode, y1_title=''))
            
    @staticmethod
    def medianSalesPrice_descr():   
        return """[기존주택 판매가격]
주거용 부동산의 가치가 지난 몇 달 혹은 몇 년동안 인플레이션과 비교해 어떤 양상의 변화를 보여 왔는지를 설명해준다.
부동산 가격이 인플레이션보다 빠른 속도로 상승한다면, 주택을 매력적인 투자 대상으로 간주하게 될 것이다."""          

    @staticmethod
    def medianSalesPrice(mode='binary'):
        return (PlotEconomicIdx('HOSMEDUSM052N').renameColumn('기존주택 판매가격')
                        .plot(title='기존주택 판매가격', mode=mode, y1_title=''))
            
    @staticmethod
    def medHousingAffordabilityIndexianSalesPrice_descr():   
        return """[주택 구매력 지수]
'전형적인 가정'이 '전형적인 주택' 구매를 위해 주택담보대출 자격을 얻을 수 있는지 말해준다.
'전형적인 가정'은 중위수 가계 소득의 가정을 말한다.
'전형적인 주택'은 기존 단족주택의 '중앙값 주택'을 말한다.
이 지수가 100을 가리키면 중앙소득 가정의 소득이 중앙값 주택구매를 위한 모기지 신청에 요구되는 자격 수준과 정확히 일치한다고 볼 수 있다.
100 이상일 경우, 선수금의 수준을 20%로 가정했을 때 중앙 소득가정의 소득이 중앙값 주택구매를 위한 모기지 신청에 요구되는 자격 수준보다 높다고 여겨진다.
예를 들어 종합지수 130은 중앙소득가정이 중앙값 주택 가격의 80%를 커버할 수 있는 모기지 신청에 요구되는 소득의 130%를 벌어들어고 있다는 사실을 가리킨다. 
100 이상이면 주택 구매 능력이 높다"""             
            
    @staticmethod
    def medHousingAffordabilityIndexianSalesPrice(mode='binary'):
        return (PlotEconomicIdx('FIXHAI').renameColumn('주택 구매력 지수')
                        .plot(title='주택 구매력 지수, 100', mode=mode, y1_title=''))
            

    @staticmethod
    def pendingHomeSalesIndex():
        return "https://www.nar.realtor/research-and-statistics/housing-statistics/pending-home-sales"