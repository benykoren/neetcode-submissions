class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        resl = []
        for k in range(len(nums)):
            if k > 0 and nums[k] == nums[k-1]:
                continue
            i = k+1
            j = len(nums) -1
            while i < j:
                res = nums[k] + nums[i] + nums[j]
                if res == 0:
                    sug = [nums[k], nums[i], nums[j]]
                    if sug not in resl:
                        resl.append(sug)
                    j =j -1 
                    i =i+1
                elif res > 0:
                    j = j-1
                elif res < 0:
                    i = i+1
        return resl