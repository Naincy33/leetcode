#!/usr/bin/env python3

# ---------- INPUT HERE ----------
n = 5
nums = [1, 2, 0, 4, 5]
# --------------------------------

from typing import List

def solve(n: int, nums: List[int]) -> None:
    zero_count = nums.count(0)

    prod_non_zero = 1
    for x in nums:
        if x != 0:
            prod_non_zero *= x

    prod = [0] * n

    if zero_count == 0:
        total = prod_non_zero
        for i in range(n):
            prod[i] = total // nums[i]

    elif zero_count == 1:
        for i in range(n):
            if nums[i] == 0:
                prod[i] = prod_non_zero
            else:
                prod[i] = 0
    else:
        pass

    # zero sum subarrays
    freq = {0: 1}
    prefix = 0
    zero_sum_count = 0

    for x in nums:
        prefix += x
        zero_sum_count += freq.get(prefix, 0)
        freq[prefix] = freq.get(prefix, 0) + 1

    print("Product Array:", *prod)
    print("Zero-sum Subarrays:", zero_sum_count)


solve(n, nums)
