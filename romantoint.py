class Solution:

    def romanoToInt(self, romano:str) -> int:

        diccionario = {"I":1, "V": 5, "X": 10, "L":50, "C": 100, "D": 500, "M": 1000, "IV": -2, "IX": -2, "XL": -20, "XC": -20, "CD": -200, "CM": -200 }
        
        suma = 0
      
        for simbolo, valor in diccionario.items():
            
            suma += romano.count(simbolo) * valor
            
        return print("El número convertido es: ", suma)


romano = Solution()
print(romano.romanoToInt("IX"))