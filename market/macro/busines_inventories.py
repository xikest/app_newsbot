from market.macro.plotviz_economic_indicator import PlotEconomicIdx

class InventoriesSalesRatio:
    @staticmethod
    def descr():
        return  """-기업 재고, 미국의 총 기업 매출과 총 재고 측정-
[채권 시장]
재고의 증가가 GDP의 증가로 이어지고 이자율상승에 압력을 가할 수 있다. 재고투자의 감소는 생산량의 감소를 의미 하는데, 이것은 채권 시장에 긍정적이다.

[주식 시장]
반응이 없다

[외환 시장]
재고율의 급증은 경제가 경기 둔화의 국면에 접어들고 있다는 징후로 볼 수 있다.
일반적으로 제조업과 도소매업에서 판매 및 재고가 동반 상승할 때 달러는 더욱 매력적인 통화로 여겨진다."""
                        
    @staticmethod
    def business_descr():
        return """[총 기업재고율]
평균 1.4개월분 가량의 제품을 재고로 비축하려는 의지를 보이다.
일반적인 경우 재고율이 1.45개월분보다 낮은 수준까지 하락하면, 경제가 침체기에 머물러 있지 않는한 기업들은 재고를 일정수준까지 보충하기 위해 주문을 늘리는 경향을 보인다."""

    @staticmethod
    def totalBusiness(mode='binary'):
        return (PlotEconomicIdx('ISRATIO').renameColumn('총 기업재고율')
                .plotWithMa(title='총 기업재고율', mode=mode, y1_title=''))
        
    @staticmethod
    def saleInventory_descr():
        return """[월간 판매 및 재고 측정치, 소매업 - 도매업 - 제조업]
소비자 지출이 눈에 띄게 둔화될 경우 소매업 매출 또한 침체를 겪게 되며, 소매업체들의 의도하지 않은 재고 추적은 재고율의 상승을 불러온다.
이것은 도매업체들에 대한 주문 감소로 이어진다.
재고가 늘어남에 따라 도매업체들 역시 제조업체에 대한 주문을 줄이게 된다."""
    
    @staticmethod
    def retailers_descr():
        return """[소매업 재고]
소매업체들은 잉여 재고의 수준을 떨어뜨리기 위해 다양한 판촉활동을 벌이기도 하는데, 그 효과가 나타나기까지 보통 3개월에서부터 9월 또는 그 이상의 시간이 소요될 수 있다."""
          
    @staticmethod    
    def retailers(mode='binary'):
        return (PlotEconomicIdx('RETAILIRSA').renameColumn('소매업 재고')
                .plot(title='소매업 재고', mode=mode, y1_title=''))
    @staticmethod
    def retailers_descr():
        return """[소매업 재고]
소매업체들은 잉여 재고의 수준을 떨어뜨리기 위해 다양한 판촉활동을 벌이기도 하는데, 그 효과가 나타나기까지 보통 3개월에서부터 9월 또는 그 이상의 시간이 소요될 수 있다."""    
          
    @staticmethod    
    def retailTradeExcludingVehicle(mode='binary'):
        return (PlotEconomicIdx('MRTSIR4400AUSS').renameColumn('소매업 토탈 자동차 제외')
                .plot(title='소매업 토탈 자동차 제외', mode=mode, y1_title=''))

    @staticmethod
    def motorVehicle(mode='binary'):
        return (PlotEconomicIdx('MRTSIR441USS').renameColumn('자동차 재고율')
                .plotWithMa(title='자동차 재고율', mode=mode, y1_title=''))
    @staticmethod    
    def furniture_home_furnishings(mode='binary'):
        return (PlotEconomicIdx('MRTSIR4423XUSS').renameColumn('가구업 재고율')
                .plot(title='가구업 재고율', mode=mode, y1_title=''))
        
    @staticmethod    
    def buildingMaterials(mode='binary'):
        return (PlotEconomicIdx('MRTSIR444USS').renameColumn('건축자재 재고율')
                .plot(title='건축자재 재고율', mode=mode, y1_title=''))

    @staticmethod
    def clothing(mode='binary'):
        return (PlotEconomicIdx('MRTSIR448USS').renameColumn('의류 재고율')
                .plotWithMa(title='의류 재고율', mode=mode, y1_title=''))
    @staticmethod    
    def food_beverage(mode='binary'):
        return (PlotEconomicIdx('MRTSIR445USS').renameColumn('식음료 재고율')
                .plot(title='식음료 재고율', mode=mode, y1_title=''))
        
    @staticmethod    
    def generalMrchandise(mode='binary'):
        return (PlotEconomicIdx('MRTSIR452USS').renameColumn('종합 소매업 재고율')
                .plot(title='종합 소매업 재고율', mode=mode, y1_title=''))

    @staticmethod
    def department(mode='binary'):
        return (PlotEconomicIdx('MRTSIR4521EUSS').renameColumn('백화점 재고율')
                .plotWithMa(title='백화점 재고율', mode=mode, y1_title=''))
    @staticmethod    
    def merchantWholesalers(mode='binary'):
        return (PlotEconomicIdx('WHLSLRIRSA').renameColumn('도매업 재고')
                .plot(title='도매업 재고', mode=mode, y1_title=''))
        
    @staticmethod    
    def manufacturers(mode='binary'):
        return (PlotEconomicIdx('MNFCTRIRSA').renameColumn('제조업 재고')
                .plot(title='제조업 재고', mode=mode, y1_title=''))

    @staticmethod
    def inventory_descr():
        return """[판매 및 재고 변화, 소매업-도매업-제조업]"""          
    
    @staticmethod
    def businessInventories(mode='binary'):
        return (PlotEconomicIdx('TOTBUSMPCIMSA').renameColumn('총기업 재고 변화')
                .plotWithMa(title='총기업 재고 변화', mode=mode, y1_title=''))
    @staticmethod    
    def retailersInventories(mode='binary'):
        return (PlotEconomicIdx('RETAILMPCIMSA').renameColumn('소매업 재고 변화')
                .plot(title='소매업 재고 변화', mode=mode, y1_title=''))
        
    @staticmethod    
    def merchantWholesalersInventories(mode='binary'):
        return (PlotEconomicIdx('WHLSLRMPCIMSA').renameColumn('도매업 재고 변화')
                .plot(title='도매업 재고 변화', mode=mode, y1_title=''))

    @staticmethod    
    def manufacturersInventories(mode='binary'):
        return (PlotEconomicIdx('MNFCTRMPCIMSA').renameColumn('제조업 재고 변화')
                .plot(title='제조업 재고 변화', mode=mode, y1_title=''))


