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
            
    @staticmethod
    def m2v(mode='binary'):
        return (PlotEconomicIdx('M2V').renameColumn('Velocity of M2 Money Stock')
                        .plot(title='Velocity of M2 Money Stock', mode=mode, y1_title=''))
            
    @staticmethod
    def t10y2y(mode='binary'):
        return (PlotEconomicIdx('T10Y2Y').renameColumn('Treasury gap')
                        .plot(title='Treasury : 10-Year Minus 2-Year', mode=mode, y1_title=''))

    @staticmethod
    def t10y3m(mode='binary'):
        return (PlotEconomicIdx('T10Y3M').renameColumn('Treasury gap')
                        .plot(title='Treasury : 10-Year Minus 3-Month', mode=mode, y1_title=''))


