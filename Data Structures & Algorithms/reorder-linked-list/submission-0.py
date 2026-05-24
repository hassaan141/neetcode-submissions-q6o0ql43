# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # [ 2, 4, 6, 8, 10]


        if not head:
            return None

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next

            if fast.next.next:
                fast = fast.next.next
            else:
                fast = fast.next


        # Reverse the second half of the linked list
        second = slow.next
        slow.next = None

        prev = None
        rev = second

        while rev:
            nxt = rev.next
            rev.next = prev
            prev = rev
            rev = nxt

        first = head
        second = prev

        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2








            

            




            
   


