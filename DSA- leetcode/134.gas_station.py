class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        start=0
        total_gas=0
        cur_gas=0

        for i in range(len(gas)):
            total_gas+= gas[i]-cost[i]
            cur_gas += gas[i]-cost[i]

            if cur_gas<0:
                start = i+1
                cur_gas=0

        return start if total_gas >=0 else -1
    
obj= Solution()
print(obj.canCompleteCircuit([1,2,3,4,5],[3,4,5,1,2]))