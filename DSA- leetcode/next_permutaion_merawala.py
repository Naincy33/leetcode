from itertools import permutations

class SolutionBruteForce:
    def nextPermutation(self, nums):
        # Step 1: Generate all permutations (as tuples)
        all_perms = sorted(set(permutations(nums)))  # remove duplicates, sort lexicographically
        
        # Step 2: Find index of current permutation
        current_index = all_perms.index(tuple(nums))
        
        # Step 3: Get next permutation (if exists), else smallest
        if current_index + 1 < len(all_perms):
            next_perm = all_perms[current_index + 1]
        else:
            next_perm = all_perms[0]
        
        # Step 4: Modify nums in place
        for i in range(len(nums)):
            nums[i] = next_perm[i]
        
        return nums


# 🔹 Example
nums = [1, 1, 5]
print("Brute Force Output:", SolutionBruteForce().nextPermutation(nums))  # [1, 5, 1]
