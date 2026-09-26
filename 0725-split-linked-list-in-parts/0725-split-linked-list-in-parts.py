class Solution:
    def splitListToParts(self, head, k):
        n = 0
        curr = head

        while curr:
            n += 1
            curr = curr.next

        base = n // k
        extra = n % k

        result = []
        curr = head

        for i in range(k):
            size = base + (1 if i < extra else 0)

            part_head = curr

            if size == 0:
                result.append(None)
                continue

            for _ in range(size - 1):
                curr = curr.next

            next_part = curr.next
            curr.next = None
            curr = next_part

            result.append(part_head)

        return result