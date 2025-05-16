quantidadefrances=0
quantidadeintegral=0
quantidadepaodoceliso=0
quantidadepaodocefarofa=0
quantidadepaodeforma=0
frances=0
integral=0
paodoceliso=0
paodocefarofa=0
paodeforma=0
while True:
    print("########padaria do grau########")
    print("[1] PÃO FRANCÊS.")
    print("[2] PÃO INTEGRAL.")
    print("[3] PÃO DOCE LISO.")
    print("[4] PÃO DOCE FAROFA.")
    print("[5] PÃO DE FORMA.")
    print("[6]PARA FINALIZAR A COMPRA.")
    opcao =int(input("ESCOLHA SUA OPÇÃO:"))
    if opcao ==1:
        quantidadedepao=int (input("escolha quantidade de pão francês. "))
        valordopao=1.04
        quantidadefrances=quantidadedepao+quantidadefrances
        frances=frances+(quantidadedepao*valordopao)
    elif opcao ==2:
        quantidadedepao= int (input("escolha quantidade de pão integral. "))
        valordopao=1.04
        quantidadeintegral=quantidadedepao+quantidadeintegral
        integral=integral+(quantidadedepao*valordopao)
    elif opcao ==3:
        quantidadedepao=int(input("escolha quantidade de pão doce liso . "))
        valordopao=1.08
        quantidadepaodoceliso=quantidadedepao+quantidadepaodoceliso
        paodoceliso=paodoceliso+(quantidadedepao*valordopao)
    elif opcao ==4:
        quantidadedepao=int(input("escolha quantidade de pão doce farofa . "))
        valordopao=1.11
        quantidadepaodocefarofa=quantidadedepao+quantidadepaodocefarofa
        paodocefarofa=paodocefarofa+(quantidadedepao*valordopao)
    elif opcao ==5:
        quantidadedepao=int(input("escolha quantidade de pão de forma . "))
        valordopao=0.95
        quantidadepaodeforma=quantidadedepao+quantidadepaodeforma
        paodeforma=paodeforma+(quantidadedepao*valordopao)
    elif opcao ==6:
        valortotal=frances+integral+paodoceliso+paodocefarofa+paodeforma
        totaldepaes=quantidadefrances+quantidadeintegral+paodoceliso+paodocefarofa+paodeforma
        break
    else:
        print("opcao invalida tente novamente. ")
print("\ncupon fiscal. ")
if frances>0 and quantidadefrances>0:
    print(f"quantidade de pão frances--- {quantidadefrances}----{frances:.2f}R$.")#atenção para repetiçao de aspas"" " ""
if integral>0 and quantidadeintegral>0:
    print(f"quantidade de pão integral--- {quantidadeintegral}----{integral:.2f}R$.")
if paodoceliso>0 and quantidadepaodoceliso>0:
    print(f"quantidade de pão doce liso--- {quantidadepaodoceliso}----{paodoceliso:.2f}R$.")
if paodocefarofa>0 and quantidadepaodocefarofa>0:
    print(f"quantidade de pão doce farofa--- {quantidadepaodocefarofa}----{paodocefarofa:.2f}R$.")
if  paodeforma>0 and quantidadepaodeforma>0:
    print(f"quantidade de pão de forma ---{quantidadepaodeforma}----{paodeforma:.2f}R$.")
if  valortotal>0 and totaldepaes>0:
    print(f"\nquantidade total de  pães --- {totaldepaes}----{valortotal:.2f}R$.")#:.2f quebra de decimal
        
