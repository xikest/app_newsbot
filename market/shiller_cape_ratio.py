import pandas as pd
from tools.graph_plot.plotviz import PlotViz
from tools.quandl.qndl import Qdl
from datetime import datetime
from tools.graph_plot.basic_plot import PlotvizBasic

def DatetimeToDate(idx: datetime.timestamp) -> datetime.date:
  return idx.date()

def qndl_keys_multpl():
    return {'SHILLER_PE_RATIO_MONTH' :'Shiller PE Ratio by Month',
              'SP500_DIV_YIELD_MONTH' : 'S&P 500 Dividend Yield by Month',
              'SP500_EARNINGS_YIELD_MONTH' : 'S&P 500 Earnings Yield by Month',
              'SP500_REAL_PRICE_MONTH' : 'S&P 500 Real Price by Month',
              'SP500_PE_RATIO_MONTH' : 'S&P 500 PE Ratio by Month'}

class ShillerRatio:
  def __init__(self, years_from_today=10):
    self._prepare_dataset_(years_from_today)
    pass
    
  def _prepare_dataset_(self, years_from_today):
    self._raw_df=Qdl('MULTPL', list(qndl_keys_multpl().keys()), years_from_today).rename(qndl_keys_multpl()).data
    self._df = self._raw_df.ffill().resample('MS').last()  #qndl에서 기본 값으로 10년 기간 데이터를 받아옴, 기본 값 사용
    # self.df.index = self.df.index.map(DatetimeToDate)

    return self

  @staticmethod
  def plot(reference='Shiller PE Ratio by Month', compare_with='S&P 500 Real Price by Month', mode='binary'):
      return  ShillerRatio()._plot(reference, compare_with, mode)
    
    #
    
  def _plot(self, compare_with='S&P 500 Real Price by Month', reference='Shiller PE Ratio by Month',  mode='binary'):
    fig = (PlotViz(self._df).line(col_idx=reference)
                               .line(col_idx=compare_with, secondary_y=True)
                               .add_hline(y=26, annotation_text='CAPE:26',  annotation_position= 'bottom left', annotation_font_color='black')
                               .add_hrect(y0=20,y1=32)
                               .add_annotation( pos='max').add_annotation( pos='min').add_annotation( pos='recent')
                               .add_annotation( pos='max', col_idx=compare_with, showarrow=False, yref='y2').add_annotation( pos='min', col_idx=compare_with, showarrow=False,  yref='y2').add_annotation( pos='recent', col_idx=compare_with,showarrow=False, yref='y2')
                               .update_layout(title= f'Shiller PE Ratio Vs {compare_with}', width=500, height=700)
                               .update_yaxes(title_text=reference).update_yaxes(title_text=compare_with, secondary_y=True)
                               .update_xaxes())
    if mode == 'binary': return fig.trx_to_byte()
    elif mode == 'show': return fig.show()
 
  @property
  def dataset_columns(self):
    return pd.DataFrame(qndl_keys_multpl(), index=['name']).T
  
  @property
  def dataset(self):
    return self._df