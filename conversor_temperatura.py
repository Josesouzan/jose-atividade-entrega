opcao = int
while opcao !=0:
    print("########VAMOS CONVERTER A TEMPERATURA######## ")
    print("1 ---- Para converter Celsius em Fahrenheit:")
    print("2 ---- Para converter Celsius em Kelvin: ")
    print("0 ----Para sair. ")
    opcao= int(input("escolha uma opação: "))
    if opcao ==1:
        temperaturainicial=float(input("Informe a temperatura a ser convertida: ")) #variavel temperatura sendo atribuido valores 
        celsiusfahrenheit= (temperaturainicial*9/5)+32
        print(f"a temperatura é: {celsiusfahrenheit}") 
    elif opcao==2:
        temperaturainicial=float(input("Informe a temperatura a ser convertida: "))#variavel temperatura sendo atribuido valores 
        celsiuskelvin=temperaturainicial+273.15
        print(f"A temperatura é: {celsiuskelvin} ")
    else:
        print("ERRO DE DIGITAÇÃO TENTE NOVAMENTE: ")        

