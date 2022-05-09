
def isValid(s):
    
    cadena = []

    diccionario ={
        ']':'[',
        ')':'(',
        '}':'{'
    }
    
    for i in s:
        
        if i == "[" or i == "(" or i == "{":
            cadena.append(i)
            print("Cadena: ", cadena)
        else:
            if len(cadena) == 0 or cadena.pop(-1) != diccionario[i]:
                print("Cadena después del else: ", cadena)
                return False
            print(cadena)

    


varcadena = "()()()[]]"

print(isValid(varcadena))

