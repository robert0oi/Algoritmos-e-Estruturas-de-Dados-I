# Construa uma função que possa ser utilizada com a função MAP do Python. Utilize esta função através da função MAP

def utilizarFuncaoMap(a):
    return len(a)

x = map( utilizarFuncaoMap, ('twingo', 'doblò', 'clio', 'mégane'))
print(x)
print(list(x))

