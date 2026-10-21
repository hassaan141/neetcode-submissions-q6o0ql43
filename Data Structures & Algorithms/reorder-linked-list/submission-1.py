# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        if head is None:
            return None

        slow = head
        fast = head

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        # print(fast.val)
        # print(slow.val)

        l1_head = head
        l2_head = slow.next
        slow.next = None

        # flip l2

        prev = None
        l2_curr = l2_head

        while l2_curr:
            nxt = l2_curr.next
            l2_curr.next = prev
            prev = l2_curr
            l2_curr = nxt

        print("Printing List 1")
        self.printList(l1_head)
     
        print("Printing List 2")
        self.printList(prev)

        print(" ")

        while prev:
            tmp1 = l1_head.next
            tmp2 = prev.next

            l1_head.next = prev
            prev.next = tmp1

            l1_head = tmp1
            prev = tmp2
        
        return 


    
    
    def printList(self, head):
        
        curr = head

        while curr:
            print(curr.val)
            curr = curr.next






        