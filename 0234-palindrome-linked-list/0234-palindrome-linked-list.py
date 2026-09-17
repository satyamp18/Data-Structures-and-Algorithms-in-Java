# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head):
        if not head or not head.next:
            return True

        # Step 1: Find the middle
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half
        prev = None
        curr = slow

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # prev is the head of the reversed second half
        second = prev
        first = head

        # Step 3: Compare both halves
        while second:
            if first.val != second.val:
                return False

            first = first.next
            second = second.next

        return True