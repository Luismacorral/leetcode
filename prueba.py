#Asignando un valor entero
a=2
print(a)
#Revisamos si el entero es un objeto o no lo es
print(isinstance(a,object))
#Asignamos un valor de cadena
b = "Bob"
print(b)
#Chequeamos si la cadena es un objeto o no lo es
print(isinstance(b,object))
#Asignamos una lista de valores
inputList = (1,2,3)
print(inputList)
#Chequeamos si la lista es un objeto o no lo es
print(isinstance(inputList,object))
#Asignamos un set de valores
inputSet = (10,20,30)
print(inputSet)
#Chequeamos si es un objeto o no lo es
print(isinstance(inputSet,object))
#Asignamos una tupla de valores
tupla = (100,200,300)
print(tupla)
#Chequeamos si es un objeto o no lo es
print(isinstance(tupla,object))
#Asignamos un diccionario de valores
diccionario = {
    "0":1922,
    "1":"BMW",
    "2":1000
}
print(diccionario)
#Chequeamos si es un objeto o no lo es
print(isinstance(diccionario, object))

cadena = "Hola Mundo"
nuevacadena = cadena.replace('H', '@')
print(nuevacadena)

strs=["autobus", "autoplano", "autocaravana","automovil", "autogiro", "autoz"]
strs2 = ["123", "456", "001", "999"]
k = max(strs2)
k2 = max(strs2)
print("minimo de la lista strs2: ", k)
print("máximo de la lista strs2: ", k2)
#print(strs[0])
#print(strs[1])
#print(strs[2])
#def cstrs(string):
#return os.path.commonprefix(strs)

ans = ''
n = len(min(strs))
print("n: ", n)

cadenadevuelta = ""
'''
for i in strs:
    for j in i:
        print(j, end="-")
    print("\n",i)


def longestCommonPrefix(self, strs: list[str]) ->str:
    ans = ''
    n = len(min(strs))
    for i in range(n):
        if all(x[i]==strs[0][i] for x in strs):
            ans = ans + strs[0][i]
        else:
            break
    return ans 

print(longestCommonPrefix(strs)) 

    
x1=(10,20,30,40,50)
for var in x1:
    print("index " + str(x1.index(var)) + ":", var)



x2=[(1,2),(3,4),(5,6)]

for a, b in x2:
    print(a, " plus ", b, " equals ", a+b)

diccionario ={
    'ABC' : 123,
    'DEF' : 456,
    'GHI' : 789
}

for key, value in diccionario.items():
    print(key + " : " + str(value))

'''