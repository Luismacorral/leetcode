
def removerduplicados(lista):
    ultimopuntero = 0
    for i in range(1,len(lista)):
        if lista[ultimopuntero] != lista[i]:
            ultimopuntero +=1
            lista[ultimopuntero] = lista[i]

    return print(abs((ultimopuntero + 1) - len(lista)))

l1 = [1,1,2,2,3,3]
removerduplicados(l1)
