from market.macro.plotviz_economic_indicator import PlotEconomicIdx

class DiffusionIndexphiladelphia:
    @staticmethod
    def descr():
        return """-필라델피아 연방은행_기업경기 전망 보고서-
동부 펜실베니아, 남부 뉴저지, 델라웨어의 제조업 활동을 조사한 내용
산업 부문의 변화를 측정하는 뛰어난 지표로 평가 한다.
특정 지역만을 다루고 있기는 하지만, 여기서 관찰되는 변화를 통해 광범위한 경제적 변화를 예견할 수 있다.
이 보고서를 참조함으로써 베이지 북의 내용을 사전에 파악할 수 있다."""

    @staticmethod
    def currentGeneralActivity_descr():
        return """[전반적 경제 활동 지수]
이 보고서는 ISM 지수와의 상관 관계가 70%에 이른다. 한정된 지역을 바탕으로 작성되었으며, 하나의 질문에 대한 답변만을 반영하고 있기 때문에 변동성이 크다.
3개월 이동 평균으로 파악하는 것이 필요하다."""
    
    @staticmethod
    def currentGeneralActivity(mode='binary'):
        return (PlotEconomicIdx('GACDFSA066MSFRBPHI').renameColumn('전반적 경제 활동 지수')
                .plotWithMa(title='전반적 경제 활동 지수', mode=mode, y1_title=''))
        
    @staticmethod
    def futureEmployment_descr():
        return """[6개월 제조업분야 고용자 수 전망]
경제의 향후 향방에 대한 불안감이 팽배해 있다면 제조업체들은 영구 노동자들에 대한 추가 고용을 꺼려할 가능성이 크다."""
    
    @staticmethod    
    def futureEmployment(mode='binary'):
        return (PlotEconomicIdx('NEFDFSA066MSFRBPHI').renameColumn('6개월 제조업분야 고용자 수 전망')
                .plot(title='6개월 제조업분야 고용자 수 전망', mode=mode, y1_title=''))

    @staticmethod
    def futureCapitalExpenditures_descr():
        return """[6개월 자본 지출 전망]
제조업체들이 소비자 수요의 회복을 확신할 경우, 기업지출이 늘어날 것이다."""

    @staticmethod    
    def futureCapitalExpenditures(mode='binary'):
        return (PlotEconomicIdx('CEFDFSA066MSFRBPHI').renameColumn('6개월 자본 지출 전망')
                .plot(title='6개월 자본 지출 전망', mode=mode, y1_title=''))
