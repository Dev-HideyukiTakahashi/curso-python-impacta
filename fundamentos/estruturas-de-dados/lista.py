# lista é representada por colchetes
lista = [1,2,3,4,5]

print(lista)
print(lista[2])
#output: [1, 2, 3, 4, 5]
#output: 3

# percorrendo com laço de repetição
for item in lista:
  print(item)
#output: 1
#output: 2
#output: 3
#output: 4
#output: 5


# adicionando novo valor, removendo o último
lista.append("7")
print(lista)
#output: [1, 2, 3, 4, 5, 7]
lista.pop()
print(lista)
#output: [1, 2, 3, 4, 5]


# podemos ter varios tipos na lista
lista.append("João")
print(lista)
#output [1, 2, 3, 4, 5, 'João']


#removendo específicamente
lista.remove(2)
print(lista)
#output: [1, 3, 4, 5, 'João']


# o sort só funciona se for todos do mesmo tipo
#lista.sort()
#output: TypeError: '<' not supported between instances of 'str' and 'int'

lista.remove("João")
lista.sort()
print(lista)
#output: [1, 3, 4, 5]

