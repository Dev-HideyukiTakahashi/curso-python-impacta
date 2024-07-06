import requests
from enderecos import Endereco
import json

cep = input("Digite o cep: ")
r = requests.get("https://viacep.com.br/ws/{}/json".format(cep) )

#checando se o http retornou código 200 ou OK
if r.status_code == requests.codes.ok:
  #pegando o resultado e armazenando como um dictionary(chave/valor)
  j = json.loads(r.text)

  #passando a chave como referência para guardar o valor no objeto endereço
  endereco = Endereco()
  endereco.cep = j['cep']
  endereco.logradouro = j['logradouro']
  endereco.complemento = j['complemento']
  endereco.bairro = j['bairro']
  endereco.localidade = j['localidade']
  endereco.uf = j['uf']
  endereco.unidade = j['unidade']
  endereco.ibge = j['ibge']
  endereco.gia = j['gia']

  endereco.salvar()
else:
  print("Cep não encontrado!")  