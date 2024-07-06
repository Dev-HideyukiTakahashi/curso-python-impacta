# dictionary são representados por colchetes
# o padrão json é convertido para dictionary
# chave , valor

d = {}
print(type(d))
#output: <class 'dict'>

d['nome'] = "João"
d['sobrenome'] = "Silva"
print(d)
#output: {'nome': 'João', 'sobrenome': 'Silva'}

d['idade'] = 25
d['telefone'] = '1199999999'
print(d)
#output: {'nome': 'João', 'sobrenome': 'Silva', 'idade': 25, 'telefone': '1199999999'}


#removendo item
d.pop("idade")
print(d)
#output: {'nome': 'João', 'sobrenome': 'Silva', 'telefone': '1199999999'}

print(d.keys())
#output: dict_keys(['nome', 'sobrenome', 'telefone'])

print(d.values())
#output: dict_values(['João', 'Silva', '1199999999'])