import heapq
from collections import defaultdict

class Solution:
    def medianSlidingWindow(self, nums, k):

        small = []
        large = []
        delayed = defaultdict(int)

        small_size = [0]
        large_size = [0]

        def prune(heap):
            while heap:
                if heap is small:
                    num = -heap[0]
                else:
                    num = heap[0]

                if delayed[num] > 0:
                    delayed[num] -= 1
                    heapq.heappop(heap)
                else:
                    break

        def balance():

            if small_size[0] > large_size[0] + 1:
                num = -heapq.heappop(small)
                heapq.heappush(large, num)

                small_size[0] -= 1
                large_size[0] += 1

                prune(small)

            elif small_size[0] < large_size[0]:
                num = heapq.heappop(large)
                heapq.heappush(small, -num)

                large_size[0] -= 1
                small_size[0] += 1

                prune(large)

        def add(num):

            if not small or num <= -small[0]:
                heapq.heappush(small, -num)
                small_size[0] += 1
            else:
                heapq.heappush(large, num)
                large_size[0] += 1

            balance()

        def remove(num):

            delayed[num] += 1

            if num <= -small[0]:
                small_size[0] -= 1
            else:
                large_size[0] -= 1

            prune(small)
            prune(large)

            balance()

        def get_median():

            if k % 2 == 1:
                return float(-small[0])

            else:
                return (-small[0] + large[0]) / 2.0

        result = []

        # First window
        for i in range(k):
            add(nums[i])

        result.append(get_median())

        # Slide window
        for i in range(k, len(nums)):

            add(nums[i])

            remove(nums[i - k])

            result.append(get_median())

        return result