
from pessoa import Pessoa
from carros import Carro
from carros import Fusca
from carros import Ferrari

p = Pessoa()
p.andar("João")
#output: Eu João estou andando


c = Carro("avenida")
c.andar()
# output: Andando pela avenida


fusca = Fusca("praia")
print(type(fusca))
#output: <class 'carros.Fusca'>
fusca.correr()
#output: Andando pela pista


ferrari = Ferrari("rua")
ferrari.andar()
#output: Correndo muito


