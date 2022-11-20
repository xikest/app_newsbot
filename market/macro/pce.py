from market.macro.plotviz_economic_indicator import PlotEconomicIdx

class PCE:
    @staticmethod
    def descr():
        return """-PCE, 개인 소득과 지출-

[채권 시장]
소득과 지출 모두에서 별다른 증가가 나타나지 않는 상황을 선호하는 경향이 있다.
반대로 소득, 특히 개인 지출이 증가할 경우 빠른 경제성장과 인플레이션 상승에 대한 우려가 발생할 수 있다. 
    
[주식 시장]
개인소득과 지출의 증가는 경제 활동을 더욱 활성화시키고 기업 이윤을 증대시킨다는 점 때문에 주식 시장에 긍정적인 영향을 준다. 경제가 효율적으로 운영되고 있는 상태에서 개인 지출의 급증하는 상황에서는 인플레이션 가속화와 이자율 상승에 대한 우려를 증가 시킬 수 있다.

[외환 시장]
개인소득과 지출 보고서에 상당히 민감하게 반응한다.
높은 소비자 수요가 성장을 더욱 촉진하고 이자율에 대한 상승압력을 불어넣어 달러를 더욱 매력적인 투자대상으로 여기게 한다. 반면 소비자 지출이 예상에 미치지 못한 결과에서는 금리 인하의 징조가 되며, 달러화 약세로 이어지는 경우가 빈번하게 발생한다."""
    
    @staticmethod
    def personalIncome_descr():
        return """[개인 소득]
소비 지출은 가계의 부의 수준을 가계가 어떻게 바라보느냐에 따라 크게 영향을 받는다.
가계가 자본투자나 부동산 투자를 통해 자산이 증가할 것이라고 예상할 경우 소비지출이 큰 폭으로 증가할 수 있다는 것이다.
이런 현상을 부의 효과, 또는 자산효과(walth effect)라고 일컫는다."""
    
    @staticmethod
    def personalIncome(mode='binary'):
        return (PlotEconomicIdx('PI').renameColumn('개인 소득')
                .plot(title='개인 소득', mode=mode, y1_title=''))
        
    @staticmethod
    def realDisposablePersonalIncome_descr():
        return """[실질 가처분 소득]
세금을 제하고 남은 월평균 소득에 인플레이션 조정을 가한 수치
실질가처분 소득의 변화는 소비자 지출 패턴의 변화를 예고하는 지표로 여겨진다."""
        
    @staticmethod    
    def realDisposablePersonalIncome(mode='binary'):
        return (PlotEconomicIdx('DSPIC96').renameColumn('실질 가처분 소득')
                .plot(title='실질 가처분 소득', mode=mode, y1_title=''))
        
    @staticmethod
    def personaloutlays_descr():
        return """[개인 경비]
(개인소비지출, 이자지출, 개인 이전지출)"""
        
    @staticmethod    
    def personaloutlays(mode='binary'):
        return (PlotEconomicIdx('A068RC1').renameColumn('개인소비지출, 이자지출, 개인 이전지출')
                .plot(title='개인 경비', mode=mode, y1_title=''))
        
    @staticmethod
    def pce_descr():
        return """[개인 소비지출]
내구재와 비내구재, 서비스에 대한 개인의 초 지출량을 합산"""

    @staticmethod    
    def pce(mode='binary'):
        return (PlotEconomicIdx('PCE').renameColumn('개인 소비지출')
                .plot(title='PCE 개인 소비지출', mode=mode, y1_title=''))
        
    @staticmethod
    def personalInterestPayments_descr():
        return """[이자 지출]
이자지급, 모기지 부채, 주택담보대출 등은 투자 지출에 가까워 여기에는 포함되지 않는다.
개인가처분소득의 2.5%를 초과하면 가계는 금융 스트레스를 받을 수 있다."""
        
    @staticmethod    
    def personalInterestPayments(mode='binary'):
        return (PlotEconomicIdx('B069RC1').renameColumn('이자 지출')
                .plot(title='이자 지출', mode=mode, y1_title=''))
        
    @staticmethod
    def personalInterestPayments_disposablePersonalIncome_descr():
        return """[개인 이자 부담 / 개인 가처분 소득]
(소득에서 이자 부담을 얼마나 하는가?)
'Personal interest payments / Disposable Personal Income'"""

    @staticmethod    
    def personalInterestPayments_disposablePersonalIncome(mode='binary'):
        return (PlotEconomicIdx('B069RC1').div('DSPI').renameColumn('이자 지출')
                .plot(title='이자 지출', mode=mode, y1_title=''))

    # plot_div(self, colKey1:str, colKey2:str, column_name:str='0',title:str=' ',  mode:str='binary', y1_title:str='')
    
    @staticmethod
    def expenditures_durable_descr():
        return """[내구재 지출]
3년 이상 사용하는 자동차, 전기제품 등의 값 비싼 소비재에 대한 지출로 구성되어 있다.
이러한 제품들은 종종 유자를 통해 구매되는 경우가 많기 때문에, 경제 변화에 민감한 반응을 보인다.
경제 상황 악화의 기미가 나타는 즉시 바로 하락하는 경향을 보이기도 한다.'"""

    def expenditures_durable(mode='binary'):
        return (PlotEconomicIdx('PCEDG').renameColumn('내구재 지출')
                .plot(title='내구재 지출', mode=mode, y1_title=''))
        
    @staticmethod
    def real_pce_descr():
        return """[실질 개인 소비지출]
GDP의 2/3 가량이 실질 개인소비지출에 근거를 두고 있다.
최근 3개월 변화를 관찰하여 추세를 파악하는 것이 중요하다'"""

    def  real_pce(mode='binary'):
        return (PlotEconomicIdx('PCEC96').renameColumn('실질 개인 소비지출')
                .plot(title='PCE 실질 개인 소비지출', mode=mode, y1_title=''))   
         

    def  pce_PriceIndex(mode='binary'):
        return (PlotEconomicIdx('PCEPI').renameColumn('개인 소비지출 체인 타입_월간')
                .plot(title='개인 소비지출 체인 타입_월간', mode=mode, y1_title=''))    
    
    
    @staticmethod
    def pce_PriceIndex_yearly_descr():
        return """[개인 소비지출 체인 타입 연간 변화율]
평균적으로 연간 PCE 물가상승률은 CPI보다 약 0.3% 정도 나즌 수준을 보이는 경향이 있다.
CPI에서는 소비자들이 대용품을 구매할 수도 있다는 가능성을 고려하지 않는다. 반면 PCE 물가지수에서는 대용품 구매를 인정하고 있다.
이런 이유로 PCE 물가상승률은 CPI보다 낮은 수치를 보이는 경향이 있다."""

    def  pce_PriceIndex_yearly(mode='binary'):
        return (PlotEconomicIdx('PCEPI').renameColumn('개인 소비지출 체인 타입_월간')
                .plotWithMa(window=3, title='개인 소비지출 체인 타입_월간', mode=mode, y1_title=''))    