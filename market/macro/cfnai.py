from market.macro.plotviz_economic_indicator import PlotEconomicIdx

class CFNAI:
    @staticmethod
    def chicagoFedNationalActivityIndex(mode='binary'):
        return (PlotEconomicIdx('CFNAIMA3').renameColumn('시카고 연방은행_국가활동지수')
                        .plot(title='시카고 연방은행_국가활동지수_MA3', mode=mode, y1_title=''))
            
