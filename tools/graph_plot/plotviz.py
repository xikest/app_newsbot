from plotly.subplots import make_subplots
# import plotly.express as px
# import pandas as pd
from datetime import datetime
import plotly.io as pio
from .plot_func import make_trace, check_instance_for_df
# from typing import Union

# import numpy as np
# from numpy import ndarray

# Templates configuration
# -----------------------
#     Default template: 'plotly'
#     Available templates:
#         ['ggplot2', 'seaborn', 'simple_white', 'plotly',
#          'plotly_white', 'plotly_dark', 'presentation', 'xgridoff',
#          'ygridoff', 'gridon', 'none']



class PlotViz:
  
  def __init__(self, df, theme='plotly_white'):
    pio.templates.default = theme
    self.df = check_instance_for_df(df).ffill() 
    self.fig = make_subplots(specs=[[{"secondary_y": True}]])
    pass     

            
            
            
        
  def bar(self, name=None, pct_change=False, col_idx:int or str=0,  secondary_y=False, **kwarg):
    self.fig.add_trace(make_trace(df=self.df, mode='bar', name=name, pct_change=pct_change, col_idx=col_idx, **kwarg), secondary_y=secondary_y)
    return self

  def box(self, name=None, pct_change=False, col_idx:int or str=0,  secondary_y=False, **kwarg):
    self.fig.add_trace(make_trace(df=self.df, mode='box', name=name, pct_change=pct_change, col_idx=col_idx, **kwarg), secondary_y=secondary_y)
    return self

  def hist(self, name=None, pct_change=False, col_idx:int or str=0,  secondary_y=False, **kwarg):
    self.fig.add_trace(make_trace(df=self.df, mode='hist', name=name, pct_change=pct_change, col_idx=col_idx, **kwarg), secondary_y=secondary_y)
    return self

  def scatter(self, name=None, pct_change=False, col_idx:int or str=0,  secondary_y=False, **kwarg):
    self.fig.add_trace(make_trace(df=self.df, mode='scatter', name=name, pct_change=pct_change, col_idx=col_idx, **kwarg), secondary_y=secondary_y)
    return self

  def line(self, name=None, pct_change=False, col_idx:int or str=0,  secondary_y=False, **kwarg):
    self.fig.add_trace(make_trace(df=self.df, mode='line', name=name, pct_change=pct_change, col_idx=col_idx, **kwarg), secondary_y=secondary_y)
    return self
  
  def heatmap(self, **kwarg):
    self.fig.add_trace(make_trace(df=self.df, mode='heatmap', **kwarg), secondary_y=False)
    self.fig.update_traces(dict(showscale=False, coloraxis=None,  colorscale='Blues'), selector={'type':'heatmap'})
    return self
  
  # ====================================================================================================
  # 지시선 그리기
  # annotation_text='text'
  # annotation_position= 'bottom right', 'top left'
  # annotation__font_color='blue'
  # annotation = dict(font_size=20, ,font_family='Times New Roman'  
  # line_dash='dot', 'dash'
  # ====================================================================================================   
  
  def add_hline(self, y, line_width= 1, line_dash='dot', line_color='black', **kwargs):    
    self.fig.add_hline(y=y, line_width= line_width, line_dash=line_dash, line_color=line_color, **kwargs)
    return self
  
  def add_vline(self, x, line_width= 1, line_dash='dash', line_color='red', **kwargs):
    self.fig.add_vline(x=x, line_width= line_width, line_dash=line_dash, line_color=line_color, **kwargs)
    return self
  
  def add_hrect(self, y0, y1, line_width= 0, fillcolor='blue', opacity=0.2,**kwargs):
    self.fig.add_hrect(y0=y0, y1=y1, line_width=line_width, fillcolor=fillcolor, opacity=opacity, **kwargs)
    return self
   
  def add_vrect(self, x0, x1, line_width= 0, fillcolor='red', opacity=0.2, **kwargs):
    self.fig.add_vrect(x0=x0, x1=x1, line_width=line_width, fillcolor=fillcolor, opacity=opacity, **kwargs)
    return self
  
  def add_annotation(self, text=None, col_idx:int=0, x=None, y=None, pos=None, showarrow=True, xshift=0, yshift=2, **kwargs):
    

    ds = self.df.iloc[:,col_idx]

    
    if pos == 'min':  x = ds.index[ds.argmin()]
    elif pos == 'max':x = ds.index[ds.argmax()]
    elif pos == 'recent':x = ds.sort_index().index[-1]
    elif pos == 'first':x = ds.sort_index().index[0]
    if y is None: y=ds[x]
    if text is None: 
      if isinstance(x, datetime):x_pos=x.strftime('%Y-%m')
      else: x_pos = x
      text = f'({x_pos}, {y})'
    self.fig.add_annotation(x=x, y=y,text=text,showarrow=showarrow, arrowhead=1,  xshift=xshift, yshift=yshift,**kwargs) # 화살표 헤드 표시: arrowhead=1
    return self

  # ====================================================================================================
  # 레이아웃 설정
  # legend_title="Legend Title"
  # legend=dict(orientation="h",yanchor="bottom",y=1.02, xanchor="right",x=1) 수평으로 legend 달기
  # ====================================================================================================  
  def update_layout(self, title="Plot Title", width=400, height=700, legend=dict(orientation="h",yanchor="bottom",y=1.01, xanchor="right",x=1), **layouts):
      self.fig.update_layout(title=title, width=width, height=height, legend=legend, **layouts)
      return self
            
  def update_yaxes(self, title_text=None, tickangle=0, secondary_y=False, **yaxes_layouts):
      self.fig.update_yaxes(title_text=title_text, tickangle=tickangle,secondary_y=secondary_y, **yaxes_layouts)
      return self
              
  def update_xaxes(self, title_text=None, tickangle=-45, **yaxes_layouts):
                 
      self.fig.update_xaxes(title_text=title_text, tickangle=tickangle, **yaxes_layouts)
      return self         
       
  # ====================================================================================================
  # 그래프 출력
  # ====================================================================================================  
            
  def show(self):
      self.fig.show()
      return self
    
  def export_file(self, format='html', file_name='untitled'):  
      today = datetime.today().strftime('%Y%M%d')
      if format == 'html':
          self.fig.write_html(f'{file_name}_{today}.{format}')
      return self
    
  def trx_to_byte(self):
      return self.fig.to_image(format="png", scale=2)     