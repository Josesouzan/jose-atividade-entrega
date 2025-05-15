nome= (input("digite de nome: "))
peso= float(input("digite seu peso: "))
altura=float(input("digite sua altura:"))
imc=peso/(altura*altura)
if imc<18.5:
    print(f"{imc:.2f} Você esta abaixo do peso.")
elif imc>=18.5 and imc<=24.9:
    print(f"Seu imc é: {imc:.2f}  Você esta com seu peso normal. ")
elif imc>=25.0 and imc<=29.9:
    print(f" Seu imc é: {imc:.2f} Você esta com sobre peso. ")
else:
    print(f" Seu imc é: {imc:.2f} Você esta com obesida. ")
    