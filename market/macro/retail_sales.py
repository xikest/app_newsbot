from market.macro.plotviz_economic_indicator import PlotEconomicIdx

class ReatailSales:
    @staticmethod
    def descr():
        return """-소매 판매 보고서-

소비자 지출은 전체 경제 활동에서 70%를 차지하고 있으며, 이 중 소매 판매는 1/3을 차지한다.
만약 소비자들이 지출을 끊임없이 지속할 수 있다면, 이것은 전반적인 경제성장과 번영의 신호로 여길 수 있다.
이 지표는 백화점과 자동차 판매점, 주유소, 음식점 등에서 판매하는 제품에 대한 지출만을 다루고 있으며, 항공여해과 치과진료, 이발, 보험, 영화 등 전체 개인지출에서 2/3 가량의 비중을 차지하고 있는 서비스산업 관련 지출에 대해서는 전혀 언급하지 않고 있다.
뿐만 아니라 소매판매는 인플레이션 조정을 거치지 않은 명목달러로만 측정되기 때문에, 그 결과 소비자들이 실제로 제품을 추가 구매하였는지 아니면 단순히 상품 판매 가격에 따라 추가 지불을 하였는지를 구별하기가 어렵다.
예비보고서와 최종보고서는 매우 큰 변동성을 보일 수도 있다. 
이 보고서에는 온라인 판매 수치가 별도로 분류되어 있지는 않다.

[채권 시장]
소매 판매의 급증은 소비가 활발히 이루어지고 있음을 의미하며, 이러한 경향은 경제 성장을 부추기면서 채권가격의 하락과 수익률 증가를 불러올 가능성이 크다.

[주식 시장]
건전한 소매판매의 증가는 기업의 수익과 이윤을 증가시키는데, 이 는 주식 시장에 긍정적으로 기여한다.
소매 판매의 성과가 미약할 경우 기업의 수익이 유지될 수 있을 것인지에 대해서 우려를 느끼게 될 가능성이 크다.

[외환 시장]
활발한 소비가 달러의 가치에 긍정적으로 작용하는 금리 동경을 불러일으킬 수 잇다는 점 때문에 이를 선호하고 있지만, 지나치게 활성화된 소매판매 수치는 구매 제품의 상당수가 수입품이라는 점에서 달러화의 가치에 부정적인 영향을 미치기도 한다.
무역적자를 고려하면, 수입의 금증은 모든 수입품들에 지불되어야 할 비 달러 통화에 대한 수요 역시 증가시키며, 그 결과로 달러 가치 하락을 불러올 수 있다."""
    
    @staticmethod
    def advanceRetailSales(mode='binary'):
        return (PlotEconomicIdx('RSAFS').renameColumn('사전 소매 판매 보고')
                .plot(title='사전 소매 판매 보고', mode=mode, y1_title=''))
        
    @staticmethod
    def retailSales_descr():
        return """소매 판매 보고, 최종 보고서
경제의 성과는 실질(인플레이션 조정을 거친) 성장률을 근거로 하여 측정되므로, 소매제품의 판매총액이 실제로 증가해 왔는지는 관찰하는 것이 필요하다.
소비자 물가의 월간 또는 연간증감률을 동기간 동안의 소매판매의 변화율에서 차감하는 것이다.
-> 인플레이션을 차감 한다"""

        
    @staticmethod    
    def retailSales(mode='binary'):
        return (PlotEconomicIdx('MRTSSM44X72USS').renameColumn('소매 판매 보고')
                .plot(title='소매 판매 보고', mode=mode, y1_title=''))
        
    @staticmethod
    def advanceRetailSalesExcludingMotorVehicle_descr():
        return """[사전 소매 판매 보고(자동차 제외)]
자동차 관련 카테고리는 월별로 매우 큰 병동성을 보일 수 있으며, 소매 판매의 전체 양상을 왜곡시키기도 한다.
이러한 단점을 보완하기 위해 자동차와 자동차 부품을 제외한다."""


    @staticmethod    
    def advanceRetailSalesExcludingMotorVehicle(mode='binary'):   
        return (PlotEconomicIdx('RSFSXMV').renameColumn('사전 소매 판매 보고(자동차 제외)')
                .plot( title='사전 소매 판매 보고 (자동차 제외)', mode=mode, y1_title=''))
    @staticmethod    
    def retailSalesExcludingMotorVehicle(mode='binary'):
        return (PlotEconomicIdx('MRTSSM44Y72USS').renameColumn('소매 판매 보고 (자동차 제외)')
                .plot(title='소매 판매 보고 (자동차 제외)', mode=mode, y1_title=''))
        
    @staticmethod
    def advanceRetailSales_Gasoline_descr():
        return """[소매 판매 보고(휘발유)]
지정학적 사건들과 미국 내 원유정제 능력이 운전자들의 휘발유 지출에 크나큰 영향을 미친다.
높은 휘발유 가격은 오랫동안 다른 소매판매 부문의 지출을 억제하는 역할을 해왔다."""


    @staticmethod    
    def advanceRetailSales_Gasoline(mode='binary'):
        return (PlotEconomicIdx('RSGASS').renameColumn('사전 소매 판매 보고 (휘발유)')
                .plot(title='사전 소매 판매 보고 (휘발유)', mode=mode, y1_title=''))
            
    @staticmethod    
    def retailSales_Gasoline(mode='binary'):
        return (PlotEconomicIdx('MRTSSM447USS').renameColumn('소매 판매 보고 (휘발유)')
                .plot(title='소매 판매 보고 (휘발유)', mode=mode, y1_title=''))
        
    @staticmethod    
    def advanceRetailSales_NonstoreRetailers(mode='binary'):   
        return (PlotEconomicIdx('RSNSR').renameColumn('사전 소매 판매 보고 (무인 점포)')
                .plot(title='사전 소매 판매 보고 (무인 점포)', mode=mode, y1_title=''))
        
    @staticmethod
    def retailSales_NonstoreRetailers_descr():
        return """[소매 판매 보고(무인점포)]
우편 주문 카탈로그, 인터넷, 방문판매, 자동판매기, 전화와 같은 다른 통로를 통해 얼마나 많은 물품을 구입했는지 집계한다."""

    @staticmethod    
    def retailSales_NonstoreRetailers(mode='binary'): 
        return (PlotEconomicIdx('MRTSSM454USS').renameColumn('소매 판매 보고 (무인 점포)')
                .plot(title='소매 판매 보고 (무인 점포)', mode=mode, y1_title=''))

    @staticmethod    
    def advanceRetailSales_food_drinking(mode='binary'):  
        return (PlotEconomicIdx('RSFSDP').renameColumn('사전 소매 판매 보고 (음식점 및 술집)')
                .plot(title='사전 소매 판매 보고 (음식점 및 술집)', mode=mode, y1_title=''))
        
    @staticmethod
    def retailSales_food_drinking_descr():
        return """[소매 판매 보고(음식점 및 술집)]
경기 침체기에 미국인들은 식당에서 덜 자주 먹고 값비싼 가구를 구매 하지 않는다."""


    @staticmethod    
    def retailSales_food_drinking(mode='binary'):
        return (PlotEconomicIdx('MRTSSM722USS').renameColumn('소매 판매 보고 (음식점 및 술집)')
                .plot(title='소매 판매 보고 (음식점 및 술집)', mode=mode, y1_title=''))