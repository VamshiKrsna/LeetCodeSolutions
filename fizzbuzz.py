class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            if i != 0:
                temp = i
                item = 0
                while temp != -1:
                    item += nums[temp]
                    temp -= 1
                res.insert(i, item)
            else :
                res.append(nums[i])
        return res
