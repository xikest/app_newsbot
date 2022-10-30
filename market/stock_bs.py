import numpy as np
import yfinance as yf
import pandas as pd
from tools.graph_plot.plotviz import PlotViz

class BalanceSheet():
    def __init__(self, symbol):
        self.symbol = symbol
        self.__data__ = yf.Ticker(symbol)
        self.plot_data = dict()
        pass
        
        
# =============================================================================
# call_basic_information: 
# =============================================================================
    def sector_info(self):
        return self.__data__.info['sector']

    def split_info(self):
        col = self.__data__.actions.loc[:, 'Stock Splits'] > 0
        self.plot_data['title'] =f'{self.symbol} split history'
        self.plot_data['y_title'] = None
        self.plot_data['data'] = self.__data__.actions[col].loc[:, 'Stock Splits']
        return self

    def prices(self):
         self.plot_data['title'] =f'{self.symbol} price'
         self.plot_data['y_title'] = None
         self.plot_data['data'] = self.__data__.history(period="max")['Close']
         return self
        
    def ESG_score(self):
        keys = ['environmentScore', 'socialScore', 'governanceScore'] 
        self.plot_data['title'] =f'{self.symbol} ESG'
        self.plot_data['y_title'] = None
        self.plot_data['data'] =  pd.DataFrame({key : self.__data__.sustainability.loc[key,:].values  for key in keys}, index=['ESG score']).transpose().loc[:,'ESG score']
        return self

    def upcoming_event(self):
         return  self.__data__.calendar

    def recommendations(self):
        recom = self.__data__.recommendations
        recom.index = recom.index.map(lambda x: x.strftime('%Y-%m'))
        recom = recom.groupby(by=['Date','Action'])['Action'].count()
        self.plot_data['title'] =f'{self.symbol} recommendations'
        self.plot_data['y_title'] = None
        self.plot_data['data'] = recom.unstack('Action').loc[:,['up', 'main', 'down', 'init']].fillna(0).transpose()
        return self

# =============================================================================
# cashflow ratio with sheet data: 
# =============================================================================
    def call_from_cashflow(self, key = 'Net Income',  period:str= 'quarterly'):
        if period == 'quarterly' : return self.__data__.quarterly_cashflow.loc[key,:]
        elif  'yearly' : return self.__data__.cashflow.loc[key,:]

    def __call_ratio_from_cashflow__(self, col_name:str, pre_key:str, suf_key:str, period:str) ->pd.Series:
       return pd.Series(self.call_from_cashflow(pre_key, period)/ self.call_from_cashflow(suf_key, period), index=self.call_from_cashflow(pre_key, period).index, name=col_name)


# =============================================================================
# balancesheet ratio with sheet data: 
# =============================================================================

    def call_from_balance_sheet(self, key = 'Total Assets',  period:str= 'quarterly'):
        if period == 'quarterly' : return self.__data__.quarterly_balance_sheet.loc[key,:]
        elif  'yearly' : return self.__data__.balance_sheet.loc[key,:]

    def debt_longterm(self,  period:str= 'quarterly'):           
        self.plot_data['title'] =f'{self.symbol}: lonterm debt {period}'
        self.plot_data['y_title'] = None
        if period == 'quarterly' : self.plot_data['data'] = self.call_from_balance_sheet(period='quarterly',  key = 'Long Term Debt')
        elif 'yearly' : self.plot_data['data'] = self.call_from_balance_sheet(period='yearly',  key = 'Long Term Debt')
        return self

# =============================================================================
# calculate_bs and cs ratio with sheet data: 
# =============================================================================

    def ratio_incomes(self, period='quarterly'):
        self.plot_data['title'] =f'{self.symbol}: 현금 흐름 Vs 수익 창출 {period}'
        self.plot_data['y_title'] = '현금 흐름 (%)'
        self.plot_data['second_y_title'] = '수익 창출 (%)'
        self.plot_data['data']  = pd.DataFrame()
        self.plot_data['data']['현금 흐름'] = self.ratio_income_div_operating(period)*100
        self.plot_data['data']['수익 창출'] = self.ratio_income_div_assetes(period)*100
        return self
        

    def ratio_income_div_operating(self, period='quarterly'):
        return pd.Series(self.call_from_cashflow('Net Income',period) / self.call_from_cashflow('Total Cash From Operating Activities', period), name='영업 활동으로 인한 현금 흐름 (Income/Operating)')

    def ratio_income_div_assetes(self, period='quarterly'):
      return pd.Series(self.call_from_cashflow('Net Income',period) / self.call_from_balance_sheet('Total Assets', period), name='자산 대비 수익 창출 능력 (Income/Assets)')

