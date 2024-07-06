### Recebendo 2 números e mostrando a soma ###

a = int(input("Digite o valor 1: "))
b = int(input("Digite o valor 2: "))
print(a+b)


### Imprimindo com python ###

# Python já adiciona 'espaço' entre as palavras
print("Imprimindo", "com", "Python")
#output: Imprimindo com Python

# Marcadores
nota = 9.8
materia = "Programação"
print(f"Eu tirei {nota:,.2f} na prova de {materia}.")
#output: Eu tirei 9.80 na prova de Programação.
print("Valor da pizza: %.2f" %39.85222)
#output: Valor da pizza: 39.85
print("Teste de %s, para dia %d. Float %.3f" %("marcadores",4,25.38444))
#output: Teste de marcadores, para dia 4. Float 25.384