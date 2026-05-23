# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1 and not list2:
            return None
        elif not list1:
            return list2
        elif not list2:
            return list1
        
        cur1 = list1
        cur2 = list2

        if cur1.val <= cur2.val:
            list3 = ListNode(cur1.val)
            cur1 = cur1.next
        else:
            list3 = ListNode(cur2.val)
            cur2 = cur2.next

        cur3 = list3
        while cur1 and cur2:
            
            if cur1.val<= cur2.val:
                cur3.next = ListNode(cur1.val)
                cur1 = cur1.next
                cur3 = cur3.next
            else:
                cur3.next = ListNode(cur2.val)
                cur2 = cur2.next
                cur3 = cur3.next
        
        if not cur1 and not cur2:
            return list3
        elif not cur1 and cur2:
            cur3.next = cur2
            return list3
        elif cur1 and not cur2:
            cur3.next = cur1
            return list3



                
                
                


        