from market.macro.plotviz_economic_indicator import PlotEconomicIdx

class IndustrialProduction:
    @staticmethod
    def industrialProduction(mode='binary'):
        return (PlotEconomicIdx('INDPRO').renameColumn('산업 생산 종합지수')
                        .plot(title='산업 생산 종합지수', mode=mode, y1_title=''))
            
    @staticmethod
    def industrialProduction_ExcludingSelected (mode='binary'):
        return (PlotEconomicIdx('IPX5VHT2S').renameColumn('산업생산 종합, 첨단산업&자동차 제외')
                        .plot(title='산업생산 종합, 첨단산업&자동차 제외', mode=mode, y1_title=''))
            
    @staticmethod
    def industrialProduction_ConsumerGoods(mode='binary'):
        return (PlotEconomicIdx('IPCONGD').renameColumn('소비재 총생산량')
                        .plot(title='소비재 총생산량', mode=mode, ))
            
    @staticmethod
    def industrialProduction_BusinessEquipment(mode='binary'):
        return (PlotEconomicIdx('IPBUSEQ').renameColumn('사업재 생산량')
                        .plot(title='사업재 생산량', mode=mode, ))
        
    @staticmethod
    def industrialProduction_Defense_Space_Equipment (mode='binary'):
        return (PlotEconomicIdx('IPB52300S').renameColumn('방위 및 우주산업 장비 생산량')
                        .plot(title='방위 및 우주산업 장비 생산량', mode=mode))
        
    @staticmethod
    def industrialProduction_Manufacturing(mode='binary'):
        return (PlotEconomicIdx('IPMAN').renameColumn('제조업 생산량')
                        .plot(title='제조업 생산량', mode=mode))
            
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
    def industrialProduction_Computer_Electronic(mode='binary'):
        return (PlotEconomicIdx('IPG334S').renameColumn('컴퓨터 전자제품 제조업 생산량')
                        .plot(title='컴퓨터 전자제품 제조업 생산량', mode=mode, y1_title=''))
    @staticmethod
    def industrialProduction_ExcludingMotorVehicles(mode='binary'):
        return (PlotEconomicIdx('IPXXX001S').renameColumn('제조업 생산, 자동차 제외')
                        .plot(title='제조업 생산, 자동차 제외', mode=mode, y1_title=''))
    @staticmethod
    def industrialProduction_ExcludingHi_Tech(mode='binary'):
        return (PlotEconomicIdx('IPX4HTMVS').renameColumn('제조업 생산, 첨단 산업,&자동차 제외')
                        .plot(title='제조업 생산, 첨단 산업,&자동차 제외', mode=mode, y1_title=''))
        
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
        