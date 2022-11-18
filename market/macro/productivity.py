from market.macro.plotviz_economic_indicator import PlotEconomicIdx

class Productivity:
    @staticmethod
    def laborProductivity(mode='binary'):
        return (PlotEconomicIdx('PRS85006091').renameColumn('비농업 경제 부문: 생산성')
                        .plot(title='비농업 경제 부문: 생산성', mode=mode))
            
    @staticmethod
    def hourlyCompensation(mode='binary'):
        return (PlotEconomicIdx('PRS85006101').renameColumn('비농업 경제 부문: 시간당 급여금')
                        .plot(title='비농업 경제 부문: 시간당 급여금', mode=mode))
            
    @staticmethod
    def unitLaborCosts(mode='binary'):
        return (PlotEconomicIdx('PRS85006111').renameColumn('비농업 경제 부문: 단위노동비용 및 가격')
                        .plot(title='비농업 경제 부문: 단위노동비용 및 가격', mode=mode))
            
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
    def upward_usd ():
        return "달러의 가치가 상승하면 수출업자의 수익이 감소한다. 수입업자들과 소비자들은 전에 비해 저렴해진 해외 상품의 혜택을 누릴 수 있게된다. 해외 제품과 경쟁을 하는 미국 제조업자들에게는 달러 가치의 상승에도 제품 가격을 종전과 같은 수준으로 유지할 경우 해외 제품들에 시장을 빼앗길 위험에 처하게 됨으로써 가격인하의 압박에 시달리게 된다."
    
    @staticmethod
    def downward_usd ():
        return "달러의 가치하락 달러 가치가 하락하면 수입품들의 가격인상으로 이어진다. 수출 업자들은 달러가치 하락으로 인해 더 저렴하고 더 경쟁력 있는 가격으로 제품을 해외시장에 판매할 수 있게 된다. 제품의 낮은 가격은 판매를 촉진시키고 수출업자들의 수익을 증가시켜 GDP의 상승을 불러온다."