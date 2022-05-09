class ListNode:
    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(ListNode):
    def deleteDuplicates(self, head):
        dummy = ListNode()
        tail = dummy
        
        while head:
            if head.val == tail.next:
                print("Hola")
                
            else:
                head.val = head.next
        return dummy.next

lista = [1,1,3]
varClase = Solution()
varClase.deleteDuplicates(lista)
print(lista)