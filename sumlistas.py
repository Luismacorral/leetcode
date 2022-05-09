class Solution:
    
    def addTwoNumbers(self, l1, l2):
        
        l1_reversed= l1[::-1]
        l2_reversed= l2[::-1]
                
        strings = [str(integer) for integer in l1_reversed]
        a_string = "".join(strings)
        l1_int = int(a_string) 
        
        strings2 = [str(integer) for integer in l2_reversed]
        b_string = "".join(strings2)
        l2_int = int(b_string) 
       
        suma = l1_int + l2_int     

        digit_string = str(suma)
        digit_map = map(int, digit_string)
        digit_list = list(digit_map)
        
        digit_list_reversed = digit_list[::-1]
        return digit_list_reversed

lista1 = Solution()
lista2 = Solution()
listanum1 = [9,9,9]
listanum2 = [9,9,9,9,9,9,9,9,9]

print(lista1.addTwoNumbers(listanum1, listanum2))
print("#############################")
lnext = listanum1.next
print(lnext)