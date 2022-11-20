from market.macro.plotviz_economic_indicator import PlotEconomicIdx

class Productivity:
    @staticmethod
    def descr():
        return """-생산성과 단위비용 보고서-
제품과 서비스를 생산하는 노동자의 효율성 변화를 측정

[채권 시장]
다른 인플레이션 관련 지수들과 같은 반응이다.

[주식 시장]
임금과 복리후생보조금이 생산성보다 빠른 속도로 증가하면 기업의 비용이 상승하고, 이것은 기업의 이윤하락을 불러 올 수 있다.
FED가 시장에 개입하여 이 상황을 역전시키려고 할 수 있다. \
[
외환 시장]
신뢰할 만한 연관성이 없다.
"""
    @staticmethod
    def laborProductivity_descr():
        return """[비농업 경제 부문: 생산성]
전년도의 노동생산성 변화율과 한 분기에서 다음 분기로 넘어가는 시기의 노동생산성 변화율을 기록한 것이다.
노동생산성은 인플레이션에 대한 우려가 없는 상태에서 경제 성장이 빠른 속도로 있다는 것을 의미한다."""
    
    @staticmethod
    def laborProductivity(mode='binary'):
        return (PlotEconomicIdx('PRS85006091').renameColumn('비농업 경제 부문: 생산성')
                        .plot(title='비농업 경제 부문: 생산성', mode=mode, y1_title=''))
        
    @staticmethod
    def hourlyCompensation_descr():
        return """[비농업 경제 부문: 시간당 급여금]
시간당 급여금은 임금 인상 압박에 대한 단초를 제공한다.
고용비용은 기업의 비용지출에서 차지하는 비중이 매우 크다.
시간당 생산이 시간당 급여금에 비해 빠른 속도로 증가하면 단위노동비용은 하락하게 된다.
반면 시간당 급여금이 생산성보다 더 빠른 속도로 증가한다면 단위노동비용이 상승하고, 그 결과 인플레이션 발발이 불가피해진다. 
흥미로운 점은 생산성 증가가 정체되어 있는 경우 기업의 자본 투자가 오히려 증가할 수 있다."""

    @staticmethod
    def hourlyCompensation(mode='binary'):
        return (PlotEconomicIdx('PRS85006101').renameColumn('비농업 경제 부문: 시간당 급여금')
                        .plot(title='비농업 경제 부문: 시간당 급여금', mode=mode, y1_title=''))
            
    @staticmethod
    def unitLaborCosts(mode='binary'):
        return (PlotEconomicIdx('PRS85006111').renameColumn('비농업 경제 부문: 단위노동비용 및 가격')
                        .plot(title='비농업 경제 부문: 단위노동비용 및 가격', mode=mode, y1_title=''))
            
    @staticmethod
    def importPriceIndex(mode='binary'):
        return (PlotEconomicIdx('IREXFUELS').renameColumn('수입 물가 지수 변화, 에너지 제외')
                        .plot(title='수입 물가 지수 변화, 에너지 제외', mode=mode, y1_title=''))
        
    @staticmethod
    def exportPriceIndex_AllCommodities (mode='binary'):
        return (PlotEconomicIdx('IQ').renameColumn('수출 물가 지수 변화')
                        .plot(title='수출 물가 지수 변화', mode=mode, y1_title=''))
    @staticmethod
    def exportPriceIndex_NonagriculturalCommodities (mode='binary'):
        return (PlotEconomicIdx('IQEXAG').renameColumn('수출 물가 지수 변화, 비농업')
                        .plot(title='수출 물가 지수 변화, 비농업', mode=mode, y1_title=''))


    @staticmethod
    def downward_usd_descr():
        return """달러 가치가 하락하면 수입품들의 가격인상으로 이어진다.
수출 업자들은 달러가치 하락으로 인해 더 저렴하고 더 경쟁력 있는 가격으로 제품을 해외시장에 판매할 수 있게 된다.
제품의 낮은 가격은 판매를 촉진시키고 수출업자들의 수익을 증가시켜 GDP의 상승을 불러온다. """
    @staticmethod
    def upward_usd_descr():
        return """달러의 가치가 상승하면 수출업자의 수익이 감소한다.
수입업자들과 소비자들은 전에 비해 저렴해진 해외 상품의 혜택을 누릴 수 있게된다.
해외 제품과 경쟁을 하는 미국 제조업자들에게는 달러 가치의 상승에도 제품 가격을 종전과 같은 수준으로 유지할 경우 해외 제품들에 시장을 빼앗길 위험에 처하게 됨으로써 가격인하의 압박에 시달리게 된다."""