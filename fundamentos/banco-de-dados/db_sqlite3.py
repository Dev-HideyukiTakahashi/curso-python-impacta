#sqlite3 já vem nativo com python
import sqlite3

#abrindo conexão
connection = sqlite3.connect("galeria.db")

#cursores para navegar a manipular registros do banco de dados
cursor = connection.cursor()


#criando tabela
def criar_tabela():
  sql = """
  CREATE TABLE albums
  (titulo text, artista text, data_lancamento text, data_publicacao text, midia text)
  """
  #executando comando sql
  cursor.execute(sql)
  #efetivando alteração,inclusão ou exclusão
  connection.commit()


#inserindo 1 
def grava_album():
  sql = """
  INSERT INTO albums
  VALUES
  ('Glow','Andy Hunter','24/07/2012','Xplore Records', 'MP3')
  """
  cursor.execute(sql)
  connection.commit()


#inserindo muitos
def grava_muitos():
  albums = [
    ('Exodus', 'Andy Hunter', '09/07/2002', 'Sparrow Records', 'CD'),
    ('Until We Have Faces', 'Red', '01/02/2011', 'Essential Records', 'CD')]
  
  cursor.executemany("INSERT INTO albums VALUES(?,?,?,?,?)",albums)
  connection.commit()

def atualiza():
  sql = """
  UPDATE albums
  SET artista = 'John Doe'
  WHERE artista = 'Andy Hunter'
  """
  cursor.execute(sql)
  connection.commit()

def excluir():
  sql = """
  DELETE FROM albums
  WHERE
  artista = 'Red' 
  """
  cursor.execute(sql)
  connection.commit()

def listar():
  sql = """
  SELECT rowid, *
  FROM albums
  ORDER BY artista
  """
  cursor.execute(sql)
  for row in cursor.fetchall():
    print(row)