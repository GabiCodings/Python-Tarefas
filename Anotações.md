> For:
- O for é muito utilizado para percorrer listas, ou contar até um X numero.

Exemplo de Codigo:
    > for item in lista: <

for = "para cada"
item = um nome que você escolhe para representar cada coisa da lista
in = "dentro de"
lista = a lista que você quer olhar
Dois pontos : = dizem ao Python que você vai começar um bloco de código
O que vem embaixo e com tab (ou espaço) é o que será feito com cada item

> Utilizando For em uma Lista:

nomes = ["Ana", "Pedro", "Lucas", "Alê"]

for nome in nomes:
    if nome.startswith("A"):
        print(nome, "começa com a letra A")

ele analisa cada parte da lista e mostra na tela apenas os nomes que começam com a letra "A"

> KEYWORDS para ajudar no for:

enumerate = usado pra enumerar posiçoes em uma lista
range = usado para contagens e repetir coisa em um espectro, ex: for i in range(5). conta de 0 até 4, como se criasse uma lista escondida.s