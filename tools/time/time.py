from datetime import datetime
from datetime import timedelta
import time
from dateutil.relativedelta import relativedelta
import numpy as np
from functools import wraps
from typing import Union

from traitlets import Float


class Timer:
    @staticmethod             
    def now(): return datetime.utcnow() + timedelta(hours=9)
    
    @staticmethod     
    def sleepToRelease(targetTime:datetime, delay:Union[int, Float]=0):
        delayDefault = 5
        try:
            sleepPeriod = (targetTime - Timer.now()).total_seconds()
            return np.where(sleepPeriod> delayDefault, sleepPeriod, delayDefault) 
        except: 
            return delayDefault * delay
        
    @staticmethod        
    def time_log(func):
        @wraps(func)
        def wrapper():
                start = time.time()          
                func()
                end = time.time()
                print(f'fin_time taken: {(end - start)}')
        return wrapper

        
    
   
class Periods:
    @staticmethod
    def make_period(periods=10):
        today = datetime.today()
        end_date = today.strftime('%Y-%m-%d')
        start_date = (today - relativedelta(years=periods)).strftime('%Y-%m-%d')
        return start_date, end_date
    
    






