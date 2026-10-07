# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        curr = head
        count = 0
        while curr: #counts number of nodes
            curr = curr.next
            count += 1 

        stop = count // 2 #identifies the middle 
        

        curr2 = head
        for i in range(stop):
            curr2 = curr2.next

        return curr2
           

        
        