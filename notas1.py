notas = [ ]
contador = 1

while contador < 5:
    notas.append (float(input("Digite uma nota: ")))
    contador += 1

media = sum(notas) / len(notas)
maior = max(notas)
menor = min(notas)

print("sua media é", media)
print("sua maior nota é:", maior)
print(" Sua Menor nota é: ", menor)