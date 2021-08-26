# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    
        llist = head
        while llist:
            if llist.next:
                if llist.val == llist.next.val:
                    if llist.next.next:
                        llist.next = llist.next.next
                    else:
                        llist.next=None
                else:
                    llist = llist.next
            else:
                llist = llist.next
        return head
