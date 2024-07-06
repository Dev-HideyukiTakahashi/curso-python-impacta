class Carro(object):

  def __init__(self, caminho):
    self.caminho = caminho
  
  def andar(self):
    print("Andando pela", self.caminho)

class Fusca(Carro):

  def __init__(self, caminho):
    super().__init__(caminho)

  def correr(self):
    self.caminho = "pista"
    super(Fusca, self).andar()

class Ferrari(Carro):

  def __init__(self, caminho):
    super().__init__(caminho)

  def andar(self):
    print("Correndo muito")
