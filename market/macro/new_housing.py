from market.macro.plotviz_economic_indicator import PlotEconomicIdx

class NewHousing :
    @staticmethod
    def descr():
        return """-주택 착공과 허가건수-
서비스에 초점을 둔 경제 월간 보고서

[채권 시장]
주택 착공 건수의 현저한 증가는 경제의 호황과 인플레이션 압력의 증가를 의미 한다. \

[주식 시장]
주택 건설 활동이 활발하게 이루어지고 인플레이션이 안정적으로 유지된다면, 긍정적인 상황이 된다.
경제적 활황기 속에서 주택착공이 급증하는 현상은 FED가 단기 금리를 인상할 것이라는 우려가 발생할 수 있다.

[외환 시장]
주택 건설 활동의 성장은 일반적으로 기업이윤 증가와 미국 금리의 안정을 보장함으로써 달러 가치에 긍정적인 영향을 주는 것으로 여겨진다.
"""
    @staticmethod
    def report_url():
        return "https://www.census.gov/construction/nrc/index.html"
    
    @staticmethod
    def newHousing_total_descr():
        return """[주택 착공 호수 총합]
건전한 주택 시장은 연간 주택착공건수가 150만 ~ 200만에 이르는 상태이다.
100만 건 이하는 경제에 어려움을 초래하며, 장기간 동안 200만건 이상을 유지하는 것 또한 자재 공급 및 노동자 부족과 같은 문제를 불러일으킬수 있다."""

    @staticmethod
    def newHousing_total (mode='binary'):
        return (PlotEconomicIdx('HOUST').renameColumn('주택 착공')
                .plot(title='주택 착공', mode=mode, y1_title=''))

    @staticmethod
    def newHousing_single_descr():
        return """[단독주택 착공 건수]
공동주택 건설이 부동산 투기의 추세와 세금정책 변화에 쉽게 좌우될 수 있는 반면, 단독 주택 건설은 소비자 신뢰도와 소비자 수요에 큰 영향을 받기 때문에 신뢰성 있는 선행지표로 여겨진다."""

    @staticmethod
    def newHousing_single (mode='binary'):
        return (PlotEconomicIdx('HOUST1F').renameColumn('단독주택 착공')
                .plot(title='단독주택 착공', mode=mode, y1_title=''))
        
    @staticmethod
    def newHousing_total_permit_descr():
        return """[신규 개인주택 건축 허가 총합]
건축 허가는 주택 착공보다 1 ~ 3달 정도 선행하여 나타난다.
모든 허가가 착공으로 이어지는 것은 아니지만 밀접한 연관성이 있다.
"""
    @staticmethod
    def newHousing_total_permit (mode='binary'):
        return (PlotEconomicIdx('PERMIT').renameColumn('신규 개인주택 건축 허가')
                .plot(title='신규 개인주택 건축 허가', mode=mode, y1_title=''))
        
    @staticmethod
    def newHousing_single_permit (mode='binary'):
        return (PlotEconomicIdx('PERMIT1').renameColumn('신규 단독 건축 허가')
                .plot(title='신규 단독 건축 허가', mode=mode, y1_title=''))
        
    @staticmethod
    def newHousing_total_notStarted_descr():
        return """[기공이 시작되지 않은 신규 주택 총합]
이 수치가 증가하게 되면 건설업체들이 신규주택 수요를 따라 잡는데 어려움이 있음을 의미한다.
"""
    @staticmethod
    def newHousing_total_notStarted (mode='binary'):
        return (PlotEconomicIdx('AUTHNOTTSA').renameColumn('기공이 시작되지 않은 신규 주택 총합')
                .plot(title='기공이 시작되지 않은 신규 주택 총합', mode=mode, y1_title=''))
        
    @staticmethod
    def newHousing_single_notStarted (mode='binary'):
        return (PlotEconomicIdx('AUTHNOT1USA').renameColumn('기공이 시작되지 않은 신규 단독 주택')
                .plot(title='기공이 시작되지 않은 신규 단독 주택', mode=mode, y1_title=''))
        
    @staticmethod
    def newHousing_total_underConstruction(mode='binary'):
        return (PlotEconomicIdx('UNDCONTSA').renameColumn('공사가 진행 중인 신규 주택 총합')
                .plot(title='공사가 진행 중인 신규 주택 총합', mode=mode, y1_title=''))
        
    @staticmethod
    def newHousing_total_underConstruction(mode='binary'):
        return (PlotEconomicIdx('UNDCON1USA').renameColumn('공사가 진행 중인 신규 단독 주택')
                .plot(title='공사가 진행 중인 신규 단독 주택', mode=mode, y1_title=''))
        
    @staticmethod
    def newHousing_total_completed_descr():
        return """[공사가 완료된 신규주택 수]
단독 주택의 경우 기공부터 완공까지 평균 6개월 소요되고, 공동 주택의 경우 10개월에서 1년 정도가 소요 된다.
"""
    @staticmethod
    def newHousing_total_completed (mode='binary'):
        return (PlotEconomicIdx('COMPUTSA').renameColumn('공사가 완료된 신규 주택 총합')
                .plot(title='공사가 완료된 신규 주택 총합', mode=mode, y1_title=''))
        
    @staticmethod
    def newHousing_single_completed (mode='binary'):
        return (PlotEconomicIdx('COMPU1USA').renameColumn('공사가 완료된 신규 단독 주택')
                .plot(title='공사가 완료된 신규 단독 주택', mode=mode, y1_title=''))