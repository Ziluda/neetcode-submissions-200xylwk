class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create hashmap
        seen = {} # value: index

        # start looping through nums
        for i, num in enumerate(nums):
            diff = target - num
            # if the complement is found, the answer is found
            if diff in seen:
                return [seen[diff], i]
            
            seen[num] = i
        
        return # or raise ValueError("No two sum solution")