class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lst = sorted(nums)

        i, j = 0, len(nums) - 1

        while i < j:
            curr = lst[i] + lst[j]
            if curr < target:
                i += 1
            elif curr > target:
                j -= 1
            else:
                ret = []
                for (dex, val) in enumerate(nums):
                    if val == lst[i] or val == lst[j]:
                        ret.append(dex)
                
                return ret