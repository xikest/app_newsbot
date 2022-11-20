from market.macro.plotviz_economic_indicator import PlotEconomicIdx

class InitialClaims:
    @staticmethod
    def descr():
        return """-캐스화물지수-
북미 전역으로 운송 되는 화물의 월별 물량과 운송 비용을 평가
"""
    @staticmethod
    def report_url():
        return "https://ide-run.goorm.io/workspace/dTCzqPwNRYleAYbW4Ni?_ga=2.84546073.1259517294.1668769379-185406363.1667556270"
    
    @staticmethod
    def cassFreightIndex_descr():
        return """[캐스화물지수: 해상 선적]
배송된 제품의 양을 반영한다
경제가 가속화될 때 공장은 생산 속도를 높이기 위해 기초 자재 주문을 늘릴 것이며, 소매업체는 증가하는 소비자 수요를 만족시키기 위해 공급업체에 더 많은 재고를 배송하도록 요청할 것이다.
제조 업체는 빠른 성장을 보이는 신흥국으로 향하는 상선에 적재하기 위해 미국의 주요 항구로 더 많은 양의 상품을 선적한다.
국제 경제가 악화되면 출하량이 줄어들어 그 반대의 결과가 초래될 것이다
"""
    @staticmethod
    def cassFreightIndex (mode='binary'):
        return (PlotEconomicIdx('FRGSHPUSM649NCIS').renameColumn('해상 선적')
                .plot(title='해상 선적', mode=mode, y1_title=''))


    @staticmethod
    def cassFreightIndex_expenditures_descr():
        return """[캐스화물지수: 운송 비용의 변화]
연료 비용, 선박의 적재량 부족, 자격을 갖춘 운전수를 얻기 위한 경쟁으로 이난 임금 상승이 있다.
이러한 요인은 특히 생산자 물가 수준에서 미국 경제에 인플레이션 영향을 미칠 수 있다.
"""
    @staticmethod
    def cassFreightIndex_expenditures (mode='binary'):
        return (PlotEconomicIdx('FRGSHPUSM649NCIS').renameColumn('해상 선적')
                .plot(title='해상 선적', mode=mode, y1_title=''))