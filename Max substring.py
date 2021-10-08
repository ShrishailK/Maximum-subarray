class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        MaxSub = nums[0]
        cursum = 0
        Maxsubarray = [nums[0]]
        cursubarray = []
        for n in nums:
            if cursum < 0:
                cursum = 0
                cursubarray = []
            
            cursubarray.append(n)
            cursum += n
            if cursum>MaxSub:
                MaxSub = max(MaxSub,cursum)
                Maxsubarray = cursubarray[:] 
        
        #To print the subarray involved in the max summation
        print(Maxsubarray)
        return(MaxSub)    