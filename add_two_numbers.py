# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        # important: always point to the head (virtual node)
        dummy_head = ListNode(None)
        # current -> dummy_head
        current = dummy_head
        
        overflow = 0
        # be careful: the while loop uses 'or'
        while (l1 != None) or (l2 != None):

            # if one list is longer than another
            # create the '0' ListNode
            if l1 == None:
                l1 = ListNode(0)
            if l2 == None:
                l2 = ListNode(0)
            
            # handle the overflow problem
            my_sum = l1.val + l2.val + overflow
            if my_sum >= 10:
                my_sum = my_sum -10
                overflow = 1
            else:
                overflow = 0
            
            # move the pointers
            current.next = ListNode(my_sum)
            current = current.next
            l1 = l1.next
            l2 = l2.next
        
        # the edge case 
        if overflow == 1:
            current.next = ListNode(1)            
        
        # return the linked list
        return dummy_head.next
