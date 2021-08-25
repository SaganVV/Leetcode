class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow =  head
        fast = head
        while not ((fast is None) or (slow is None)):
            if (not fast) or (not fast.next) or (not fast.next.next):
                return False
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
              
 # Usef two-pointers technique. If we have a cycle then at some point slow and fast be equals. If we fast ended then we have no cycle
