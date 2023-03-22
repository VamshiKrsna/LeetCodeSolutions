# Problem No. 1342
# Number of Steps to Reduce a Number to Zero
class Solution:
    def numberOfSteps(self, num: int) -> int:
        temp = num
        count = 0
        while temp>0:
            if temp%2==0:
                temp/= 2
                count+=1
            elif temp%2!=0:
                temp-=1
                count+=1
        return count