# =============================================================================
# call options: 
# =============================================================================

    # def option(self, option_type: str):    
    #     expiration = self.__data__.options[0]
    #     options = self.__data__.option_chain(expiration)
    #     self.plot_data['title'] =f'{self.symbol}: {option_type}'
    #     self.plot_data['y_title'] = None
    #     if option_type == 'call' : self.plot_data['data'] = options.calls.loc[:,['strike', 'volume']].set_index('strike').dropna()
    #     elif 'put': self.plot_data['data'] = options.puts.loc[:,['strike', 'volume']].set_index('strike').dropna()
    #     return self
    
    def option(self):    
        expiration = self.__data__.options[0]
        options = self.__data__.option_chain(expiration)
        self.plot_data['title'] =f'{self.symbol}: call vs put'
        self.plot_data['y_title'] = None
        self.plot_data['data']  = pd.DataFrame()
        self.plot_data['data']['call'] = options.calls.loc[:,['strike', 'volume']].set_index('strike').dropna()
        self.plot_data['data']['put'] = options.puts.loc[:,['strike', 'volume']].set_index('strike').dropna()
        return self


    def option_series(self, option_type:str) -> pd.DataFrame:
        option_dict = dict()
        for expiration in self.__data__.options:
            try:
                options = self.__data__.option_chain(expiration)

                if option_type == 'call' : option_series = options.calls.loc[:,['strike', 'volume']].set_index('strike').dropna()
                elif 'put': option_series = options.puts.loc[:,['strike', 'volume']].set_index('strike').dropna()

                arg_max = np.argmax(option_series)
                option_dict[expiration] = option_series.iloc[arg_max,:].name.astype(float)
            except:  pass
        
        self.plot_data['title'] =f'{self.symbol}: {option_type} series'
        self.plot_data['y_title'] = None
        self.plot_data['data'] = pd.DataFrame.from_dict(option_dict, orient='index').rename(columns={0:'strike'}).loc[:,'strike']
        return self


    def plot(self, mode='binary',  plot_type='bar'):
        title =self.plot_data['title']
        y_title= self.plot_data['y_title']
        second_y_title = self.plot_data['second_y_title']

        if plot_type == 'bar':
          fig = (PlotViz(self.plot_data['data']).bar()
                                              .update_layout(title= title, width=500, height=700)
                                              .update_yaxes(title_text=y_title)
                                              .update_xaxes())
        elif plot_type == 'line' :
          fig = (PlotViz(self.plot_data['data']).line()
                                .update_layout(title= f'{title}', width=500, height=700)
                                .add_annotation( pos='max')
                                .add_annotation( pos='recent')
                                .add_annotation( pos='min')
                                .update_yaxes(title_text=y_title)
                                .update_xaxes())
          
        elif plot_type == 'heatmap':
          fig = (PlotViz(self.plot_data['data']).heatmap()
                                .update_layout(title= f'{title}', width=500, height=700)
                                .update_yaxes(title_text=y_title)
                                .update_xaxes())
        elif plot_type == 'scatter':
            fig = (PlotViz(self.plot_data['data']).scatter()
                                                .update_layout(title= f'{title}', width=500, height=700)
                                                .update_yaxes(title_text=y_title)
                                                .update_xaxes())

        elif plot_type == 'line_pair':
            fig = (PlotViz(self.plot_data['data']).line(col_idx=0).line(col_idx=1)
                                    .update_layout(title= f'{title}', width=500, height=700)
                                    .add_annotation( pos='max').add_annotation( pos='max',col_idx=1, yshift=5)
                                    .update_yaxes(title_text=y_title)
                                    .update_xaxes())
            
        elif plot_type == 'bar_line_pair':
            fig = (PlotViz(self.plot_data['data']).bar(col_idx=0).line(col_idx=1, secondary_y=True)
                                    .update_layout(title= f'{title}', width=500, height=700)
                                    .update_yaxes(title_text=y_title)
                                    .update_yaxes(title_text=second_y_title, secondary_y=True)
                                    .update_xaxes())


        if mode == 'binary': return fig.trx_to_byte()
        elif mode == 'show': return fig.show()
