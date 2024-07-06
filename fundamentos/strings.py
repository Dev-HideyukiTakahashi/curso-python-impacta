
### fatiando de x:y-1 // omitindo valores reconhece o primeiro ou último caractere
fatiado = "Texto para ser fatiado"[0:6]
print(fatiado)
fatiado = "Texto para ser fatiado"[3:10]
print(fatiado)
#output: Texto 
#output: to para 


### invertendo string
fatiado = "Texto para ser fatiado"[::-1]
print(fatiado)
#output: odaitaf res arap otxeT


###string array é imutavel
nome = "Alex"
#nome[0] = "B"
#output: TypeError: 'str' object does not support item assignment

### solução
nome = "B" + nome[1:]
print(nome)
#output: Blex


#verificando primeiro caractere
print(nome.startswith("B"))
#output: True

#verificando último caractere
print(nome.endswith("r"))
#output: False

#trocando valores em string // obs String continua sendo imutável
#para mudar o valor seria: nome = nome.nome.replace("B", "A")
print(nome.replace("B", "A"))
#output: Alex

#split no python
texto = "Testando split no python"
texto2 = "maçã,banana,uva,abacaxi"
s = texto.split()
s2 = texto2.split(",")
print(s)
print(s2)
#output: ['Testando', 'split', 'no', 'python']
#output: ['maçã', 'banana', 'uva', 'abacaxi']


#join no python
data = ['18','05','1979']
print("/".join(data))
#output: 18/05/1979
