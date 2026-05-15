class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result=[]
        def backtrack(i, curr, total):
            if total== target:
                result.append(curr[:])
                return
            if i>=len(candidates)or total>target:
                return

            curr.append(candidates[i])
            backtrack(i, curr,total+candidates[i])
            
            curr.pop()
            backtrack(i+1, curr,total)
        backtrack(0,[],0)
        return result
    
print(Solution().combinationSum([2,3,6,7],7))