# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.

 


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        copy_head = head
        i = 1
        while head:
            i+=1
            head = head.next
        j = 1
        while j<(i+1)//2:
            copy_head = copy_head.next
            j+=1
        return copy_head
