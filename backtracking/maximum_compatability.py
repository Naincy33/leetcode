class Solution:
    def maxCompatibilitySum(self, students, mentors):

        m = len(students)
        n = len(students[0])

        def score(s, t):

            cnt = 0

            for i in range(n):

                if s[i] == t[i]:
                    cnt += 1

            return cnt

        used = [False] * m

        ans = [0]

        def backtrack(student_index, total):

            if student_index == m:

                ans[0] = max(ans[0], total)
                return

            for mentor_index in range(m):

                if not used[mentor_index]:

                    used[mentor_index] = True

                    curr_score = score(
                        students[student_index],
                        mentors[mentor_index]
                    )

                    backtrack(
                        student_index + 1,
                        total + curr_score
                    )

                    used[mentor_index] = False

        backtrack(0, 0)

        return ans[0]
# Time complexity: O(m!) where m is the number of students/mentors, due to the backtracking approach
# Space complexity: O(m) due to the used array and the recursion stack
solution = Solution()
students = [[1, 1, 0], [1, 0, 1], [0, 0, 1]]
mentors = [[1, 0, 0], [0, 0, 1], [1, 1, 0]]
print(solution.maxCompatibilitySum(students, mentors))  