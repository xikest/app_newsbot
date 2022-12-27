from pandas_datareader import data as pdr
import yfinance as yf

from datetime import datetime
import numpy as np
from tools.graph_plot.plotviz import PlotViz
from dateutil.relativedelta import relativedelta
from tools.time.time import Periods

yf.pdr_override() # <== that's all it takes :-)


def market_symbols():
  return {'XLV':'Health Care', 'XLB': 'Materials', 'XLP' :'Consumer Staples', 'XLF': 'Financial',
          'XLI':'Industrial', 'XLC' : 'Communication Services', 'XLK' : 'Technology',
          'XLU': 'Utilities', 'XLY':'Consumer Discretionary' ,'XLE': 'Energy',
          'VNQ':'Real Estate',
          'TLT': 'Treseary',
          'GLD':'Gold'}  
  
def calculate_sharpe_ratio(df):
  return df.mean() /df.std()

def to_text_as_weeks(idx, format='%Y-%m, %Ww'):
  return idx.strftime(format)

def to_text_as_month(idx, format='%Y-%mm'):
  return idx.strftime(format)



class MarketPattern:
  def __init__(self, period='w'):
    start, end = Periods.make_period(periods=1)
    (self._prepare_dataset(symbols = market_symbols(), 
                              start=start,end=end)
         ._sharp_ratio(period))
    self.title=f'Market pattern_{period}'
    pass

  def _prepare_dataset(self, symbols, start, end):
    
    dataset = pdr.get_data_yahoo(list(symbols.keys()), 'yahoo', start=start, end=end)['Adj Close']
    self.dataset = dataset.rename(columns=symbols)
    return self


  def _sharp_ratio(self, period):
    heatmap = (calculate_sharpe_ratio(self.dataset.pct_change(1).resample(period))
                                                .apply(lambda sharp: np.where(sharp>0, 1,0)))
    if period == 'w': heatmap.index = heatmap.index.map(to_text_as_weeks)
    elif period == 'm':  heatmap.index = heatmap.index.map(to_text_as_month)
    self.heatmap = heatmap.sort_index(ascending=False)
    return self

  def _plot(self, mode='binary'):
    fig = PlotViz(self.heatmap).heatmap().update_layout(title= self.title, width=400, height=1000).update_yaxes().update_xaxes()
    if mode == 'binary': return fig.trx_to_byte()
    elif mode == 'show': return fig.show()
  
  @staticmethod
  def plot(mode='binary', period='w'):
    return MarketPattern(period)._plot(mode)