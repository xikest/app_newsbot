from market.macro.plotviz_economic_indicator import PlotEconomicIdx

class AdpNationalEmploymentReport:
    @staticmethod
    def descr():
        return """-ADP 전미 고용 보고서-
[채권 시장]
경제가 침체기나 약화 국면에서 회복하고 있는 시기에 대규모 고용이 발생하였다면 채권 투자자들은 그다지 동요하지 않을 것이다.
그러나 경제 호황 및 고용 성장이 몇 년 동안 꾸준히 이어지고 있는 상황에서 동일한 내용의 보고서가 발표되면 강력한 고용 동향을 보여줄 것이라는 우려로 채권 시장에 부정적인 영향을 줄 수 있다.
경기 확장이 상당히 오래 진행된 후에 나타는 고용의 증가는 노동시장과 산업부문에 압력을 가하게 되며, 그 결과 임금상승과 상품가격 인상 등이 유발되면서 FED의 시장 개입을 발생시킬 수 있다.\

[주식 시장]
활발한 고용 증가에 대한 기대는 소비자의 구매력을 증가시켜 긍정적인 상황을 만들어 낸다. 하지만인플레이션 압력을 증가시킬 수 있다는 가능성을 가지고 있다.

[외환 시장]
일반적으로 월간 비농업 민간사업장에서 고용이 평균 150,000명 이상 증가하면 미국 내 금리동결을 발생시킬 수 있으며, 달러 표시 자산은 매력적인 투자대상이 된다.
월간 고용증가율이 100,000명 이하에 불과하다면, 이는 경기하강 또는 약화를 의미하며, 향후 금리가 인하할 것이라고 생각될 수 있다. 이로 인해 달러 가치가 하락할 수 있다."""

    
    @staticmethod
    def nonfarmPrivatePayrollEmployment(mode='binary'):
        return (PlotEconomicIdx('NPPTTL').renameColumn('전체 비농업 민간 부문')
                .plot(title='전체 비농업 민간 부문', mode=mode, y1_title=''))
    @staticmethod
    def nonfarmPrivateManufacturingPayrollEmployment_descr():
        return """제조업은 서비스 부문에 비해 경기의 순환에 훨씬 더 민감한 반응을 보인다."""    
    
    @staticmethod    
    def nonfarmPrivateManufacturingPayrollEmployment(mode='binary'):
        return (PlotEconomicIdx('NPPMNF').renameColumn('Nonfarm: 제조업')
                .plot(title='Nonfarm: 제조업', mode=mode, y1_title=''))
        
    @staticmethod
    def nonfarmPrivateSmallPayrollEmployment_descr():
        return """[소규모 기업 고용 (1 - 49)]
소규모 생산 업체들은 대기업에 비해 고용과 해고에 더욱 민첩하게 움직이는 경향이 있다.
이들의 고용 패턴 변화는 경제의 터닝 포인트를 예측하게 해주는 중요한 선행지표로 간주될 수 있다."""   

    @staticmethod    
    def nonfarmPrivateSmallPayrollEmployment(mode='binary'):
        return (PlotEconomicIdx('NPPTS').renameColumn('소규모 기업 고용 (1~49)')
                .plot(title='소규모 기업 고용(1~49)', mode=mode, y1_title=''))

    @staticmethod
    def nonfarmPrivateMediumPayrollEmployment_descr():
        return """[중규모 기업 고용 (50 - 499)]
중규모 생산 업체들은 대기업에 비해 고용과 해고에 더욱 민첨하게 움직이는 경향이 있다."""   
        
    @staticmethod    
    def nonfarmPrivateMediumPayrollEmployment(mode='binary'):
        return (PlotEconomicIdx('NPPTM').renameColumn('중규모 기업 고용 (50 - 499)')
                .plot(title='중규모 기업 고용 (50 - 499)', mode=mode, y1_title=''))
    @staticmethod    
    def nonfarmPrivateLargePayrollEmployment(mode='binary'):
        return (PlotEconomicIdx('NPPTL2').renameColumn('대규모 기업 고용 (1000+)')
                .plot(title='대규모 기업 고용 (1000+)', mode=mode, y1_title=''))
        
