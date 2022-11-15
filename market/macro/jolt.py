from market.macro.plotviz_economic_indicator import PlotEconomicIdx

class Jolt:
    @staticmethod
    def descr():
        return "이 보고서가 제시하는 총 신규 채용건수, 구인 건수 및 이직 규모의 정보는 현재 경제 상황과 특정 산업의 수익 및 수입에 미칠 수 있는 영향을 주시하게 합니다."
    
    @staticmethod
    def jobOpenings_Nonfarm(mode='binary'):
        return (PlotEconomicIdx('JTSJOL').renameColumn('job Openings: Total Nonfarm')
                .plot(title='job Openings: 비농업', mode=mode, y1_title=''))
    @staticmethod    
    def jobOpenings_Private(mode='binary'):
        return (PlotEconomicIdx('JTS1000JOL').renameColumn('Job Openings: Total Private')
                .plot(title='Job Openings: 민간', mode=mode, y1_title=''))
        
    @staticmethod    
    def jobOpenings_Government(mode='binary'):
        return (PlotEconomicIdx('JTS9000JOL').renameColumn('Job Openings: Government')
                .plot(title='Job Openings: 정부', mode=mode, y1_title=''))
  
    @staticmethod    
    def hires_Nonfarm(mode='binary'):
        return (PlotEconomicIdx('JTSHIL').renameColumn('비농업 신규 채용수')
                .plot(title='비농업 신규 채용수', mode=mode, y1_title=''))
    @staticmethod    
    def hires_Private(mode='binary'):
        return (PlotEconomicIdx('JTS1000HIL').renameColumn('민간 신규 채용수')
                .plot(title='민간 신규 채용수', mode=mode, y1_title=''))
    @staticmethod    
    def hires_Government(mode='binary'):
        return (PlotEconomicIdx('JTS9000HIL').renameColumn('정부 신규 채용수')
                .plot(title='정부 신규 채용수', mode=mode, y1_title=''))
    
    @staticmethod    
    def separations_Nonfarm(mode='binary'):
        return (PlotEconomicIdx('JTSTSL').renameColumn('이직건수 - 비농업')
                .plot(title='비농업 이직건수', mode=mode, y1_title=''))
    
    @staticmethod    
    def separations_Private(mode='binary'):
        return (PlotEconomicIdx('JTS1000TSL').renameColumn('이직건수 - 민간')
                .plot(title='민간 이직건수', mode=mode, y1_title=''))
    
    @staticmethod    
    def separations_Government(mode='binary'):
        return (PlotEconomicIdx('JTS9000TSL').renameColumn('이직건수 - 정부')
                .plot(title='정부 이직건수', mode=mode, y1_title=''))
    
    @staticmethod    
    def quits_Nonfarm(mode='binary'):
        return (PlotEconomicIdx('JTSQUL').renameColumn('자발적 퇴사 규모 - 비농업')
                .plot(title='자발적 퇴사 규모 - 비농업', mode=mode, y1_title=''))
    
    @staticmethod    
    def quits_Private(mode='binary'):
        return (PlotEconomicIdx('JTS1000QUL').renameColumn('자발적 퇴사 규모 - 민간')
                .plot(title='자발적 퇴사 규모 - 민간', mode=mode, y1_title=''))
    
    @staticmethod    
    def quits_Government(mode='binary'):
        return (PlotEconomicIdx('JTS9000QUR').renameColumn('자발적 퇴사 규모 - 정부')
                .plot(title='자발적 퇴사 규모 - 정부', mode=mode, y1_title=''))
    
     