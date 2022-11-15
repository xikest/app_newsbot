from market.macro.plotviz_economic_indicator import PlotEconomicIdx

class AdpNationalEmploymentReport:
    @staticmethod
    def descr():
        return ""
    
    @staticmethod
    def nonfarmPrivatePayrollEmployment(mode='binary'):
        return (PlotEconomicIdx('NPPTTL').renameColumn('Nonfarm: Total')
                .plot(title='Nonfarm: Total', mode=mode, y1_title=''))
    @staticmethod    
    def nonfarmPrivateManufacturingPayrollEmployment(mode='binary'):
        return (PlotEconomicIdx('NPPMNF').renameColumn('Nonfarm: 제조업')
                .plot(title='Nonfarm: 제조업', mode=mode, y1_title=''))
        
    @staticmethod    
    def nonfarmPrivateSmallPayrollEmployment(mode='binary'):
        return (PlotEconomicIdx('NPPTS').renameColumn('소규모 기업 고용')
                .plot(title='소규모 기업 고용(1~49)', mode=mode, y1_title=''))
    @staticmethod    
    def nonfarmPrivateMediumPayrollEmployment(mode='binary'):
        return (PlotEconomicIdx('NPPTM').renameColumn('중규모 기업 고용')
                .plot(title='중규모 기업 고용', mode=mode, y1_title=''))
    @staticmethod    
    def nonfarmPrivateLargePayrollEmployment(mode='binary'):
        return (PlotEconomicIdx('NPPTL2').renameColumn('대규모 기업 고용')
                .plot(title='대규모 기업 고용', mode=mode, y1_title=''))
        
