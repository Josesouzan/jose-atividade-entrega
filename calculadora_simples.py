opcao=int
while opcao !=0:
    print("###########calculdora simples@@@@@@@@@@@@@") 
    print("1----SOMAR")
    print("2----SUBTRAIR")
    print("3----MULTIPLICAR")
    print("4----DIVIDIR")
    print("0----SAIR")
    opcao=int(input("Escolha uma opção: "))
    if opcao==1:
        numero1=int(input("Digite o primeiro numero: "))
        numero2=int(input("Digite o segudo numero: "))
        resultado=numero1+numero2
        print(resultado)
    elif opcao==2:
        numero1=int(input("Digite o primeiro numero: "))
        numero2=int(input("Digite o segudo numero: "))
        resultado=numero1-numero2
        print(resultado)
    elif opcao==3:
        numero1=int(input("Digite o primeiro numero: "))
        numero2=int(input("Digite o segudo numero: "))
        resultado=numero1*numero2
        print(resultado)
    elif opcao==4:
        numero1=int(input("Digite o primeiro numero: "))
        numero2=int(input("Digite o segudo numero: "))
        resultado=numero1/numero2
        print(resultado)
    else:
        print("Desculpe não entendi você digitou errado. ")
    