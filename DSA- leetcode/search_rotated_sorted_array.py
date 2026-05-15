def search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        print(f"Left={left}, Mid={mid}, Right={right}, "
              f"nums[Left]={nums[left]}, nums[Mid]={nums[mid]}, nums[Right]={nums[right]}")

        # Found target
        if nums[mid] == target:
            print(f"✅ Found target {target} at index {mid}")
            return mid

        # Left half is sorted
        if nums[left] <= nums[mid]:
            print("Left half is sorted.")
            if nums[left] <= target < nums[mid]:
                print(f"Target {target} is in left half → move Right to mid-1")
                right = mid - 1
            else:
                print(f"Target {target} is not in left half → move Left to mid+1")
                left = mid + 1
        # Right half is sorted
        else:
            print("Right half is sorted.")
            if nums[mid] < target <= nums[right]:
                print(f"Target {target} is in right half → move Left to mid+1")
                left = mid + 1
            else:
                print(f"Target {target} is not in right half → move Right to mid-1")
                right = mid - 1

    print(f"❌ Target {target} not found in array.")
    return -1


# 🧩 Example Run:
nums = [4,5,6,7,0,1,2]
target = 0

result = search(nums, target)
print(f"\nFinal Output: {result}")
