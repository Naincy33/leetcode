class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        jobs = list(zip(startTime, endTime, profit))
        jobs.sort(key=lambda x: x[1])   # sort by end time

        n = len(jobs)

        # dp[i] = max profit considering jobs up to index i
        dp = [0] * n
        dp[0] = jobs[0][2]

        for i in range(1, n):
            start, end, prof = jobs[i]

            # profit if we take current job
            take = prof

            # binary search to find last job that doesn't overlap
            left, right = 0, i - 1
            idx = -1

            while left <= right:
                mid = (left + right) // 2
                if jobs[mid][1] <= start:   # end <= start (allowed)
                    idx = mid
                    left = mid + 1
                else:
                    right = mid - 1

            if idx != -1:
                take += dp[idx]

            # max of taking or skipping current job
            dp[i] = max(dp[i-1], take)

        return dp[-1]
obj = Solution()
print(obj.jobScheduling([1,2,3,3],[3,4,5,6],[50,10,40,70]))