Internet = float(input(f'Informe o valor gasto em internet: '))
mb = float(input(f'Informe a quantidade gasta de megabytes em internet: '))
LigacaoLocal = float(input(f'Informe o valor gasto em ligação local: '))
MinutosdeUsoLocal = float(input(f'Informe a quantidade de minutos na ligação local: '))
MinutosdeInterurbana = float(input(f'Informe a quantidade de minutos na ligação interurbana: '))
LigacaoInterUrbana = float(input(f'Informe o valor gasto em ligação interurbana: '))
Torpedo = float(input(f'Informe o valor gasto em torpedo: '))
QuantidadedeTorpedos = float(input(f'Informe a quantidade de torpedos feitos: '))

ValorInternet = Internet + (mb * 0.50)
ValorLigacaoLocal = LigacaoLocal + (MinutosdeUsoLocal * 0.35)
ValorLigacaoInterUrbana = LigacaoInterUrbana + (MinutosdeInterurbana * 0.60)
ValorTorpedo = Torpedo + (QuantidadedeTorpedos * 0.20)
DescontoInternet = ValorInternet * 0.05
DescontoLocal = ValorLigacaoLocal * 0.1
DescontoInterurbana = ValorLigacaoInterUrbana * 0.1
DescontoTorpedo = ValorTorpedo * 0.2

if mb > 50:
    float(print(f'Valor da internet com desconto de 5% é de {ValorInternet - DescontoInternet:.2f}.'))
else:
    print(f'Não obteve desconto na internet.')
if MinutosdeUsoLocal > 200:
    (print(f'Valor da ligação local com desconto de 10% é de {ValorLigacaoLocal - DescontoLocal:.2f}.'))
else:
    print(f'Não obtve desconto na licação local.')
if MinutosdeInterurbana > 150:
    float(print(f'Valor da ligação interurbana com desconto de 10% é de {ValorLigacaoInterUrbana - DescontoInterurbana:.2f}.'))
else:
    print(f'Não obtve desconto na licação interurbana.')
if QuantidadedeTorpedos > 50:
    float(print(f'O valor do torpedo com desconto de 20% é de {ValorTorpedo - DescontoTorpedo:.2f}.'))
else:
    print(f'Não obteve desconto no torpedo.')