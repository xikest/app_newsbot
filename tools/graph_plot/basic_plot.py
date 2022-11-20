
# =============================================================================================    
# 기본으로 미리 준비된 샘플 코드
# =============================================================================================

import datetime
import pandas as pd
import pandas_datareader.data as web
from tools.graph_plot.plotviz import PlotViz
from tools.time.time import Periods
from typing import Optional
import numpy as np


class PlotvizBasic:
    @staticmethod
    def plotWithPctchage(ds, title:str=' ',  mode:str='show', yaxis_title = None, y1_title:str=''):  #변화율을 표시
        
        ds_pct = ds.pct_change().replace([np.inf, -np.inf], np.nan).dropna()
        max_ds = abs(ds_pct.quantile(q=0.9).max())
        min_ds = abs(ds_pct.quantile(q=0.9).min())
        range_secondary_y = int(np.where(max_ds > min_ds, max_ds, min_ds)*100*2+1)
        if yaxis_title is None: yaxis_title = ''
        
        fig = (PlotViz(ds).line()
                                .bar(pct_change=True, secondary_y=True, opacity=0.5)
                                .add_annotation( pos='recent')
                                .update_layout(title= f'{title}', yaxis_title=yaxis_title, width=500, height=700)
                                .update_yaxes(title_text=y1_title).update_yaxes(title_text='percent (%)', secondary_y=True, range=[0-range_secondary_y,  range_secondary_y])
                                .update_xaxes())
        if mode == 'binary': return fig.trx_to_byte()
        elif mode == 'show': return fig.show()
        
    @staticmethod
    def plot(ds, title:str=' ',  mode:str='show',  yaxis_title=None, yaxis_title =''):  #변화율을 표시
        if yaxis_title is None: yaxis_title = ''
        
        fig = (PlotViz(ds).line()
                                .add_annotation( pos='recent')
                                .update_layout(title= f'{title}', yaxis_title=yaxis_title,width=500, height=700)
                                .update_xaxes())
        if mode == 'binary': return fig.trx_to_byte()
        elif mode == 'show': return fig.show()
        
    @staticmethod
    def plotForShiller(ds, reference='Shiller PE Ratio by Month', compare_with='S&P 500 Real Price by Month', mode='binary'):
        fig = (PlotViz(ds).line(col_idx=reference)
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
        
        
        