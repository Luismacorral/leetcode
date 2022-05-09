
fila1 = ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "q", "w", "e", "r", "t", "y", "u", "i", "o", "p"]
fila2 = ["A", "S", "D", "F", "G", "H", "J", "K", "L", "a", "s", "d", "f", "g", "h", "j", "k", "l"]
fila3 = ["Z", "X", "C", "V", "B", "N", "M", "z", "x", "c", "v", "b", "n", "m"]
  
words = ["lasa", "tasa"]
resultado = []
   
# Recorremos cada palabra en la lista words
for palabra in words:

    # a flag to track which row each letter in a word is in. If all in row1, the sum of flag will be 1
    flag = [0,0,0]

    for letra in palabra:

        if letra in fila1:
            flag[0] = 1
        elif letra in fila2:
            flag[1] = 1
        elif letra in fila3:
            flag[2] = 1
    if sum(flag) == 1:
        resultado.append(palabra)
        

print(resultado)