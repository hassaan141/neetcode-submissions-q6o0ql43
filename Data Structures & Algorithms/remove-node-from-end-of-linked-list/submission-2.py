# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        count = 0
        temp = head
        # 8 - 2
        # 1 2 3 4 5 6 7 8 
        while temp:
            count += 1
            temp = temp.next 

        if count == n:
            head = head.next
            return head

        out = head
        for i in range(count - n -1):
            print(out.val)
            out = out.next
        
        print(f'The value is {out.val}')
        out.next = out.next.next
        print(out.val)

        return head