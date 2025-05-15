print("Calculando sua comição!!!!!")
#declarando variaveis
nome=(input("Informe seu nome: "))
salariofixo=float(input("Informe seu salário: "))
vendas= int(input("Informe sua quantidade de vendas: "))
comissao= salariofixo* 0.15
salariototal= salariofixo+ comissao
if vendas>=20:
    print(f"{nome} Sua meta foi atingida, Seu salário é: {salariototal} R$. ")
else:
    print(f"{nome } Você nao atingiu a quantidade de vendas do mês, Seu salário é: {salariofixo} R$.")
