from market.macro.plotviz_economic_indicator import PlotEconomicIdx

class PPI:
    
    @staticmethod
    def descr():
        return """
        생산자 물가지수: 원자재
        최초로 시장에 진입하는 원자재의 가격을 반영한다.
        식품재의 예로는 밀, 소, 콩 등을 꼽을 수 있으며, 비식품 원자재에는 석탄, 원유, 모래, 원목등이 포함된다.
        이러한 1차 상품들의 가격 변화는 일반적으로 가뭄, 동물의 질병, 지정학적 요인들로 인한 공급 변화에 따라 좌우된다.
        생산의 초기 단계에 발생하는 가격의 급등은 중간 단계에까지 이어지는 경향이 있다.

        생산자 물가지수: 중간재
        최종 제품으로 완성되기 전 제품으로의 전환 단계에 있는 상품의 가격을 반영한다. 밀가루, 특정 동물의 사료, 종이, 자동차 부품, 가죽, 직물 등이 중간재에 포함된다.
        중간 단계에서의 가격 변화는 최종 단계로 이어지기도 한다.

        생산자 물가지수: 최종재
        최종재는 의류와 가구, 자동차, 육류, 휘발유, 연료유 등으로 구성되어 있다.
        최종재는 소매업자가 구매하는 제품이며, 소매업자 지불가격이 소비자에게 직접적인 영향을 미칠 수 있다는 점 때문에 이 단계에 나타나는 인플레이션은 매우 심각하게 받아들여진다.

        최종재 가격지수와 소비자물가 사이의 연관성은 중요하게 여겨지고 있는데, 이 두 지수는 월단위로는 각각 다른 움직임을 보이지만 보통 6개월에서 9개월 사이의 장기간 동안에는 나란히 움직이는 경향이 있다. \

        서비스 부문의 가격이 대부분의 경우 PPI에 포함되지 않는 반면, CPI에서는 반 이상을 차지한다.
        '소비재'는 최종재 물가지수의 75%에 해당한다. 소비재 가격의 급격한 상승이 PPI에서 포착된다면, CPI 역시 상승 압력에 시달리게 될 가능성이 커진다.
        """
    
    @staticmethod
    def finalDemand(mode='binary'):
        return (PlotEconomicIdx('PPIFIS').renameColumn('Final Demand')
                        .plot(title='PPI_Final Demand, total', mode=mode, y1_title=''))
            
    @staticmethod
    def finalDemand_yoy(mode='binary'):
        return (PlotEconomicIdx('PPIFIS').renameColumn('Final Demand, YoY')
                        .plotWithMa(window=12, title='PPI_Final Demand, total, YoY', mode=mode, y1_title=''))
            
    @staticmethod
    def finalDemand_less_foods_energy(mode='binary'):
        return (PlotEconomicIdx('PPIFES').renameColumn('식량과 에너지 제외')
                        .plot(title='PPI_모든 품목, 식량과 에너지 제외', mode=mode, y1_title=''))
            
    @staticmethod
    def finalDemand_less_foods_energy_yoy(mode='binary'):
        return (PlotEconomicIdx('PPIFES').renameColumn('less_foods_energy_yoy')
                        .plotWithMa(window=12, title='PPI_모든 품목, 식량과 에너지 제외_yoy', mode=mode, y1_title=''))

    @staticmethod
    def  processed_goods_Intermediate_yoy(mode='binary'):
        return (PlotEconomicIdx('WPSID61').renameColumn('중간재 연간 변화율')
                        .plotWithMa(window=12,title='중간재에 나타난 월간 PPI의 연간 변화율', mode=mode, y1_title=''))
            
    @staticmethod
    def processed_goods_Intermediate_core(mode='binary'):
        return (PlotEconomicIdx('WPSID69115').renameColumn('중간재 변화율, 식량과 에너지 제외 (core)')
                        .plot( title='중간재에 나타난 월간 PPI 변화율, 식량과 에너지 제외 (core)', mode=mode, y1_title=''))
            
    @staticmethod
    def unprocessed_goods_Intermediate_yoy(mode='binary'):
        return (PlotEconomicIdx('WPSID69216').renameColumn('원자재 연간 변화율')
                        .plotWithMa(window=12,title='원자재 생산에 나타난 월간 PPI의 연간 변화율', mode=mode, y1_title=''))
            
    @staticmethod
    def unprocessed_goods_Intermediate_core(mode='binary'):
        return (PlotEconomicIdx('WPSID69115').renameColumn('원자재 변화율,식량과 에너지 제외 (core)')
                        .plot( title='원자재 생산에 나타난 월간 PPI의 변화율,식량과 에너지 제외 (core)', mode=mode, y1_title=''))
            



