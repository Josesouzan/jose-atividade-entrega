#COLOCANDO VALORES DE VARIAVEIS
print("##SEJAM MUITO BEM VINDOS A LOCADORA DE VELICULOS.##")
print("Tabela de preços. ")
print("Carro simples R$90,00 a diaria, mais R$0,20 reais o km rodado..")
diaria=int(input("Informe a quantidade de diaria: "))#variavel diaria sendo atribuido valores
km=float(input("Informe a quilometragem ultilizada. "))#variavel km sendo atribuido valores
total=(diaria*90)+(km*0.20)
diariatotal=diaria*90
kmtotal=km*0.20
print(f"Total a ser pago é: {total}R$ ")
print(f"{diaria} diarias no valor de:{diariatotal}R$.")
print(f"{km} kms Ultilizados no valor de: {kmtotal}R$")