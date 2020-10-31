# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        
        # edge cases
        if head == None:
            return head
        if head.next == None:
            return head
        
        dummy_head = ListNode(0)        
        current = dummy_head
    
        while (head != None) and (head.next != None):
            
            # swap
            tmp = head.next
            head.next = tmp.next
            tmp.next = head
                        
            current.next = tmp
            current = head
            head = head.next
    
        return dummy_head.next
