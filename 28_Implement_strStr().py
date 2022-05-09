def strStr(cadena1, cadena2):
    if cadena2 == "":
        return 0
    if cadena2 not in cadena1:
        return -1
    for i in range(0,len(cadena1)):
        for j in cadena2:
            if cadena1[i] == j:
                return i


                

           

c1 = "mississippi"
c2 = "issip"

print(strStr(c1, c2))
            
