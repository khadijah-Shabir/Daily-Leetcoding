# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head and not head.next: 
            return 
        # find the middle of the list
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        #reverse the list from mid
        second=slow.next
        prev=slow.next=None
        while second:
            temp=second.next
            second.next=prev
            prev=second
            second=temp

        second=prev
        first=head
        while second:
            temp1, temp2=first.next, second.next
            first.next, second.next=second,temp1
            first,second=temp1, temp2


    


        

        
        