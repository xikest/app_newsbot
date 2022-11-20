from market.macro.plotviz_economic_indicator import PlotEconomicIdx

class GDP:
    @staticmethod
    def descr():
        return """-GDP, 소비자가 고용, 경제 그리고 소비에 대해 어떻게 느끼고 있는지를 측정-

[채권 시장]
인플레이션 압력의 증가와 이와 동반해 나타나는 강력한 GDP의 성장률은 FED가 개입하여 단기금리를 인상함으로써 경기의 긴축을 유도할 것이라는 우려를 확산시킨다.

[주식 시장]
경제 활동이 몇 분기 동안 3.5% 이상 계속 성장했다면 주식투자자들 마저도 가격 인상에 대한 불안을 느끼기 시작할 가능성이 있다.
높은 인플레이션은 가계의 구매력을 저하시키고 이자율 인상의 원인으로 작용하기도 한다. 

[외환 시장]
만약 FED가 단기금리를 인상해 인플레이션을 재빨리 조정한다면, 미국중앙은행이 가격 압력에 대한 발 빠른 대응을 하고 있다는 평가와 함께 달러의 가치가 높아질 수 있다.
만약 인플레이션이 가속화되어 지속적으로 높은 수준을 유지한다면, 미국의 경쟁력은 하락할 것이며 이에 따라 미국의 해외무역수지가 악화될 수 밖에 없다. 이것은 달러의 가치하락으로 이어진다."""
    
    @staticmethod
    def gdp_descr():
        return """[Gross Domestic Product (GDP)]
미국에서 생산된 모든 상품과 서비스의 최종 가치를 일컫는다."""

    @staticmethod
    def gdp(mode='binary'):
        return (PlotEconomicIdx('GDP').renameColumn('GDP')
                .plot(title='GDP', mode=mode, y1_title=''))
        
        
    @staticmethod
    def pce_descr():
        return """[개인 소비 지출, PCE]
소비자가 얼마나 지출하였는가
상품과 서비스에 대한 소비자의 총 지출을 의미, GDP의 70%에 해당 한다. 
소비자들은 무엇에 지출하는가는 세개의 하위 구성요소에서 찾아야 한다."""
    
    @staticmethod    
    def pce(mode='binary'):
        return (PlotEconomicIdx('PCEC').renameColumn('개인 소비 지출')
                .plot(title='개인 소비 지출', mode=mode, y1_title=''))

    @staticmethod
    def durableGoods_descr():
        return """[PCE: 내구재]
냉장고, TV, 자동차, 가구 등 평균 수명이 3년 이상인 고가품들을 말한다.
전체 소비지출 중 15%를 차지한다.
내구재에 대한 지출은 소비자의 소득 및 심리의 변화에 극도로 민감하게 반응한다.
일반적으로 내구재들은 고가품인 경우가 많으며 소비자가 종종 신용대출을 통해 구매하기 때문에, 내구재에 대한 지출여부는 이자율의 변화에 민감할 수 밖에 없다. \
        """
           

    @staticmethod    
    def durableGoods(mode='binary'):
        return (PlotEconomicIdx('PCDG').renameColumn('내구재')
                .plot(title='내구재', mode=mode, y1_title=''))
        
    @staticmethod
    def non_durableGoods_descr():
        return """[PCE: 비내구재]
야채, 스웨터, 신발처럼 평균 수명이 3년 이하인 상품들이 여기에 속한다.
전체 소비지출에서 25% 정도의 비중을 차지한다.
경기호황이나 불황 여부에 관계 없이 비교적 안정적인 증가세를 보이는데, 일상생활의 일부분을 차지하는 이러한 상품들에 대한 지출은 쉽사리 연기될 수 없기 때문이다.
(주식 투자자자들이 경기 침체기에 비내구재 생산기업들의 주식을 매수하고 내구재 생산기업들의 주식을 매도 하는 이유이기도 하다)
""" 

    @staticmethod    
    def non_durableGoods(mode='binary'):
        return (PlotEconomicIdx('PCND').renameColumn('비내구재')
                .plot(title='비내구재', mode=mode, y1_title=''))
        
    @staticmethod
    def services_descr():
        return """[PCE: 서비스]
병원이나 치과 진료, 자동차 및 주택보험, 이발, 주택담보대출, 운송, 법률비용 등의 서비스와 관련 된다.
소비지출의 절반 이상을 차지한다.
서비스에 대한 지출을 소득이 감소세를 보이는 와중에도 크게 감소하지 않고 일정수준으로 유지되는 경향이 있다."""  
        
    @staticmethod    
    def services(mode='binary'):
        return (PlotEconomicIdx('PCESV').renameColumn('서비스')
                .plot(title='서비스', mode=mode, y1_title=''))
        
    @staticmethod
    def domesticInvestment_descr():
        return """[민간 국내 총투자, Gross Private Domestic Investment]
기업들이 공장, 설비 및 건설 등에 얼마나 투자하였는가
GDP의 15% 가량을 차지하고 있다.
경제가 지속적인 성장세를 보일 것이라는 예측은 기업 지출의 증가로 이어지지만, 경게 활동이 둔화될 것이라는 전망에서는 기업 지출이 급격히 하락할 수 있다. """  
   
    @staticmethod
    def domesticInvestment(mode='binary'):
        return (PlotEconomicIdx('GPDI').renameColumn('민간 국내 총투자')
                .plot(title='민간 국내 총투자', mode=mode, y1_title=''))    
    
    @staticmethod
    def fixedInvestment_descr():
        return """[고정 투자, Fixed Private Investment]
전체 기업 지출 중 가장 큰 부분을 차지한다.
이것은 비주거용 지출(사무용 건물, 창고, 컴퓨터 장비 및 소프트웨어, 기계설비, 운송장비)과 주거용 지출(단독 주택과 공동 주택 건설)로 분류할 수 있다.
주거용 지출은 전체 투자 지출의 1/3에 가까운 비중을 차지하고 있다.
주거용 지출과 비주거용 투자지출 모두 경기에 극도로 민감한 반응을 보인다."""    
    
    @staticmethod
    def  fixedInvestment(mode='binary'):
        return (PlotEconomicIdx('FPI').renameColumn('고정 투자')
                .plot(title='고정 투자', mode=mode, y1_title=''))    

    
    @staticmethod
    def changeInventories_descr():
        return """[민간 재고의 변화]
GDP는 미국 경제 내에서 생산되는 모든 상품 및 서비스의 가치를 반영한다.
기업들은 종종 실제로 팔리는 것보다 더 많은 상품을 생산하기도 하며, 이중 팔리지 않고 남겨진 상품들은 재고의 일부로 분류된다.
GDP는 총수요와 재고 변화의 합이라 할 수 있다.
재고는 경제의 전환기에 급변할 수 있다.
재고는 경제성장의 갑작스런 중단을 불러오는 계기로 작용할 수 있다. 하지만 과고판매, 특별할인, 기타 쇼핑 인센티브 부여 등으로 판매 촉진 활동을 통해 시간이 지남에 따라 재고 수준은 점차적으로 감소하게 될 것이다.
소비 수요가 회복되고 상품 구매가 다시 늘어나면, 공장들은 고갈된 재고의 보충을 위해 상산을 증가시킬 것이고, 이와 같은 과정은 경제가 회복 국면으로 진입하도록 보조하는 역할을 한다."""     
    
    @staticmethod
    def  changeInventories(mode='binary'):
        return (PlotEconomicIdx('CBI').renameColumn('민간 재고의 변화')
                .plot(title='민간 재고의 변화', mode=mode, y1_title='', secondary_y=False))   
    
    @staticmethod
    def netExports_descr():
        return """[순수출, 미국의 해외 수출액과 수입액의 차이]
GDP에서 수출이 차지하는 비중은 10% 정도이고, 수입은 16% 정도이다.
GDP의 1/4가 국제무역과 밀접한 연관성을 보이고 있다.
해외에 수출되는 미국산 상품과 서비스는 미국 내에서 생산된다는 이유로 GDP에 포함된다.
해외 상품과 서비스 구매에 따른 지출은 GDP에서 제외 되는데, 미국 외 다른 나라의 생산품을 구매함으로써 수요를 충족시킨다는 사실 때문이다.
순수출은 GDP 계정에 수출을 더한 수치와 GDP 계정에서 수입을 뺀 수치 사이의 차이이다.
1970년대 이래로 순 수출이 마이너스를 기록하고 있는데, 이것은 30년 이상 동안 미국의 GDP의 성장률을 끌어내린 원인 중 하나로 해석된다."""
    
    @staticmethod
    def netExports(mode='binary'):
        return (PlotEconomicIdx('NETEXP').renameColumn('순수출')
                .plot(title='순수출', mode=mode, y1_title=''))  
          
    @staticmethod
    def governmentConsumptionExpenditures_GrossInvestment_descr():
        return """[정부 소비지출과 총투자, 연방정부, 주정부, 지방정부가 지출 및 투자한 액수]
GDP에서 18% 가량을 차지한다.
전체 정부 지출에서 연방정부지출의 비중이 1/3에 해당하며, 나머지를 주정부와 지방정부의 지출이 차지하고 있다.
연방 정부 지출은 군수용 지출(군사장비, 군인 및 군대에 고용된 민간종사자의 급여 등)과 비군수용지출(고속도로 건설, 미국 항공우주국, 공원 서비스 공단, 국방부 제외 연방직원의 급여 등)로 분류 되어 있다.
주정부와 지방정부는 전체 공적지출과 투자(도로건설, 경찰, 소방장비 등)에서 2/3의 비중을 차지하고 있다.
경기 둔화는 고용 보험 등에 지불되는 공적 지출의 확대를 불러옴으로써 주정부나 지방정부의 예산을 고갈시킬 수 있으며, 정부의 조세수입도 감소를 피할 수 없게 될 것이다.
"""
    @staticmethod
    def  governmentConsumptionExpenditures_GrossInvestment(mode='binary'):
        return (PlotEconomicIdx('GCE').renameColumn('정부 소비지출과 총투자')
                .plot(title='정부 소비지출과 총투자', mode=mode, y1_title=''))    

    @staticmethod
    def finalSalesofDomesticProduct_descr():
        return """[국내생산최종판매, Final Sales of Domestic Product]
경제 활동이 얼마나 활발히 이루어지고 있는지를 파악한다.
국내생산최종판매는 GDP에서 재고변화를 제외한 수치이기 때문에 미국산 상품과 서비스의 실수요를 측정하는 바로미터로 여겨진다.
미국 소비자들뿐만 아니라 해외 소비자들에 대한 판매도 포함한다는 단점이 있다. 미국 내에서의 수요만 파악하기 위해서는 국내총구매를 보아야 한다."""
    
    @staticmethod
    def  finalSalesofDomesticProduct(mode='binary'):
        return (PlotEconomicIdx('FINSAL').renameColumn('국내생산최종판매')
                .plot(title='국내생산최종판매', mode=mode, y1_title=''))    

    @staticmethod
    def grossDomesticPurchases_descr():
        return """[국내총구매, Gross Domestic Purchases]
미국 내에서 또는 해외에서 생산된 상품에 대한 미국 소비자와 기업의 구매를 모두 합산한 것이다.
국내총구매는 미국 내에서의 실수요를 파악하기 위한 지표이기 때문에 수출을 제외하는 반면 해외수입을 그 대상에 포함시킨다.
"""

    @staticmethod
    def  grossDomesticPurchases(mode='binary'):
        return (PlotEconomicIdx('GDB').renameColumn('국내총구매')
                .plot(title='국내총구매', mode=mode, y1_title=''))    
        
    @staticmethod
    def gDPImplicitPriceDeflator_descr():
        return """[GDP Implicit Price Deflator]
미국 내에서 생산된 상품과 서비스의 가격 변화를 측정한다"""

    @staticmethod
    def  gDPImplicitPriceDeflator(mode='binary'):
        return (PlotEconomicIdx('A191RI1Q225SBEA').renameColumn('GDP Implicit Price Deflator')
                .plot(title='GDP Implicit Price Deflator', mode=mode, y1_title=''))  
          
    @staticmethod
    def gNPImplicitPriceDeflator_descr():
        return """[GNP Implicit Price Deflator]
해외수입품을 포함한 모든 상품의 구매가격변화를 측정한다.
만약 오일가격(수입품)이 급등하면 오일가격의 증가분은 국내총구매 가격지수에 완전히 편입되며, GDP 인플레이션 지수와 차별화 된다.
수입 가격의 급등은 오일가격의 급상승 또는 달러가치의 폭락으로 인해 발생하며, 수입 가격이 더욱 상승하는 현상으로 이어진다.
이러한 경우에는 국내총구매 디플레이터가 인플레이션을 더 정확히 측정할 수 있다."""

    @staticmethod
    def  gNPImplicitPriceDeflator(mode='binary'):
        return (PlotEconomicIdx('A001RI1Q225SBEA').renameColumn('GNP Implicit Price Deflator')
                .plot(title='GNP Implicit Price Deflator', mode=mode, y1_title=''))    
        
    @staticmethod
    def pCeDeflator_descr():
        return """[개인소비지출(PCE) 디플레이터]
미국 내에서 생산된 상품과 서비스의 가격 변화를 측정한다"""
        
    @staticmethod
    def pCeDeflator(mode='binary'):
        return (PlotEconomicIdx('DPCERD3Q086SBEA').renameColumn('PCE Implicit Price Deflator')
                .plot(title='PCE Implicit Price Deflator', mode=mode, y1_title=''))    
        
    @staticmethod
    def realGrossDomesticProduct_descr():
        return """[실질 GDP 변화율(직전 분기 대비)]
매년 3% 의 성장이 필요하다
노동력 증가 1% +생산성 증가 2%
연속 분기 3.5% 이상의 성장은 과잉 노동력과 물적 자원이 고갈되고 인플레이션 압력이 발생하여 FED의 개입을 불러온다"""
        
    @staticmethod
    def realGrossDomesticProduct(mode='binary'):
        return (PlotEconomicIdx('A191RL1Q225SBEA').renameColumn('실질 GDP 변화율(직전 분기 대비)')
                .plot(title='실질 GDP 변화율(직전 분기 대비)', mode=mode, y1_title=''))    
        
        
    @staticmethod
    def realNetExportsofGoodsandServices_descr():
        return """[실질 상품 및 서비스 순 수출GDP 변화량]
미국 무역 규모는 전체 경제 활동의 거의 1/3에 달한다.
수출입량에서 나타나는 아주 작은 변화가 국내총생산의 증가에 막대한 영향을 줄 수 있다."""
        
    @staticmethod
    def realNetExportsofGoodsandServices(mode='binary'):
        return (PlotEconomicIdx('NETEXC').renameColumn('실질 상품 및 서비스 순 수출GDP 변화량')
                .plot(title='실질 상품 및 서비스 순 수출GDP 변화량', mode=mode, y1_title=''))    
        
        
    @staticmethod
    def realFinalSalestoPrivateDomesticPurchasers_descr():
        return """[국내 생산 최종 매출]
이 지표는 재고와 관련된 내용을 제외시키는 대신 소비자, 기업, 정부의 실제 지출액을 관찰한다.
경제에서 발생하는 수요를 보다 정확하게 보여준다.
장기간 동안 최종 매출의 증가율이 GDP의 증가율보다 낮은 수준으로 하락한다면, 구매에 대한 소비자들의 현재 관심 수준보다 더 많은 상품을 기업들이 생산해 왔음을 암시한다.
역으로, 최종 매출이 GDP보다 빠른 증가율을 보인다면 기업들은 소비자들의 높은 수요를 충족 시키기 위해 생산을 가속할 것이며, 향후 경제 성장이 예고되기도 한다."""
        
    @staticmethod
    def realFinalSalestoPrivateDomesticPurchasers(mode='binary'):
        return (PlotEconomicIdx('PB0000031Q225SBEA').renameColumn('국내 생산 최종 매출')
                .plot(title='국내 생산 최종 매출', mode=mode, y1_title='', secondary_y=False))   
        
        
    @staticmethod
    def rGDPdivRealFinalSales_descr():
        return """[Real GDP / Real Final Sales to Private Domestic Purchasers]"""
        
    @staticmethod
    def rGDPdivRealFinalSales(mode='binary'):
        return (PlotEconomicIdx('LB0000031Q020SBEA').div('GDPC1').renameColumn('실질GDP / 실제 최종 판매')
                .plot(title='실질GDP / 실제 최종 판매', mode=mode, y1_title='Pecent (%)', secondary_y=False))   
        
    @staticmethod
    def gDPdivGNP_descr():
        return """[GDP / GNP]
GDP는 미국계인지 외국계인지 여부에 상관없이 미국 내에서 운영되는 전체 기업들에 의해 생산된 모든 상품과 서비스를 포함한다.
반면 GNP는 공장과 사무실이 전 세계의 어느 곳에 위치하고 있는지에 상관없이 미국 소유의 기업들에 의해 생상된 상품과 서비스만을 대상으로 삼는다.
GDP는 미국 내 생산량에 대한 뛰어난 지표이며 미국의 고용 활동과 더 밀접한 관련을 맺고 있다."""
        
    @staticmethod
    def gDPdivGNP(mode='binary'):
        return (PlotEconomicIdx('GDP').div('GNP').renameColumn('GDP / GNP')
                .plot(title='GDP / GNP', mode=mode,  y1_title='Pecent (%)', secondary_y=False))   
        
        
    @staticmethod
    def realGDP_Computers_descr():
        return """[실질 GDP: 컴퓨터 매출]
컴퓨터 최종 매출은 첨단 기술 상품에 대한 기업의 지출을 반영한다.
경제 상황에 대해 낙관적인 전망과 투자에 따른 수익 창출에 충분한 확인이 존재할 때 증가하는 경향이 있다."""
        
    @staticmethod
    def realGDP_Computers(mode='binary'):
        return (PlotEconomicIdx('BB01RL1Q225SBEA').renameColumn('실질 GDP: 컴퓨터 매출')
                .plot(title='실질 GDP: 컴퓨터 매출', mode=mode, secondary_y=False))   
        
    @staticmethod
    def realGDP_Vehicle_descr():
        return """[실질 GDP: 자동차 매출]
자동차 산업은 고무, 유리, 철강, 전자 상품, 섬유 등을 포함한 수천 개의 자재 공급에 의존하고 있기 때문에 자동차 생산활동의 변화는 수많은 부속 산업의 흥망성쇠에 영향을 끼칠 수 있다"""
        
    @staticmethod
    def realGDP_Vehicle(mode='binary'):
        return (PlotEconomicIdx('A953RL1Q225SBEA').renameColumn('실질 GDP: 자동차 매출')
                .plot(title='실질 GDP: 자동차 매출', mode=mode, secondary_y=False))     
        
        
    @staticmethod
    def rPCE_excludingfood_energy_descr():
        return """[실질 PCE: 음식, 에너지 제외]
식량과 에너지는 가계에서 매우 필수적이고 일상적으로 요구되는 지출 대상으로 제외 한다.
일반적으로 FED는 1~2% 범위 내에서 유지하는 것을 선호한다.
"""
    def rPCE_excludingfood_energy(mode='binary'):
        return (PlotEconomicIdx('DPCCRAM1M225NBEA').renameColumn('실질 PCE: 음식, 에너지 제외')
                .plot(title='실질 PCE: 음식, 에너지 제외', mode=mode, secondary_y=False))    