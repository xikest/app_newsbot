import quandl

import pandas as pd
from tools.time.time import Periods
from ids import Ids

def get_keys(key_list, pos=0):
    category = key_list[pos].split('_')[0]
    keys = pd.read_csv(key_list[pos], index_col=0)
    return category, keys


class Qdl:
    
    def __init__(self, category, keys : list or str, periods:int=10):       
        quandl.ApiConfig.api_key = Ids.qdl_api()
        self.__get_data(category, keys, periods).__adjusting_data()
       
       
    def __get_data(self, category, keys : list or str, periods):       
        self.data = {}
        start_date, end_date= Periods.make_period(periods)
        if isinstance(keys, list):
            for key in keys:
                self.data[key]= quandl.get(f'{category}/{key}', start_date=start_date,end_date=end_date)
        else:
            self.data[keys]= quandl.get(f'{category}/{keys}',start_date=start_date,end_date=end_date)
        return self
    
    def __adjusting_data(self):
        self.data = pd.concat(self.data).unstack(0)
        self.data.columns = self.data.columns.droplevel(0)
        return self

    def rename(self, dict_keys=dict):
        self.data=self.data.rename(columns=dict_keys)
        return self