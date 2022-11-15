from market.macro.plotviz_economic_indicator import PlotEconomicIdx

class Fed:
    @staticmethod
    def totalAssets(mode='binary'):
        return (PlotEconomicIdx('WALCL').renameColumn('Total Assets')
                        .plot(title='Total Assets', mode=mode, y1_title=''))
            
    @staticmethod
    def fed_effective_rate(mode='binary'):
        return (PlotEconomicIdx('DFF').renameColumn('Federal Funds Effective Rate')
                        .plot(title='Federal Funds Effective Rate', mode=mode, y1_title=''))
            


