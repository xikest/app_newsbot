from market.macro.plotviz_economic_indicator import PlotEconomicIdx

class E_COMMERCE:
    @staticmethod
    def descr():
        return """-전자 상거래 판매액 보고서-
소매 판매액에서 전자 상거래가 차지하는 비중

[채권 시장]
별다른 영향을 미치지 않는다.

[주식 시장]
일반적으로 영향을 주지 않는다.
나스닥과 같은 기술 집중 주가 지수에 영향을 미칠 것으로 보인다.

[외환 시장]
별다른 영향을 미치지 않는다."""

    @staticmethod
    def e_CommerceRetailSales(mode='binary'):
        return (PlotEconomicIdx('ECOMPCTSA').renameColumn('사전자 상거래를 통한 판매액')
                .plot(title='전자 상거래를 통한 판매액', mode=mode, y1_title=''))