from market.macro.plotviz_economic_indicator import PlotEconomicIdx

class PCE:
    @staticmethod
    def personalIncome(mode='binary'):
        return (PlotEconomicIdx('PI').renameColumn('개인 소득')
                .plot(title='개인 소득', mode=mode))
    @staticmethod    
    def realDisposablePersonalIncome(mode='binary'):
        return (PlotEconomicIdx('DSPIC96').renameColumn('실질 가처분 소득')
                .plot(title='실질 가처분 소득', mode=mode))
        
    @staticmethod    
    def personaloutlays(mode='binary'):
        return (PlotEconomicIdx('A068RC1').renameColumn('개인소비지출, 이자지출, 개인 이전지출')
                .plot(title='개인 경비', mode=mode))

    @staticmethod    
    def pce(mode='binary'):
        return (PlotEconomicIdx('PCE').renameColumn('개인 소비지출')
                .plot(title='PCE 개인 소비지출', mode=mode))
    @staticmethod    
    def personalInterestPayments(mode='binary'):
        return (PlotEconomicIdx('B069RC1').renameColumn('이자 지출')
                .plot(title='이자 지출', mode=mode))
       ## 개인 이자 부담// 개인 가처분 소득 
    # @staticmethod    
    # def personalInterestPayments(mode='binary'):
    #     return (PlotEconomicIdx('B069RC1').renameColumn('이자 지출')
    #             .plot_div(title='이자 지출', mode=mode, y1_title=''))

    # plot_div(self, colKey1:str, colKey2:str, column_name:str='0',title:str=' ',  mode:str='binary', y1_title:str='')
    
    
    def expenditures_durable(mode='binary'):
        return (PlotEconomicIdx('PCEDG').renameColumn('내구재 지출')
                .plot(title='내구재 지출', mode=mode))
    
    def  real_pce(mode='binary'):
        return (PlotEconomicIdx('PCEC96').renameColumn('실질 개인 소비지출')
                .plot(title='PCE 실질 개인 소비지출', mode=mode, y1_title=''))    
    
    def  pce_PriceIndex(mode='binary'):
        return (PlotEconomicIdx('PCEPI').renameColumn('PCE물가지수')
                .plot(title='PCE물가지수', mode=mode, y1_title=''))    
    