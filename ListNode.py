# Definition for singly-linked list.
class ListNode:
    def _init_(self, val=0, siguiente=None):
        self.valor = val
        self.siguiente = siguiente
        
nodo = ListNode()
nodo.valor = 5

dummy = ListNode()  #Dummy es un objeto de la clase ListNode()
tail = dummy 

def twomergedlist(list1, list2):        
    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
                
            tail = tail.next
                
    if list1:
        tail.next = list1
    elif list2:
        tail.next = list2
        
    return print(dummy.next)

lista = ListNode()
lista2 = ListNode()


