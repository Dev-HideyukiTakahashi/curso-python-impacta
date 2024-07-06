def somar (numero1, numero2):
  print(numero1 + numero2)

somar(5,5)
#output: 10

def subtrair(numero1, numero2):
  return numero1 - numero2

print(subtrair(12,5))
#output: 7

### Boas praticas
# no lugar de passar varios param, passar **kwargs para evitar erros
def imprime_parametros(**kwargs):
  for key, value in kwargs.items():
    print("%s = %s " %(key,value))

imprime_parametros(nome="João", sobrenome="Silva", idade= 55)
#output: nome = João
#output: sobrenome = Silva
#output: idade = 55