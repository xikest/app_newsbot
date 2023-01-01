
from market.stock_bs import BalanceSheet
from tools.telegram_bot.contents import Context


class SrcStocks:
      class Stock_bs:    
            def __init__(self, symbol:str):
                self._symbol=symbol

            def ratio_incomes(self):
                try:
                    yield Context(content = [BalanceSheet(self._symbol).ratio_incomes(period='yearly').plot(plot_type='bar_line_pair'),
                                            #  BalanceSheet(self._symbol).finanacing_cashflow().plot(plot_type='bar'),
                                            #  BalanceSheet(self._symbol).investing_cashflow().plot(plot_type='bar')
                                             ], dtype='img')
                except:
                    yield Context(content = ['No search'], dtype='img')
                    
            
            
    
    
    