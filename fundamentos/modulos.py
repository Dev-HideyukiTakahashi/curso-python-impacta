import random

### número aleatório entre 0 e 1
print(random.random())
#output: 0.43892136634244105


### número aleatório entre 10 e 20
print(random.randint(10,20))
#output: 14


### retorna elemento aleatório de uma lista
x = ["Gol", "Astra", "Fusca", "Palio", "Uno"]
print(random.choice(x))
#output: Astra
random.shuffle(x)
print(x)
#output:['Palio', 'Gol', 'Uno', 'Astra', 'Fusca']


import string

print(string.punctuation)
#output: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
print(string.digits)
#output: 0123456789

