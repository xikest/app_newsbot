from market.macro.plotviz_economic_indicator import PlotEconomicIdx

class PPI:
    @staticmethod
    def finalDemand(mode='binary'):
        return (PlotEconomicIdx('PPIFIS').renameColumn('Final Demand')
                        .plot(title='PPI_모든 품목, total', mode=mode, y1_title=''))
            
    @staticmethod
    def finalDemand_yoy(mode='binary'):
        return (PlotEconomicIdx('PPIFIS').renameColumn('Final Demand_yoy')
                        .plotWithMa(window=12, title='PPI_모든 품목, total, YoY', mode=mode, y1_title=''))
            
    @staticmethod
    def finalDemand_less_foods_energy(mode='binary'):
        return (PlotEconomicIdx('PPIFES').renameColumn('less_foods_energy')
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
            



