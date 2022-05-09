#Esta me funciona supuestamente aquí pero no se la traga leetcode
def removeElements(lista, val):
    puntero = 0
    result = []
    for i in range(0,len(lista)):
        if lista[i] == val:
            print("lista[i]:", lista[i])
            puntero +=1
            print("puntero: ", puntero)
        else:
            result.append(lista[i])
    return (abs(len(lista)-puntero)), result

#Esta sí funciona en leetcode
def removeElements2(lista, val):
    while val in lista:
        lista.remove(val)
    return len(lista)

    

l1 = [3,2,2,3]
valor = 3

l2 = [0,1,2,2,3,0,4,2]
valor2 = 2

#removeElements(l1,valor)

print(removeElements2(l2, valor2))