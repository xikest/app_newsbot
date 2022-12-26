
from market.stock_bs import BalanceSheet
from tools.telegram_bot.contents import Context


class SrcStocks:
      class Stock_bs:    
            def __init__(self, symbol:str):
                self._symbol=symbol

            def ratio_incomes(self):
                try:
                    yield Context(content = [BalanceSheet(self._symbol).ratio_incomes().plot(plot_type='bar_line_pair'),
                                             BalanceSheet(self._symbol).cashflow().plot(plot_type='bar_line_pair')], dtype='img')
                except:
                    yield Context(content = ['No search'], dtype='img')
                    
            
            
    
    
    