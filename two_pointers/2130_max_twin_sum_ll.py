class Solution:
    def pairSum(self, head):
        # Find middle
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse second half
        prev = None
        curr = slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Find maximum twin sum
        max_sum = 0
        first = head
        second = prev

        while second:
            max_sum = max(max_sum, first.val + second.val)
            first = first.next
            second = second.next

        return max_sum
# Time complexity: O(n) where n is the number of nodes in the linked list
# Space complexity: O(1) since we are modifying the linked list in place and using only a constant amount of extra space            
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
solution = Solution()
# Create linked list: 1 -> 2 -> 3 -> 4
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
print(solution.pairSum(head))  # Output: 5 (1 + 4 or 2 + 3) 