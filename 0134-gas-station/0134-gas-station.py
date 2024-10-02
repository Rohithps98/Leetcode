class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        total,res = 0,0
        for i in range(len(gas)):
            total+=gas[i]-cost[i]
            if total<0:
                res = i+1
                total = 0
        return res
        # if sum(gas)<sum(cost):
        #     return -1
        # total,res = 0,0
        # for i in range(len(gas)):
        #     total+=(gas[i]-cost[i])
        #     if total<0:
        #         total = 0
        #         res = i+1
        # return res
#         n = len(gas)
#         total_gas = 0
#         total_cost = 0
#         current_gas = 0
#         start_index = 0
#         for i in range(n):
#             total_gas += gas[i]
#             total_cost += cost[i]
#             current_gas += gas[i]-cost[i]
            
#             if current_gas<0:
#                 start_index = i+1
#                 current_gas = 0
#         if total_gas<total_cost:
#             return -1
#         return start_index