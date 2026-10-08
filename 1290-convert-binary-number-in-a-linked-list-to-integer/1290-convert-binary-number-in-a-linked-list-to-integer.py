# Definition for singly-linked list.  
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode | None) -> int:
        nodes = [] 
        curr = head 
        while curr:
            nodes.append(str(curr.val))
            curr = curr.next
            

        result = "".join(nodes)
        submit = int(result,2)
        return submit