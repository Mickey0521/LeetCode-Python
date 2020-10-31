# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        # the edge case(s):                
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        
        # we insert a 'dummy head' before the new list
        dummy_node = ListNode(None)        
        # new linked list
        current_pointer= dummy_node
        # current_pointer -> dummy_node 
        
        while (l1 != None) and (l2 != None):
            # case 1
            if l1.val <= l2.val:
                current_pointer.next = l1
                l1 = l1.next
                current_pointer = current_pointer.next
                # current_pointer.next -> l1
                # l1 -> l1.next
                # current_pointer -> l1
            # case 2
            else:
                current_pointer.next = l2
                l2 = l2.next
                current_pointer = current_pointer.next
                # current_pointer.next -> l2
                # l2 -> l2.next
                # current_pointer -> l2

        if l1 == None:
            current_pointer.next = l2
        if l2 == None:
            current_pointer.next = l1

        return dummy_node.next
