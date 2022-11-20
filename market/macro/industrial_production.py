from market.macro.plotviz_economic_indicator import PlotEconomicIdx

class IndustrialProduction:
    
        
    @staticmethod
    def descr():
        return """-산업생산 및 설비가동률, 미국 산업 생산량과 생산여력을 기록-

[채권 시장]
산업 생산과 설비가동률이 예상보다 높은 수준으로 급등하면 채권 가격이 단기적으로 하락할 수 있다.
특히 이러한 현상은 설비가동률이 무자부족, 생산병목, 인플레이션 등으로 촉발할 수 있는 80%이상의 위험 수준까지 오를 경우 더욱 두드러진다.

[주식 시장]
일반적인 경우에 생산 증가는 경제성장과 기업이윤의 확대를 예고한다.
생산 증가가 지나친 설비 사용과 물가 인상으로 이어지는 경우 부정적인 영향을 받는다.

[외환 시장]
산업생산량의 급증은 경제 성장의 가속화를 암시하는데, 이러한 상황은 달러화를 매개로 한 투자에 대한 수요의 증가를 불러오거나 달러화의 가치 하락을 막는다.""""
    
    @staticmethod
    def industrialProduction_descr():
        return"""[산업 생산 종합지수]
지난 3개월 동안의 산업 생산량 증감률을 관찰함으로써 GDP의 성장에 관해 꽤 정확한 측정을 할 수 있다."""
    
    @staticmethod
    def industrialProduction(mode='binary'):
        return (PlotEconomicIdx('INDPRO').renameColumn('산업 생산 종합지수')
                        .plot(title='산업 생산 종합지수', mode=mode, y1_title=''))

    @staticmethod
    def industrialProduction_ExcludingSelected (mode='binary'):
        return (PlotEconomicIdx('IPX5VHT2S').renameColumn('산업생산 종합, 첨단산업&자동차 제외')
                        .plot(title='산업생산 종합, 첨단산업&자동차 제외', mode=mode, y1_title=''))
                        
    @staticmethod
    def industrialProduction_ConsumerGoods_descr():
        return"""[소비재 총생산량]
높은 매출과 재고 완화는 소비재의 생산 증가를 촉진한다."""
  
    @staticmethod
    def industrialProduction_ConsumerGoods(mode='binary'):
        return (PlotEconomicIdx('IPCONGD').renameColumn('소비재 총생산량')
                        .plot(title='소비재 총생산량', mode=mode, ))
    @staticmethod
    def industrialProduction_BusinessEquipment_descr():
        return"""[사업재 생산량]
사업자 생산량은 기업의 고정투자지출을 반영한다."""
    
    @staticmethod
    def industrialProduction_BusinessEquipment(mode='binary'):
        return (PlotEconomicIdx('IPBUSEQ').renameColumn('사업재 생산량')
                        .plot(title='사업재 생산량', mode=mode, ))
                        
    @staticmethod
    def industrialProduction_Defense_Space_Equipment_descr():
        return"""[방위 및 우주산업 장비 생산량]
군사 및 우주선용 하드웨어 생산에 대해 광범위하게 다룬다."""

    @staticmethod
    def industrialProduction_Defense_Space_Equipment (mode='binary'):
        return (PlotEconomicIdx('IPB52300S').renameColumn('방위 및 우주산업 장비 생산량')
                        .plot(title='방위 및 우주산업 장비 생산량', mode=mode))
                        
    @staticmethod
    def industrialProduction_Manufacturing_descr():
        return"""[제조업 생산량]
미국 제조업체들의 기업이윤을 예측하고 싶다면 제조업 생산량의 3개월 변화율을 구하고, 이것을 3개월 동안의 소비자물가인상률과 곱하면 된다."""

    @staticmethod
    def industrialProduction_Manufacturing(mode='binary'):
        return (PlotEconomicIdx('IPMAN').renameColumn('제조업 생산량')
                        .plot(title='제조업 생산량', mode=mode))
                        
    @staticmethod
    def industrialProduction_Motor_VehiclesParts_descr():
        return"""[자동차와 부품]
자동차 제조업체들이 자동차 판매업체들의 충분한 수요를 예상하고 있는지 여부를 말해준다.
자동차 제조 산업은 전체 GDP에서 약 4%의 비중을 차지한다.
알루미늄과 철, 플라스틱, 고무, 섬유, 비닐, 철강, 컴퓨터칩 등의 자재에 대한 가장 거대한 구매집단이다."""
    
    @staticmethod
    def industrialProduction_Motor_VehiclesParts(mode='binary'):
        return (PlotEconomicIdx('IPG3361T3S').renameColumn('자동차와 부품')
                        .plot(title='자동차와 부품', mode=mode))
        
    @staticmethod
    def industrialProduction_Communications_Equipment(mode='binary'):
        return (PlotEconomicIdx('IPHITEK2S').renameColumn('첨단산업 제조업 생산량')
                        .plot(title='첨단산업 제조업 생산량', mode=mode, y1_title=''))
    @staticmethod
    def industrialProduction_Semiconductor(mode='binary'):
        return (PlotEconomicIdx('IPG3344S').renameColumn('반도체 제조업 생산량')
                        .plot(title='반도체 제조업 생산량', mode=mode, y1_title=''))
                        
    @staticmethod
    def industrialProduction_Computer_Electronic_descr():
        return"""[컴퓨터 전자제품 제조업 생산량]
이러한 제품들의 높은 생산량은 생산성 수준을 향상시키려는 기업들의 의지를 반영한다."""
    
    @staticmethod
    def industrialProduction_Computer_Electronic(mode='binary'):
        return (PlotEconomicIdx('IPG334S').renameColumn('컴퓨터 전자제품 제조업 생산량')
                        .plot(title='컴퓨터 전자제품 제조업 생산량', mode=mode, y1_title=''))
                        
    @staticmethod
    def industrialProduction_ExcludingMotorVehicles_descr():
        return"""[제조업 생산, 자동차 제외]
자동차 산업에서의 심한 변동은 전반적인 산업생산의 변화를 증폭시킬 수 있다."""    
    
    @staticmethod
    def industrialProduction_ExcludingMotorVehicles(mode='binary'):
        return (PlotEconomicIdx('IPXXX001S').renameColumn('제조업 생산, 자동차 제외')
                        .plot(title='제조업 생산, 자동차 제외', mode=mode, y1_title=''))
                        
                        
                        
                        
    @staticmethod
    def industrialProduction_ExcludingHi_Tech(mode='binary'):
        return (PlotEconomicIdx('IPX4HTMVS').renameColumn('제조업 생산, 첨단 산업,&자동차 제외')
                        .plot(title='제조업 생산, 첨단 산업,&자동차 제외', mode=mode, y1_title=''))
                        
                        
    @staticmethod
    def capacityUtilization_descr():
        return"""[설비 가동률 종합 지수]
80% 이하의 설비가동률은 기업의 신규투자를 저해하고 심지어는 노동자의 대량해고로까지 이어질수 있다.
반면 제품에 대한 강한 수요는 생산을 자극한다.
설비가동률이 최고 수준에 근접하면 가격인상에 대한 압력이 증가하기 시작한다.
설비가동률이 81%까지 유지되고 있을 때 물가의 폭발적 인상이 유발되지 않는다.
일반적으로 설비가동률이 82 ~ 85%대로 진입하면 생산의 병목 현상이 나타나고, 이것은 생산자 물가에 새로운 인상 압력을 가한다.
인플레이션을 촉발하는 설비가동률의 위험 수준은 각 산업별로 다르다.
85%의 가동률은 자동차 산업에 큰 부담이 될 수 있지만, 1차 금속 산업에는 별다른 문제가 되지 않는다.

컴퓨터 산업은 94-95년 경제 활황기에 최고 86.6%의 가동률로 운영되었으나, 2003년에는 평균 수준인 71%의 가동률을 유지하였다.
이 시기에 매우 많은 생산설비가 유휴 상태에 머무르면서 컴퓨터와 주변기기가 낮은 가격대를 유지할 수 있었다."""    
  
    @staticmethod
    def capacityUtilization(mode='binary'):
        return (PlotEconomicIdx('TCU').renameColumn('설비 가동률 종합 지수')
                        .plot(title='설비 가동률 종합 지수', mode=mode, y1_title=''))
        
        
    @staticmethod
    def capacityUtilization_Manufacturing(mode='binary'):
        return (PlotEconomicIdx('MCUMFN').renameColumn('제조업 가동률')
                        .plot(title='제조업 가동률', mode=mode, y1_title=''))
        
    @staticmethod
    def capacityUtilization_Manufacturing_hi_tech(mode='binary'):
        return (PlotEconomicIdx('CAPUTLHITEK2S').renameColumn('첨단 산업 가동률')
                        .plot(title='첨단 산업 가동률', mode=mode, y1_title=''))
        
    @staticmethod
    def capacityUtilization_Manufacturing_Computers(mode='binary'):
        return (PlotEconomicIdx('CAPUTLG3341S').renameColumn('컴퓨터와 주변기기 산업 가동률')
                        .plot(title='컴퓨터와 주변기기 산업 가동률', mode=mode))
    @staticmethod
    def capacityUtilization_Manufacturing_Communications(mode='binary'):
        return (PlotEconomicIdx('CAPUTLG3342S').renameColumn('통신장비 산업 가동률')
                        .plot(title='통신장비 산업 가동률', mode=mode))
    @staticmethod
    def capacityUtilization_Vehicles(mode='binary'):
        return (PlotEconomicIdx('CAPUTLG3361T3S').renameColumn('자동차 산업 가동률')
                        .plot(title='자동차 산업 가동률', mode=mode))
    @staticmethod
    def capacityUtilization_PrimaryMetal(mode='binary'):
        return (PlotEconomicIdx('CAPUTLG331S').renameColumn('1차 금속 산업 가동률')
                        .plot(title='1차 금속 산업 가동률', mode=mode))
        