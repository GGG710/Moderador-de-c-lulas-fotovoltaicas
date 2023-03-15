consumomedio = float(input("Digite seu consumo diário em KWh: "))

tipodeligaçao = float(input("Digite o tipo de ligação,(monofásico:30KWh)(Bifásico:50KWh)(Trifásico:100KWh): "))

projeto = consumomedio - tipodeligaçao

print("Projeto =",projeto,"KWh")
consumodiario = projeto / 30
print("Consumo diário =",consumodiario,"KWh")

irradiaçao = float(input("Digite o valor da irradiaçao em KWh/m² dia: "))

print(irradiaçao,"KWh/m² dia")

sistema = consumodiario / irradiaçao
print(sistema,"KWp")

potencia = float(input("Digite a potência do módulo FV em Wp: "))
print(potencia,"Wp")

quantidademodulos = sistema *1000 / potencia
print("A quantiade de módulos é:",quantidademodulos)
