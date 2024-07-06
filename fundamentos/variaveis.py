
### No python não é necessário informar o tipo da variável ###

a = 10
print(a)
print(type(a))
#output: 10
#output: <class 'int'>


### Conversão ###

var1 = "nome"
print(var1 + a)
#output: TypeError: can only concatenate str (not "int") to str
print(var1 + str(a))
#output: nome10
