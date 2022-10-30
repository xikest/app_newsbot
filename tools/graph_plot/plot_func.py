from ast import Str
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from numpy import ndarray

def make_trace(df:pd.DataFrame, mode:str, name:str=None, pct_change:bool=False, col_idx:int or str=0, **kwarg):
  
  if pct_change == True : df = df.pct_change()*100
  
  if mode == 'heatmap':
    trace = go.Heatmap(z= df.to_numpy(), x= df.columns.to_list(), y=df.index.to_list())
  else:
    if isinstance(col_idx, int):
      ds = df.iloc[:,col_idx]
    elif isinstance(col_idx, str):
      ds = df.loc[:,col_idx]
      
    if name is None: name=ds.name    
    if mode == 'bar': 
      trace = go.Bar(x = ds.index, y = ds, text = round(ds,2), name=name, **kwarg)
    elif  mode == 'scatter':
      trace = go.Scatter(x = ds.index, y = ds, mode = 'markers', marker = dict(size = 10), name=name, **kwarg)  
    elif mode == 'box':
      trace = go.Box(y = ds, name= name, **kwarg)
    elif mode == 'hist':
      trace = go.Histogram(x = ds, name=name, **kwarg)
    elif mode == 'line':
      trace = go.Scatter(x = ds.index, y = ds, mode = 'lines', marker = dict(size = 10), name=name, **kwarg)
    
  return trace

def dataset_df(n:int):
    x=np.random.randint(1,100,n,int)
    return pd.DataFrame(x)

def check_instance_for_df(data):
  if isinstance(data, pd.Series): return pd.DataFrame(data)
  if isinstance(data, dict): return pd.DataFrame.from_dict(data,  orient='index').rename(columns={0:'data'})
  if isinstance(data, list): return pd.DataFrame(data, columns=['data'])
  if isinstance(data, ndarray): return pd.DataFrame(data, columns=['data'])
  else : return data