import pandas as pd
import pandas_datareader.data as web
from tools.graph_plot.basic_plot import PlotvizBasic
from tools.time.time import Periods
from typing import Optional

class PlotEconomicIdx:
    def __init__(self, colKey:str):
        self._colName:Optional[str]= None
        self._ds:pd.Series = self.load_data_from_fred(colKey)

    def sub(self, colKey):
        data = self._ds.values - self.load_data_from_fred(colKey).values
        self._ds = pd.DataFrame(data, index=self._ds.index, columns=self._ds.columns)
        return self
        
    def load_data_from_fred(self, colKey:str): # 데이터 받이오기
        start, end = Periods.make_period(periods=5)
        return web.DataReader(colKey, 'fred', start, end)
    
    def renameColumn(self, colName:Optional[str]=None): # 데이터 이름 변경
        self._colName=colName
        if colName is not None: self._ds.columns = [self._colName]
        return self

    def plot(self, title:str=' ',  mode:str='binary', y1_title:Optional[str]=None):  #변화율을 표시
        data = self._ds.applymap(lambda x: round(x,1))
        if y1_title  is None:   return PlotvizBasic.plot(data, title,  mode)
        else:   return PlotvizBasic.plotWithPctchage(data, title,  mode, y1_title)


    def plotWithMa(self, window=3, title:str=' ',  mode:str='binary', y1_title:str=''): #이동평균
        data = self._ds.rolling(window).mean().dropna().applymap(lambda x: round(x,1))
        return PlotvizBasic.plotWithPctchage(data,  title,  mode, y1_title)
    
    # def plotBar(self, periods:str='M'): #막대 그래프
        
    #     return PlotViz(self._ds.resample(periods).sum()).bar()
        
    def plot_div(self, colKey2:str, column_name:str='0',title:str=' ',  mode:str='binary', y1_title:str=''): # 두개의 데이터를 받아서 표시
        
        df = self._ds.join(self.load_data_from_fred(colKey2).applymap(lambda x: round(x,1)))
        ds = pd.DataFrame(df.iloc[:,0] / df.iloc[:,1], columns=column_name)
        return PlotvizBasic.plotWithPctchage(ds, title,  mode, y1_title)