# classe pessoa

class Pessoa(object) :
  nome = None
  sobrenome = None
  idade = None

  def andar(self, n):
    self.nome = n
    print("Eu {} estou andando".format(self.nome))
  def dormir(self):
    print("Estou dormindo")