from market.macro.plotviz_economic_indicator import PlotEconomicIdx

class DurableGoods:
    @staticmethod
    def newOrder_durableGoods(mode='binary'):
        return (PlotEconomicIdx('DGORDER').renameColumn('내구재 신규 주문')
                .plot(title='내구재 신규 주문', mode=mode))
    @staticmethod    
    def newOrder_durableGoodsExcludingTransportation(mode='binary'):
        return (PlotEconomicIdx('ADXTNO').renameColumn('운송 제외 내구재 신규 주문')
                .plot(title='운송 제외 내구재 신규 주문', mode=mode))
        
    @staticmethod    
    def newOrder_durableGoodsExcludingDefence(mode='binary'):
        return (PlotEconomicIdx('AMTUNO').renameColumn('방산재 제외 내구재 신규 주문')
                .plot(title='방산재 제외 내구재 신규 주문', mode=mode))
    
# #### 방산재 및 운송을 제외한 신규 내구재 주문, 

# 가계의 임의 소비지출 중 15% 가량이 내구재 구매와 관련된 것으로서, 경제 상황에 대한 소비자들의 불안감이 커지면 내구재에 대한 소비지출이 가장 먼저 타격을 받게 된다. \
# 신규 주문의 회복은 소비자들이 지출을 재개할 수 있을 정도로 재정상태와 고용전망이 안정적이며, 더 나아가 산업부문과 경제 전반에 대해서 충분히 만족하고 있다는 사실을 의미한다.

#     tranportation = load_data_from_fred('DGORDER').values - load_data_from_fred('ADXTNO').values
# df = pd.DataFrame(load_data_from_fred('AMTUNO').values- tranportation,
#              index =load_data_from_fred('AMTUNO').index,
#              columns = ["방산재 및 운송을 제외한 신규 내구재 주문"])
# plot_df(df)
    
    
        
    @staticmethod    
    def primaryMetals(mode='binary'):
        return (PlotEconomicIdx('A31SNO').renameColumn('1차 금속 신규 주문')
                .plot(title='1차 금속 신규 주문', mode=mode))
    @staticmethod    
    def capitalGoods(mode='binary'):
        return (PlotEconomicIdx('ATCGNO').renameColumn('자본재 신규 주문')
                .plot(title='자본재 신규 주문', mode=mode))
    @staticmethod    
    def capitalGoodsExcludingDefence(mode='binary'):
        return (PlotEconomicIdx('NEWORDER').renameColumn('비군수용 자본재(항공기 제외) 신규 주문')
                .plot(title='비군수용 자본재(항공기 제외) 신규 주문', mode=mode))
    @staticmethod    
    def UnfilledOrdersDurableGoods(mode='binary'):
        return (PlotEconomicIdx('AMDMUO').renameColumn('수주 잔량')
                .plot(title='수주 잔량', mode=mode, y1_title=''))
    