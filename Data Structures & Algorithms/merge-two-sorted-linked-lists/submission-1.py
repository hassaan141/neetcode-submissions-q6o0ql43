# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = None
        curr1, curr2 = list1, list2

        if curr1 == None and curr2 != None:
            return curr2
        elif curr1 != None and curr2 == None:
            return curr1
        elif curr1 == None and curr2 == None:
            return head

        if curr1.val <= curr2.val:
            head = ListNode(curr1.val)
            curr1 = curr1.next
        else:
            head = ListNode(curr2.val)
            curr2 = curr2.next
        
        tail = head
        while curr1 and curr2:
            if curr1.val <= curr2.val:
                tail.next = ListNode(curr1.val)
                curr1 = curr1.next
            else:
                tail.next = ListNode(curr2.val)
                curr2 = curr2.next
            
            tail = tail.next
                
        if curr1 == None:
            tail.next = curr2

        elif curr2 == None:
            tail.next = curr1
        elif curr1 and curr2 == None:
            return head

        return head
                
            


        
