notas = [ ]
contador = 1
provao = 0


while contador < 5:
    notas.append (float(input("Digite uma Nota: ")))
    contador += 1

media = sum(notas) / len(notas)

def aprovar(notas, provao, media):
    
    if media >= 7:
        print("aprovado")
        
    else:
        notas.append (float(input("Qual sua nota do Provão? ")))
        provao = notas[len(notas) - 1]
        media = sum(notas) / len(notas)

        if media >= 5:
            print("Demorou mas você foi aprovado")
        else:
            print("Reprovado mesmo com o provão")


aprovar(notas, provao, media)
