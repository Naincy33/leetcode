class Solution(object):
    def isBalanced(self, num):
        even_sum = 0
        odd_sum = 0
        length= len(num)
        for i in range(length):
            if i % 2 == 0:
                even_sum += int(num[i])
            else:
                odd_sum += int(num[i])
        return even_sum == odd_sum