# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # Attach remaining list
        if list1:
            tail.next = list1
        else:
            tail.next = list2

        return dummy.next

def createLinkedList(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for x in arr[1:]:
        curr.next = ListNode(x)
        curr = curr.next
    return head

def printList(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()


obj = Solution()

list1 = [1,1,2,3,4,5]
list2 = [1,2,2,3,4,7]

l1 = createLinkedList(list1)
l2 = createLinkedList(list2)

merged_head = obj.mergeTwoLists(l1, l2)

printList(merged_head)
