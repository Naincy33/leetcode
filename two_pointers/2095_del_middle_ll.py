class Solution:
    def deleteMiddle(self, head ):

       
        if not head.next:
            return None

        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        
        prev.next = slow.next

        return head
# Time complexity: O(n) where n is the number of nodes in the linked list
# Space complexity: O(1) since we are modifying the linked list in place and using only a constant amount of extra space
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next        


solution = Solution()
# Create linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)       
head.next.next.next.next = ListNode(5)
new_head = solution.deleteMiddle(head)
# Print the modified linked list
current = new_head
while current:
    print(current.val, end=" -> ")
    current = current.next
# Output: 1 -> 2 -> 4 -> 5  