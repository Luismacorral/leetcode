pila = []
dic = {
   ']' : '[',
   ')' : '(',
   '}' : '{'
    }

cadena=["[","]","(",")"]
resultado = True
'''for c in cadena:
    if c == "[" or c == "(" or c =="{":
        pila.append(c)
    else:
        if len(pila) == 0 or pila.pop(-1) != dic[cadena]:
            print(dic[cadena])
            resultado = False
'''
for i in dic:
    print(dic[i])
