from typing import Optional


class ListNode:
    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


    def mergeTwoLists(self, list1, list2):
        
        dummy = ListNode()  #Dummy es un objeto de la clase ListNode() y es un nodo ficticio
        tail = dummy #Tail apunta al nodo ficticio dummy
        
        while list1 and list2: #Mientras las listas no sean null
            if list1.val < list2.val:  #Si el valor del nodo de lista1 es menor que el valor del nodo de lista2
                tail.next = list1  #Tomamos el valor del nodo de lista1 y lo insertamos en tail, de modo que el siguiente punto de cola sea el nodo en sí mismo
                list1 = list1.next #Actualizamos el puntero de lista1
            else: #Si el valor del nodo de lista2 es menor que el nodo de lista1
                tail.next = list2 #Tomamos el valor del nodo de lista2 y lo insertamos en tail
                list2 = list2.next #Actualizamos el puntero de lista2
            
            tail = tail.next #Actualizamos el puntero de cola
        
        #En el caso de que una de las listas esté vacía (null)
        if list1: #Si lista1 no está vacia...
            tail.next = list1 #El siguiente punto de cola será igual a list1
        elif list2: #Si lista2 no está vacia...
            tail.next = list2 #El siguiente punto de cola será igual a list2
        
        return dummy.next


listaA = [1,2,4]
listaB = [1,3,4]

mergelists = ListNode()
print(mergelists.mergeTwoLists(listaA,listaB))