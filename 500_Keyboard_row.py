keyboard = ["qwertyuiop", "asdfghjkl", "zxcvbnm" ]
lista_palabras = ["alaska","asa", "pedigri"]
listareturn = []


for elemento in range(len(keyboard)):
    print("elemento ", elemento+1, " de la lista keyboard")

    for letra in keyboard[elemento]:
        print(letra,end="")

    for elemento2 in range(len(lista_palabras)):
        print("\nLongitud de lista de palabras: ", len(lista_palabras))
        print("\nelemento ",elemento2+1, " de la lista word2: ")

        for letra in lista_palabras[elemento2]:
            print(letra, end=",")

    print("\n##########################")
print(listareturn)