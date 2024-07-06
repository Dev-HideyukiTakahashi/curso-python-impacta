import sqlite3

class Endereco(object):

  def __init__(self):
    self.cep = None
    self.logradouro = None
    self.complemento = None
    self.bairro = None
    self.localidade = None
    self.uf = None
    self.unidade = None
    self.ibge = None
    self.gia = None

  def cria_tabela(self):
    connection = sqlite3.connect("enderecos.db")
    cursor = connection.cursor()
    sql = """
    CREATE TABLE IF NOT EXISTS endereco
    (cep text, logradouro text, complemento text, bairro text, localidade text, uf text, unidade text, ibge text, gia text)
    """
    cursor.execute(sql)
    connection.commit()


  def salvar(self):
    self.cria_tabela()
    connection = sqlite3.connect("enderecos.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO endereco VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s')" %
                  (self.cep, self.logradouro, self.complemento,self.bairro,self.localidade,self.uf,self.unidade,self.ibge,self.gia))
    connection.commit()
    print("CEP: {} encontrado e salvo com sucesso!".format(self.cep))
    
