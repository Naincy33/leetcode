def findMin(nums):
    left, right = 0, len(nums) - 1

    print(f"Initial array: {nums}")
    print("----------------------------------")

    while left < right:
        mid = (left + right) // 2
        print(f"Left={left}, Mid={mid}, Right={right}, "
              f"nums[Left]={nums[left]}, nums[Mid]={nums[mid]}, nums[Right]={nums[right]}")

        # Case 1: minimum is in the right half
        if nums[mid] > nums[right]:
            print("➡ nums[mid] > nums[right], so min is in right half")
            left = mid + 1
        # Case 2: minimum is in the left half (including mid)
        else:
            print("⬅ nums[mid] <= nums[right], so min is in left half")
            right = mid

        print(f"Now Left={left}, Right={right}")
        print("----------------------------------")

    print(f"✅ Minimum element found: {nums[left]} at index {left}")
    return nums[left]


# 🧩 Example Run
nums = [4,5,6,7,0,1,2]
result = findMin(nums)
print(f"\nFinal Output: {result}")
