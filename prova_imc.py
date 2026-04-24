peso = int(input("digite o seu peso: "))
altura = float(input("digite a sua altura: "))
IMC = peso / (altura ** 2)
print(f"IMC: {IMC:.2f}")

if IMC < 18.4:
    print("Abaixo do peso ")
elif IMC < 24.9:
    print("Peso normal")
elif IMC < 29.9:
    print("Sobrepeso")
elif IMC < 34.9:
    print("Obesidade Grau I")
elif IMC < 39.9:
    print("Obesidade Grau II")
else:
    print("Obesidade Grau III(mórbida)")

if IMC >= 30.0:
    print("cuidado com a saúde!")