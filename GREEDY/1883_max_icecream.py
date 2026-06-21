from typing import List

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        freq = [0] * (max(costs) + 1)

        for cost in costs:
            freq[cost] += 1

        count = 0

        for price in range(1, len(freq)):
            if freq[price] == 0:
                continue

            can_buy = min(freq[price], coins // price)

            count += can_buy
            coins -= can_buy * price

        return count
    
# Example usage:
solution = Solution()
print(solution.maxIceCream([1, 3, 2, 4, 1], 7))  # Output: 4
print(solution.maxIceCream([10, 6, 8, 7, 7, 8], 5))  # Output: 0
print(solution.maxIceCream([1, 6, 3, 1, 2, 5], 20))  # Output: 6