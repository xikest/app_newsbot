from market.macro.plotviz_economic_indicator import PlotEconomicIdx

class Jolt:
    @staticmethod
    def descr():
        return """[JOLTs, 고용 및 이직 동향]

[채권 시장]
이 보고서가 나올 때 쯤이면, 같은 기준 기간에 대해 일자리 관련 설문 조사가 이미 여러 건 발표된 상태로 큰 반응이 없다.

[주식 시장]
이 보고서가 제시하는 총 신규 채용건수, 구인 건수 및 이직 규모에 대한 관심이 있고 이 정보는 현재 경제 상황과 특정 산업의 수익 및 수입에 미칠 수 있는 영향을 주시한다.

[외환 시장]
큰 반응이 없다."""

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
    def quits_Nonfarm_descr():
        return """[자발적 퇴사 규모]
경제 활동이 활발할 시기에는 퇴직하는 노동자들의 수가 가장 많고, 침체기에는 퇴작자 수가 가장 적다.
"""
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
    
     