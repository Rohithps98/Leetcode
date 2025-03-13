class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        
        def can_zero_array(k):
            # Use line sweep technique to efficiently calculate maximum possible decrements
            # at each position after applying first k queries
            decrements = [0] * (n + 1)
            
            for i in range(k):
                l, r, val = queries[i]
                decrements[l] += val  # Add val at start of range
                decrements[r+1] -= val  # Subtract val after end of range
            
            # Calculate prefix sum to get actual decrement values at each position
            current_decrement = 0
            for i in range(n):
                current_decrement += decrements[i]
                # If decrement is less than the value at position i, we can't make it zero
                if current_decrement < nums[i]:
                    return False
            
            return True
        
        # Binary search for the answer
        left, right = 0, len(queries)
        result = -1
        
        while left <= right:
            mid = (left + right) // 2
            
            if can_zero_array(mid):
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return result