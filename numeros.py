numeros = [22.5, 40, 13, 29, 34]
par = [ ]
impar = [ ]

print("Nós vamos somar essa sequencia: ", numeros)

if len(numeros) % 2 == 0:
    par.append (numeros)
else:
    impar.append (numeros)

soma_par = sum(par)
soma_impar = sum(impar)

print("A soma dos pares da sequencia são iguais à: ", soma_par)
print("A soma dos impares da sequencia são iguais à: ", soma_impar)
#adicionar um for pra funcionar